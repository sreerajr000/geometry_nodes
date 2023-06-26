import sys
sys.path.append(r'D:\blender\geometry_nodes\expression')
import bpy
import antlr4
from ExpressionLexer import ExpressionLexer
from ExpressionParser import ExpressionParser
from ExpressionVisitor import ExpressionVisitor

from collections import deque
def bfs_arrange_nodes(node_tree, root_node, base_spacing=20):
    visited = set()
    levels = {}
    max_positions = {}
    queue = deque([(root_node, 0)])

    while queue:
        node, level = queue.popleft()
        if node not in visited:
            visited.add(node)
            if level not in levels:
                levels[level] = []
            levels[level].append(node)

            for socket in node.inputs:
                for link in socket.links:
                    queue.append((link.from_node, level + 1))

            for socket in node.outputs:
                for link in socket.links:
                    queue.append((link.to_node, level + 1))

    max_x = 0
    for level, nodes in sorted(levels.items()):
        max_y = 0
        for node in nodes:
            node.location.x = max_x + base_spacing
            node.location.y = -max_y - base_spacing
            max_y += node.dimensions.y + base_spacing
        if nodes:
            max_x += max(node.dimensions.x for node in nodes) + base_spacing
            max_positions[level] = max_x

    max_x_position = max(max_positions.values())
    for level, nodes in levels.items():
        for node in nodes:
            node.location.x = max_x_position - node.location.x


    return node


class ExpressionEvalVisitor(ExpressionVisitor):
    def __init__(self, material):
        super().__init__()
        self.material = material
        self.nodes = ng.nodes
        self.links = ng.links
        self.current_y = 0
        self.current_x = 0
        self.variables = {}

    def create_node(self, type):
        node = self.nodes.new(type)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        node.location.x = self.current_x
        node.location.y = self.current_y
        self.current_y -= node.height + 100  # Moving y downward by the height of the node plus a little padding
        if self.current_y < -2000:  # Start a new column if the current one is too long
            self.current_y = 0
            self.current_x += 400  # Moving to a new column
        return node

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        expr_node = self.visit(ctx.expression())

        if var_name in self.nodes:
            self.nodes.remove(self.nodes[var_name])

        expr_node.name = var_name
        self.variables[var_name] = expr_node

        return expr_node

    def visitAdditiveExp(self, ctx):
        nodes = [self.visit(c) for c in ctx.multiplicativeExp()]
        for i in range(1, len(nodes)):
            math_node = self.create_node('ShaderNodeMath')
            math_node.operation = 'ADD' if ctx.getChild(i*2-1).getText() == "+" else 'SUBTRACT'
            if isinstance(nodes[i-1], bpy.types.Node):
                self.links.new(nodes[i-1].outputs[0], math_node.inputs[0])
            else:
                math_node.inputs[0].default_value = nodes[i-1]
            if isinstance(nodes[i], bpy.types.Node):
                self.links.new(nodes[i].outputs[0], math_node.inputs[1])
            else:
                math_node.inputs[1].default_value = nodes[i]
            nodes[i] = math_node

        return nodes[-1]

    def visitMultiplicativeExp(self, ctx):
        nodes = [self.visit(c) for c in ctx.unaryExp()]
        for i in range(1, len(nodes)):
            math_node = self.create_node('ShaderNodeMath')
            math_node.operation = 'MULTIPLY' if ctx.getChild(i*2-1).getText() == "*" else 'DIVIDE'
            if isinstance(nodes[i-1], bpy.types.Node):
                self.links.new(nodes[i-1].outputs[0], math_node.inputs[0])
            else:
                math_node.inputs[0].default_value = nodes[i-1]
            if isinstance(nodes[i], bpy.types.Node):
                self.links.new(nodes[i].outputs[0], math_node.inputs[1])
            else:
                math_node.inputs[1].default_value = nodes[i]
            nodes[i] = math_node

        return nodes[-1]

    def visitUnaryExp(self, ctx):
        if ctx.unaryOp() is not None:
            node = self.create_node('ShaderNodeMath')
            node.operation = ctx.unaryOp().getText().upper()
            child_node = self.visit(ctx.expression())
            if isinstance(child_node, bpy.types.Node):
                self.links.new(child_node.outputs[0], node.inputs[0])
            else:
                node.inputs[0].default_value = child_node
            return node
        else:
            return self.visit(ctx.binaryExp())

    def visitBinaryExp(self, ctx):
        if ctx.binaryOp() is not None:
            node = self.create_node('ShaderNodeMath')
            node.operation = ctx.binaryOp().getText().upper()
            child_nodes = [self.visit(c) for c in ctx.expression()]
            if isinstance(child_nodes[0], bpy.types.Node):
                self.links.new(child_nodes[0].outputs[0], node.inputs[0])
            else:
                node.inputs[0].default_value = child_nodes[0]
            if isinstance(child_nodes[1], bpy.types.Node):
                self.links.new(child_nodes[1].outputs[0], node.inputs[1])
            else:
                node.inputs[1].default_value = child_nodes[1]
            return node
        else:
            return self.visit(ctx.factor())

        
    def visitFactor(self, ctx):
        if ctx.NUMBER():
            # Just return the number itself for now, we will handle this later
            return float(ctx.NUMBER().getText())
        elif ctx.ID():
            # Lookup the variable node
            var_name = ctx.ID().getText()
            return self.variables[var_name]
        else:
            # Visit the expression in parentheses
            return self.visit(ctx.expression())

def parse_expression(input_str, material):
    input_stream = antlr4.InputStream(input_str)
    lexer = ExpressionLexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = ExpressionParser(token_stream)
    tree = parser.program()

    visitor = ExpressionEvalVisitor(material)
    return visitor.visit(tree)


# usage
expr = '''
a = 3.14 * 2
b = a + 2.71
c = b * b - 4 * a * 2.71
d = (3 + 5) / 2
e = d * d - 4 * a * c
f = 2 * (3.14 + 2.71)
g = 2 * f + 3 * (4 - 1)
h = g / 2 * (2 + a)
i = h - e
j = (i + e) / 2
'''

expr = '''
result = pow((a + b), max(c, d)) * sin(e) - cos(f / g) * tan(abs(h)) + round(i, j) * sqrt(k);
'''
ng =  bpy.data.node_groups['Geometry Nodes']
parse_expression(expr, ng)

bfs_arrange_nodes(ng, ng.nodes[-1])