import sys

sys.path.append(r'F:\geometry_nodes')
import geometry_nodes as gn
import bpy
import importlib
importlib.reload(gn)

active_obj = bpy.context.active_object
gn_name = 'Geometry Nodes'
# Convert these later to classes
inputs = [{'name': 'Geometry', 'type': 'NodeSocketGeometry'}, 
{'name': 'Value', 'type': 'NodeSocketFloat'},
]
outputs = inputs
ng = gn.create_gn(gn_name, inputs, outputs)
active_obj.modifiers['GeometryNodes'].node_group = ng

# TODO Convert functions to groups

cube = gn.mesh_cube(ng)



bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

gn.bfs_arrange_nodes(ng, ng.nodes['Group Output'])