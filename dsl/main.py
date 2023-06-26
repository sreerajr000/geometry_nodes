import sys
sys.path.append(r'D:\blender\geometry_nodes\dsl')
import bpy
from antlr4 import *
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

class Generator(ExpressionVisitor):
    def __init__(self, ng):
        super().__init__()
        self.nodes = ng.nodes
        self.links = ng.links
        self.variables = {}
        self.current_y = 0
        self.current_x = 0
    
    def visitGroup_def(self, ctx:ExpressionParser.Group_defContext):
        group_def = {'inputs': [], 'outputs': []}
        group_name = ctx.ID().getText()

        return_statement = ctx.return_statement()
        outputs = [x.getText() for x in return_statement.ID()]
        group_def['outputs'] = outputs

        parameters = ctx.parameters().parameter()
        for param in parameters:
            param_type = param.type_().getText()
            param_name = param.ID().getText()
            default_value = param.default_value().getText() if param.default_value() is not None else None
            group_def['inputs'].append([param_type, param_name, default_value])
        
        self.variables[group_name] = group_def
        return self.visitChildren(ctx)
    
    
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
        # Get the variable name
        var_name = ctx.ID().getText()

        # Visit the expression
        expr_node = self.visit(ctx.expression())

        # Store the node for this variable
        self.variables[var_name] = expr_node

        return expr_node


    def visitExpression(self, ctx):
        # Visit all terms
        nodes = [self.visit(t) for t in ctx.term()]

        # Combine the nodes using addition or subtraction
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

    def visitTerm(self, ctx):
        # Visit all factors
        nodes = [self.visit(f) for f in ctx.factor()]

        # Combine the nodes using multiplication or division
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

    
def main():
    expr = '''
    group main():
        a = 3.14 * 2;
        b = a + 2.71;
        c = b * b - 4 * a * 2.71;
        d = (3 + 5) / 2;
        e = d * d - 4 * a * c;
        f = 2 * (3.14 + 2.71);
        g = 2 * f + 3 * (4 - 1);
        h = g / 2 * (2 + a);
        i = h - e;
        j = (i + e) / 2;
        return j;
    '''

    input_stream = InputStream(expr)
    lexer = ExpressionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExpressionParser(stream)
    tree = parser.file_()

    ng =  bpy.data.node_groups['Geometry Nodes']
    generator = Generator(ng)
    
    print("Starting visitor traversal...")
    result = generator.visit(tree)
    print(result)
    
    print("Visitor traversal completed.")
    print("Result:", generator.variables)

    # bfs_arrange_nodes(ng, ng.nodes[-1])

main()
