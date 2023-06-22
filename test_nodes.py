import sys
sys.path.append(r'F:\geometry_nodes')
import geometry_nodes as gn
import bpy

# active_obj = bpy.context.active_object
# gn_name = 'Geometry Nodes'
# # Convert these later to classes
# inputs = [{'name': 'string', 'type': 'NodeSocketGeometry'}, 
# {'name': 'bool', 'type': 'NodeSocketBool'},
# {'name': 'material', 'type': 'NodeSocketMaterial'},
# {'name': 'vector', 'type': 'NodeSocketVector'},
# {'name': 'integer', 'type': 'NodeSocketInt'},
# {'name': 'geometry', 'type': 'NodeSocketString'},
# {'name': 'collection', 'type': 'NodeSocketCollection'},
# {'name': 'texture', 'type': 'NodeSocketTexture'},
# {'name': 'float', 'type': 'NodeSocketFloat'},
# {'name': 'color', 'type': 'NodeSocketColor'},
# {'name': 'object', 'type': 'NodeSocketObject'},
# {'name': 'image', 'type': 'NodeSocketImage'},
# {'name': 'rot', 'type': 'NodeSocketVectorEuler'},
# ]
# outputs = inputs
# nodetree = gn.create_gn(gn_name, inputs, outputs)
# active_obj.modifiers['GeometryNodes'].node_group = nodetree

# vr = gn.vector_rotate()

# bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# bfs_arrange_nodes(nodetree, nodetree.nodes['Group Output'])


import re

def camel_to_snake(camel_str):
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()


ng = bpy.context.space_data.edit_tree
classes = dir(bpy.types)

for cls in classes:
    try:
        ng.nodes.new(cls)
    except:
        pass

nodes = [x.bl_idname for x in ng.nodes]

COMMON_PROPS = {'update', 'bl_label', 'outputs', 'output_template', 'location', 'socket_value_update', 'mute', 'bl_rna', 'type', 'input_template', 'is_registered_node_type', 'use_custom_color', 'poll_instance', 'bl_height_max', 'hide', 'show_preview', 'poll', 'bl_width_min', 'show_options', 'width_hidden', 'bl_width_default', 'dimensions', 'internal_links', 'bl_height_min', '__doc__', 'label', 'rna_type', 'show_texture', 'width', 'bl_width_max', '__slots__', 'select', 'inputs', 'height', 'bl_height_default', 'bl_static_type', 'bl_icon', 'draw_buttons', '__module__', 'bl_description', 'color', 'draw_buttons_ext', 'name', 'bl_idname', 'parent'}

def get_dv(socket):
    if socket.type == 'VALUE': return str(socket.default_value) if not isinstance(socket.default_value, str) else f"'{socket.default_value}'"
    if socket.type == 'VECTOR': return str(list(socket.default_value))
    return 'None'

fn = 'import bpy\nng=bpy.context.space_data.edit_tree\n'
for node in ng.nodes:
    inputs = node.inputs.keys()
    outputs = node.outputs.keys()
    props = set(dir(node)).difference(COMMON_PROPS)

    inputs_default = [node.inputs[x] for x in inputs]

    fn_name = node.bl_idname
    fn_name = fn_name.replace("ShaderNode", "")
    fn_name = fn_name.replace("FunctionNode", "")
    fn_name = fn_name.replace("GeometryNode", "")
    fn_name = fn_name.replace("Node", "")
    fn_name = camel_to_snake(fn_name)

    args = [x.lower().replace(' ', '_') for x in inputs]
    actual_args = args.copy()
    args = zip(args, inputs_default)
    args = [x+'='+get_dv(y) for x,y in args]
    args = ', '.join(args)

    props = [x+'='+ str(getattr(node, x)) if not isinstance(getattr(node, x), str) else f"{x}='{getattr(node, x)}'"  for x in props]
    props = ', '.join(props)
    args_props = f'{args}, {props}' if props is not None else f'{args}'
    fn += f'''
def {fn_name}({args_props}):
    node = ng.nodes.new("{node.bl_idname}")
'''
    for inp,arg in zip(inputs, actual_args):
        fn += f'''    if isinstance({arg}, bpy.types.NodeSocket):
        ng.links.new(node.inputs["{inp}"], {arg})
    else:
        node.inputs["{inp}"] = {arg}\n'''
    
    props = set(dir(node)).difference(COMMON_PROPS)
    for prop in props:
        fn += f'    node.{prop} = {prop}\n'


with open(r'F:\geometry_nodes\generated_nodes.py', 'w') as f:
    f.write(fn)

# print('Outputs', node_outputs)
# print('Inputs', node_inputs)
# print('Properties', node_props)