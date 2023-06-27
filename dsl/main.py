import sys
sys.path.append(r'D:\blender\geometry_nodes\dsl')
import bpy
from antlr4 import *
from gnLexer import gnLexer
from gnParser import gnParser
from gnVisitor import gnVisitor

from collections import deque

socket_dict = {
    'geo': 'NodeSocketGeometry',
    'int': 'NodeSocketInt',
    'float': 'NodeSocketFloat',
    'col': 'NodeSocketColor',
    'mat': 'NodeSocketMaterial',
    'coll': 'NodeSocketCollection',
    'str': 'NodeSocketString',
    'vec': 'NodeSocketVector',
    'img': 'NodeSocketImage',
    'obj': 'NodeSocketObject',
    'bool': 'NodeSocketBool',
    'tex': 'NodeSocketTexture'
}

def assign_default_value(socket, value):
    if isinstance(socket, bpy.types.NodeSocketInterfaceMaterial) or isinstance(socket, bpy.types.NodeSocketMaterial):
        socket.default_value = bpy.data.materials[value]
    elif isinstance(socket, bpy.types.NodeSocketInterfaceObject) or isinstance(socket, bpy.types.NodeSocketObject):
        socket.default_value = bpy.data.objects[value]
    elif isinstance(socket, bpy.types.NodeSocketInterfaceCollection) or isinstance(socket, bpy.types.NodeSocketCollection):
        socket.default_value = bpy.data.collections[value]
    elif isinstance(socket, bpy.types.NodeSocketInterfaceTexture) or isinstance(socket, bpy.types.NodeSocketTexture):
        socket.default_value = bpy.data.textures[value]
    elif isinstance(socket, bpy.types.NodeSocketInterfaceImage) or isinstance(socket, bpy.types.NodeSocketImage):
        socket.default_value = bpy.data.images[value]
    else:
        socket.default_value = value

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

def id_to_label(s):
    s = s.replace('_', ' ')
    s = s.title()
    return s


class Generator(gnVisitor):
    def __init__(self, ng):
        super().__init__()
        self.nodes = ng.nodes
        self.links = ng.links
        self.variables = {}
        self.current_y = 0
        self.current_x = 0
        self.ng = ng
    
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

    # Visit a parse tree produced by gnParser#program.
    def visitProgram(self, ctx:gnParser.ProgramContext):
        return self.visitChildren(ctx)

     # Visit a parse tree produced by gnParser#group.
    def visitGroup(self, ctx:gnParser.GroupContext):
        # If group name is not main, a new node group should be created and added to the main nodetree
        params = self.visit(ctx.parameters()) # Params will return group inputs
        outputs = self.visit(ctx.block()) # Blocks will return group outputs

        if ctx.ID().getText() == 'main':
            ng = self.ng
        else:
            ng = bpy.data.node_groups.new(ctx.ID().getText(), 'GeometryNodeTree')
        
        group_input = ng.nodes.new('NodeGroupInput')
        group_output = ng.nodes.new('NodeGroupOutput')

        for param in params:
            ng.inputs.new(socket_dict[param['type']], id_to_label(param['id']))
            if 'value' in param:
                assign_default_value(ng.inputs[-1], param['value'])
        
        # Have to find some way to do the type inference
        # for output in outputs:
        #     ng.outputs.new(socket_dict[param['type']], id_to_label(param['id'])) 



    # Visit a parse tree produced by gnParser#parameters.
    def visitParameters(self, ctx:gnParser.ParametersContext):
        params = []
        for param in ctx.parameter():
            params.append(self.visit(param))
        return params


    # Visit a parse tree produced by gnParser#parameter.
    def visitParameter(self, ctx:gnParser.ParameterContext):
        param = {}
        if ctx.value() is not None:
            param['value'] = self.visit(ctx.value())
        param['id'] = ctx.ID().getText()
        param['type'] = ctx.type_().getText()
        return param

    # Visit a parse tree produced by gnParser#type.
    def visitType(self, ctx:gnParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gnParser#value.
    def visitValue(self, ctx:gnParser.ValueContext):
        value = ctx.getText()
        if value in ['true', 'false']:
            return bool(value)
        if value[0] == '"' and value[-1] == '"':
            return value[1:-1]
        return float(value)


    # Visit a parse tree produced by gnParser#block.
    def visitBlock(self, ctx:gnParser.BlockContext):
        ret = self.visit(ctx.exprList())
        for statement in ctx.statement():
            self.visit(statement)
        return ret


    # Visit a parse tree produced by gnParser#statement.
    def visitStatement(self, ctx:gnParser.StatementContext):
        for expr in ctx.expr():
            self.visit(expr)

    # Visit a parse tree produced by gnParser#expr.
    def visitExpr(self, ctx:gnParser.ExprContext):
        if ctx.getChildCount() == 3 and ctx.op is not None:
            if ctx.op.text == '*':
                print(ctx.getChild(0).getText(), ctx.getChild(2).getText())
            elif ctx.op.text == '/':
                print(ctx.getChild(0).getText(), ctx.getChild(2).getText())
            elif ctx.op.text == '+':
                print(ctx.getChild(0).getText(), ctx.getChild(2).getText())
            elif ctx.op.text == '-':
                print(ctx.getChild(0).getText(), ctx.getChild(2).getText())
        elif ctx.getChildCount() == 1:
            print(ctx.getText())
        for expr in ctx.expr():
            self.visit(expr)


    # Visit a parse tree produced by gnParser#exprList.
    def visitExprList(self, ctx:gnParser.ExprListContext):
        return self.visitChildren(ctx)

    
    
    
def main():
    with open(r'D:\blender\geometry_nodes\dsl\test.dsl', 'r') as f:
        expr = f.read()

    input_stream = InputStream(expr)
    lexer = gnLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gnParser(stream)
    tree = parser.program()

    bpy.ops.node.new_geometry_nodes_modifier()
    ng =  bpy.data.node_groups['Geometry Nodes']
    generator = Generator(ng)
    
    print("Starting visitor traversal...")
    result = generator.visit(tree)
    # print(result)
    
    print("Visitor traversal completed.")

    # bfs_arrange_nodes(ng, ng.nodes[-1])

main()
