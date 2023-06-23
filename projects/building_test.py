import importlib
import bpy
import geometry_nodes as gn
import sys
sys.path.append(r'F:\geometry_nodes')
importlib.reload(gn)

def o(n, s='Value'):
    return n.outputs[s]

active_obj = bpy.context.active_object
gn_name = 'Geometry Nodes'

inputs = [
    {'name': 'Geometry', 'type': 'NodeSocketGeometry'},
    {'name': 'Length', 'type': 'NodeSocketInt', 'default_value': 3},
    {'name': 'Width', 'type': 'NodeSocketInt', 'default_value': 3},
    {'name': 'Height', 'type': 'NodeSocketInt', 'default_value': 3},
]
outputs = [
    {'name': 'Geometry', 'type': 'NodeSocketGeometry'},
]
ng, g_in, g_out = gn.create_gn(gn_name, inputs, outputs)
active_obj.modifiers['GeometryNodes'].node_group = ng


# Actual Nodes
l = gn.math(ng, o(g_in, 'Length'), 1)
w = gn.math(ng, g_in.outputs['Width'], 1)
h = gn.math(ng, g_in.outputs['Height'], 1)
offset_h = gn.math(ng, g_in.outputs['Height'], 2, operation='DIVIDE')
offset = gn.combine_xyz(ng, 0, 0, o(offset_h))
lwh = gn.combine_xyz(ng, g_in.outputs['Length'], g_in.outputs['Width'], g_in.outputs['Height'])


cube = gn.mesh_cube(ng, size=lwh.outputs['Vector'], vertices_x=l.outputs['Value'], vertices_y=w.outputs['Value'], vertices_z=h.outputs['Value'])
tr_cube = gn.transform(ng, cube.outputs['Mesh'], translation=offset.outputs['Vector'])


# Outputs
ng.links.new(tr_cube.outputs['Geometry'], g_out.inputs['Geometry'])



bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
gn.bfs_arrange_nodes(ng, ng.nodes['Group Output'], base_spacing=75)
