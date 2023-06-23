import bpy
from math import inf
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


def create_group_socket(nodetree, node, data, inout='in'):
    def update_socket_info(socket, socket_info):
        dv_dict = {
            'NodeSocketBool': False, 
            'NodeSocketString': '',
            'NodeSocketMaterial': None,
            'NodeSocketVector': (0,0,0),
            'NodeSocketInt': 0,
            'NodeSocketFloat': 0.0,
            'NodeSocketColor': (0,0,0,0),
            'NodeSocketImage': None,
            'NodeSocketCollection': None,
            'NodeSocketTexture': None,
            'NodeSocketObject': None,
            'NodeSocketGeometry': None,
            'NodeSocketVectorEuler': (0,0,0)
            
        }
        socket_type = socket_info.get('type')
        socket.description = socket_info.get('description', '')
        socket.default_attribute_name = socket_info.get('default_attribute_name', '')
        socket.hide_value = socket_info.get('hide_value', False)
        if socket_type != 'NodeSocketGeometry':
            socket.default_value = socket_info.get('default_value', dv_dict[socket_type])
        
        if socket_type in ['NodeSocketVector', 'NodeSocketFloat', 'NodeSocketVectorEuler']:
            socket.min_value = socket_info.get('min_value', -inf)
            socket.max_value = socket_info.get('max_value', inf)
        elif socket_type == 'NodeSocketInt':
            socket.min_value = socket_info.get('min_value', -2147483648)
            socket.max_value = socket_info.get('max_value', 2147483647)
            
        # Update Attribute Domain for out
        if inout == 'out' and socket_type in ['NodeSocketVector', 'NodeSocketFloat', 'NodeSocketBool', 'NodeSocketInt', 'NodeSocketColor', 'NodeSocketVectorEuler']:
            socket.attribute_domain = socket_info.get('attribute_domain', 'POINT')
            
            
 
    for socket_info in data:
        if inout == 'in':
            socket = nodetree.inputs.new(socket_info['type'], socket_info['name'])
        else:
            socket = nodetree.outputs.new(socket_info['type'], socket_info['name'])
        update_socket_info(socket, socket_info)

    

def create_gn(name, inputs, outputs):
    if name in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups[name])
    nodetree = bpy.data.node_groups.new(name, 'GeometryNodeTree')
    inps = nodetree.nodes.new('NodeGroupInput')
    outs = nodetree.nodes.new('NodeGroupOutput')
    
    create_group_socket(nodetree, inps, inputs, 'in')
    create_group_socket(nodetree, outs, outputs, 'out')
    return nodetree

def create_node_function(node_type):
    def create_node(**kwargs):
        # Get the active object
        obj = bpy.context.active_object

        # Ensure object has a geometry node tree
        if not obj.modifiers:
            mod = obj.modifiers.new(name="GeometryNodes", type='NODES')
            node_group = bpy.data.node_groups.new(name="NodeGroup", type='GeometryNodeTree')
            mod.node_group = node_group
        else:
            mod = next((m for m in obj.modifiers if m.type == 'NODES'), None)
            if not mod:
                mod = obj.modifiers.new(name="GeometryNodes", type='NODES')
                node_group = bpy.data.node_groups.new(name="NodeGroup", type='GeometryNodeTree')
                mod.node_group = node_group
            else:
                node_group = mod.node_group

        # Add a new node of the specified type to the node tree
        new_node = node_group.nodes.new(node_type)

        # Assign the inputs
        for input_name, input_value in kwargs.items():
            if input_name in new_node.inputs:
                if isinstance(input_value, tuple):
                    # input_value is a tuple, create a link
                    source_node = input_value[0]
                    source_socket_name = input_value[1]
                    
                    if source_socket_name in source_node.outputs:
                        node_group.links.new(new_node.inputs[input_name], source_node.outputs[source_socket_name])
                else:
                    # input_value is a value, assign it
                    new_node.inputs[input_name].default_value = input_value

        return new_node

    return create_node


# frame = create_node_function('NodeFrame')
# function_align_euler_to_vector = create_node_function('FunctionNodeAlignEulerToVector')
# function_boolean_math = create_node_function('FunctionNodeBooleanMath')
# function_combine_color = create_node_function('FunctionNodeCombineColor')
# function_compare = create_node_function('FunctionNodeCompare')
# function_float_to_int = create_node_function('FunctionNodeFloatToInt')
# function_input_bool = create_node_function('FunctionNodeInputBool')
# function_input_color = create_node_function('FunctionNodeInputColor')
# function_input_int = create_node_function('FunctionNodeInputInt')
# function_input_special_characters = create_node_function('FunctionNodeInputSpecialCharacters')
# function_input_string = create_node_function('FunctionNodeInputString')
# function_input_vector = create_node_function('FunctionNodeInputVector')
# function_random_value = create_node_function('FunctionNodeRandomValue')
# function_replace_string = create_node_function('FunctionNodeReplaceString')
# function_rotate_euler = create_node_function('FunctionNodeRotateEuler')
# function_separate_color = create_node_function('FunctionNodeSeparateColor')
# function_slice_string = create_node_function('FunctionNodeSliceString')
# function_string_length = create_node_function('FunctionNodeStringLength')
# function_value_to_string = create_node_function('FunctionNodeValueToString')
# accumulate_field = create_node_function('GeometryNodeAccumulateField')
# attribute_domain_size = create_node_function('GeometryNodeAttributeDomainSize')
# attribute_statistic = create_node_function('GeometryNodeAttributeStatistic')
# bound_box = create_node_function('GeometryNodeBoundBox')
# capture_attribute = create_node_function('GeometryNodeCaptureAttribute')
# collection_info = create_node_function('GeometryNodeCollectionInfo')
# convex_hull = create_node_function('GeometryNodeConvexHull')
# corners_of_face = create_node_function('GeometryNodeCornersOfFace')
# corners_of_vertex = create_node_function('GeometryNodeCornersOfVertex')
# curve_arc = create_node_function('GeometryNodeCurveArc')
# curve_endpoint_selection = create_node_function('GeometryNodeCurveEndpointSelection')
# curve_handle_type_selection = create_node_function('GeometryNodeCurveHandleTypeSelection')
# curve_length = create_node_function('GeometryNodeCurveLength')
# curve_of_point = create_node_function('GeometryNodeCurveOfPoint')
# curve_primitive_bezier_segment = create_node_function('GeometryNodeCurvePrimitiveBezierSegment')
# curve_primitive_circle = create_node_function('GeometryNodeCurvePrimitiveCircle')
# curve_primitive_line = create_node_function('GeometryNodeCurvePrimitiveLine')
# curve_primitive_quadrilateral = create_node_function('GeometryNodeCurvePrimitiveQuadrilateral')
# curve_quadratic_bezier = create_node_function('GeometryNodeCurveQuadraticBezier')
# curve_set_handles = create_node_function('GeometryNodeCurveSetHandles')
# curve_spiral = create_node_function('GeometryNodeCurveSpiral')
# curve_spline_type = create_node_function('GeometryNodeCurveSplineType')
# curve_star = create_node_function('GeometryNodeCurveStar')
# curve_to_mesh = create_node_function('GeometryNodeCurveToMesh')
# curve_to_points = create_node_function('GeometryNodeCurveToPoints')
# deform_curves_on_surface = create_node_function('GeometryNodeDeformCurvesOnSurface')
# delete_geometry = create_node_function('GeometryNodeDeleteGeometry')
# distribute_points_in_volume = create_node_function('GeometryNodeDistributePointsInVolume')
# distribute_points_on_faces = create_node_function('GeometryNodeDistributePointsOnFaces')
# dual_mesh = create_node_function('GeometryNodeDualMesh')
# duplicate_elements = create_node_function('GeometryNodeDuplicateElements')
# edge_paths_to_curves = create_node_function('GeometryNodeEdgePathsToCurves')
# edge_paths_to_selection = create_node_function('GeometryNodeEdgePathsToSelection')
# edges_of_corner = create_node_function('GeometryNodeEdgesOfCorner')
# edges_of_vertex = create_node_function('GeometryNodeEdgesOfVertex')
# extrude_mesh = create_node_function('GeometryNodeExtrudeMesh')
# face_of_corner = create_node_function('GeometryNodeFaceOfCorner')
# field_at_index = create_node_function('GeometryNodeFieldAtIndex')
# field_on_domain = create_node_function('GeometryNodeFieldOnDomain')
# fill_curve = create_node_function('GeometryNodeFillCurve')
# fillet_curve = create_node_function('GeometryNodeFilletCurve')
# flip_faces = create_node_function('GeometryNodeFlipFaces')
# geometry_to_instance = create_node_function('GeometryNodeGeometryToInstance')
# group = create_node_function('GeometryNodeGroup')
# image_texture = create_node_function('GeometryNodeImageTexture')
# input_curve_handle_positions = create_node_function('GeometryNodeInputCurveHandlePositions')
# input_curve_tilt = create_node_function('GeometryNodeInputCurveTilt')
# input_id = create_node_function('GeometryNodeInputID')
# input_index = create_node_function('GeometryNodeInputIndex')
# input_instance_rotation = create_node_function('GeometryNodeInputInstanceRotation')
# input_instance_scale = create_node_function('GeometryNodeInputInstanceScale')
# input_material = create_node_function('GeometryNodeInputMaterial')
# input_material_index = create_node_function('GeometryNodeInputMaterialIndex')
# input_mesh_edge_angle = create_node_function('GeometryNodeInputMeshEdgeAngle')
# input_mesh_edge_neighbors = create_node_function('GeometryNodeInputMeshEdgeNeighbors')
# input_mesh_edge_vertices = create_node_function('GeometryNodeInputMeshEdgeVertices')
# input_mesh_face_area = create_node_function('GeometryNodeInputMeshFaceArea')
# input_mesh_face_is_planar = create_node_function('GeometryNodeInputMeshFaceIsPlanar')
# input_mesh_face_neighbors = create_node_function('GeometryNodeInputMeshFaceNeighbors')
# input_mesh_island = create_node_function('GeometryNodeInputMeshIsland')
# input_mesh_vertex_neighbors = create_node_function('GeometryNodeInputMeshVertexNeighbors')
# input_named_attribute = create_node_function('GeometryNodeInputNamedAttribute')
# input_normal = create_node_function('GeometryNodeInputNormal')
# input_position = create_node_function('GeometryNodeInputPosition')
# input_radius = create_node_function('GeometryNodeInputRadius')
# input_scene_time = create_node_function('GeometryNodeInputSceneTime')
# input_shade_smooth = create_node_function('GeometryNodeInputShadeSmooth')
# input_shortest_edge_paths = create_node_function('GeometryNodeInputShortestEdgePaths')
# input_spline_cyclic = create_node_function('GeometryNodeInputSplineCyclic')
# input_spline_resolution = create_node_function('GeometryNodeInputSplineResolution')
# input_tangent = create_node_function('GeometryNodeInputTangent')
# instance_on_points = create_node_function('GeometryNodeInstanceOnPoints')
# instances_to_points = create_node_function('GeometryNodeInstancesToPoints')
# is_viewport = create_node_function('GeometryNodeIsViewport')
# join_geometry = create_node_function('GeometryNodeJoinGeometry')
# material_selection = create_node_function('GeometryNodeMaterialSelection')
# merge_by_distance = create_node_function('GeometryNodeMergeByDistance')
# mesh_boolean = create_node_function('GeometryNodeMeshBoolean')
# mesh_circle = create_node_function('GeometryNodeMeshCircle')
# mesh_cone = create_node_function('GeometryNodeMeshCone')
# mesh_cube = create_node_function('GeometryNodeMeshCube')
# mesh_cylinder = create_node_function('GeometryNodeMeshCylinder')
# mesh_face_set_boundaries = create_node_function('GeometryNodeMeshFaceSetBoundaries')
# mesh_grid = create_node_function('GeometryNodeMeshGrid')
# mesh_ico_sphere = create_node_function('GeometryNodeMeshIcoSphere')
# mesh_line = create_node_function('GeometryNodeMeshLine')
# mesh_to_curve = create_node_function('GeometryNodeMeshToCurve')
# mesh_to_points = create_node_function('GeometryNodeMeshToPoints')
# mesh_to_volume = create_node_function('GeometryNodeMeshToVolume')
# mesh_uv_sphere = create_node_function('GeometryNodeMeshUVSphere')
# object_info = create_node_function('GeometryNodeObjectInfo')
# offset_corner_in_face = create_node_function('GeometryNodeOffsetCornerInFace')
# offset_point_in_curve = create_node_function('GeometryNodeOffsetPointInCurve')
# points = create_node_function('GeometryNodePoints')
# points_of_curve = create_node_function('GeometryNodePointsOfCurve')
# points_to_vertices = create_node_function('GeometryNodePointsToVertices')
# points_to_volume = create_node_function('GeometryNodePointsToVolume')
# proximity = create_node_function('GeometryNodeProximity')
# raycast = create_node_function('GeometryNodeRaycast')
# realize_instances = create_node_function('GeometryNodeRealizeInstances')
# remove_attribute = create_node_function('GeometryNodeRemoveAttribute')
# replace_material = create_node_function('GeometryNodeReplaceMaterial')
# resample_curve = create_node_function('GeometryNodeResampleCurve')
# reverse_curve = create_node_function('GeometryNodeReverseCurve')
# rotate_instances = create_node_function('GeometryNodeRotateInstances')
# sample_curve = create_node_function('GeometryNodeSampleCurve')
# sample_index = create_node_function('GeometryNodeSampleIndex')
# sample_nearest = create_node_function('GeometryNodeSampleNearest')
# sample_nearest_surface = create_node_function('GeometryNodeSampleNearestSurface')
# sample_uv_surface = create_node_function('GeometryNodeSampleUVSurface')
# scale_elements = create_node_function('GeometryNodeScaleElements')
# scale_instances = create_node_function('GeometryNodeScaleInstances')
# self_object = create_node_function('GeometryNodeSelfObject')
# separate_components = create_node_function('GeometryNodeSeparateComponents')
# separate_geometry = create_node_function('GeometryNodeSeparateGeometry')
# set_curve_handle_positions = create_node_function('GeometryNodeSetCurveHandlePositions')
# set_curve_normal = create_node_function('GeometryNodeSetCurveNormal')
# set_curve_radius = create_node_function('GeometryNodeSetCurveRadius')
# set_curve_tilt = create_node_function('GeometryNodeSetCurveTilt')
# set_id = create_node_function('GeometryNodeSetID')
# set_material = create_node_function('GeometryNodeSetMaterial')
# set_material_index = create_node_function('GeometryNodeSetMaterialIndex')
# set_point_radius = create_node_function('GeometryNodeSetPointRadius')
# set_position = create_node_function('GeometryNodeSetPosition')
# set_shade_smooth = create_node_function('GeometryNodeSetShadeSmooth')
# set_spline_cyclic = create_node_function('GeometryNodeSetSplineCyclic')
# set_spline_resolution = create_node_function('GeometryNodeSetSplineResolution')
# spline_length = create_node_function('GeometryNodeSplineLength')
# spline_parameter = create_node_function('GeometryNodeSplineParameter')
# split_edges = create_node_function('GeometryNodeSplitEdges')
# store_named_attribute = create_node_function('GeometryNodeStoreNamedAttribute')
# string_join = create_node_function('GeometryNodeStringJoin')
# string_to_curves = create_node_function('GeometryNodeStringToCurves')
# subdivide_curve = create_node_function('GeometryNodeSubdivideCurve')
# subdivide_mesh = create_node_function('GeometryNodeSubdivideMesh')
# subdivision_surface = create_node_function('GeometryNodeSubdivisionSurface')
# switch = create_node_function('GeometryNodeSwitch')
# transform = create_node_function('GeometryNodeTransform')
# translate_instances = create_node_function('GeometryNodeTranslateInstances')
# triangulate = create_node_function('GeometryNodeTriangulate')
# trim_curve = create_node_function('GeometryNodeTrimCurve')
# uv_pack_islands = create_node_function('GeometryNodeUVPackIslands')
# uv_unwrap = create_node_function('GeometryNodeUVUnwrap')
# vertex_of_corner = create_node_function('GeometryNodeVertexOfCorner')
# viewer = create_node_function('GeometryNodeViewer')
# volume_cube = create_node_function('GeometryNodeVolumeCube')
# volume_to_mesh = create_node_function('GeometryNodeVolumeToMesh')
# group_input = create_node_function('NodeGroupInput')
# group_output = create_node_function('NodeGroupOutput')
# reroute = create_node_function('NodeReroute')
# clamp = create_node_function('ShaderNodeClamp')
# combine_rgb = create_node_function('ShaderNodeCombineRGB')
# combine_xyz = create_node_function('ShaderNodeCombineXYZ')
# float_curve = create_node_function('ShaderNodeFloatCurve')
# map_range = create_node_function('ShaderNodeMapRange')
# math = create_node_function('ShaderNodeMath')
# mix = create_node_function('ShaderNodeMix')
# mix_rgb = create_node_function('ShaderNodeMixRGB')
# rgb_curve = create_node_function('ShaderNodeRGBCurve')
# separate_rgb = create_node_function('ShaderNodeSeparateRGB')
# separate_xyz = create_node_function('ShaderNodeSeparateXYZ')
# tex_brick = create_node_function('ShaderNodeTexBrick')
# tex_checker = create_node_function('ShaderNodeTexChecker')
# tex_gradient = create_node_function('ShaderNodeTexGradient')
# tex_magic = create_node_function('ShaderNodeTexMagic')
# tex_musgrave = create_node_function('ShaderNodeTexMusgrave')
# tex_noise = create_node_function('ShaderNodeTexNoise')
# tex_voronoi = create_node_function('ShaderNodeTexVoronoi')
# tex_wave = create_node_function('ShaderNodeTexWave')
# tex_white_noise = create_node_function('ShaderNodeTexWhiteNoise')
# val_to_rgb = create_node_function('ShaderNodeValToRGB')
# value = create_node_function('ShaderNodeValue')
# vector_curve = create_node_function('ShaderNodeVectorCurve')
# vector_math = create_node_function('ShaderNodeVectorMath')
# vector_rotate = create_node_function('ShaderNodeVectorRotate')

from nodes import *