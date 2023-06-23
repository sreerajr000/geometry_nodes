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


    return node

def create_group_socket(nodetree, node, data, inout='in'):

    def update_socket_info(socket, socket_info):
        dv_dict = {
            'NodeSocketBool': False,
            'NodeSocketString': '',
            'NodeSocketMaterial': None,
            'NodeSocketVector': (0, 0, 0),
            'NodeSocketInt': 0,
            'NodeSocketFloat': 0.0,
            'NodeSocketColor': (0, 0, 0, 0),
            'NodeSocketImage': None,
            'NodeSocketCollection': None,
            'NodeSocketTexture': None,
            'NodeSocketObject': None,
            'NodeSocketGeometry': None,
            'NodeSocketVectorEuler': (0, 0, 0)

        }
        socket_type = socket_info.get('type')
        socket.description = socket_info.get('description', '')
        socket.default_attribute_name = socket_info.get(
            'default_attribute_name', '')
        socket.hide_value = socket_info.get('hide_value', False)
        if socket_type != 'NodeSocketGeometry':
            socket.default_value = socket_info.get(
                'default_value', dv_dict[socket_type])

        if socket_type in ['NodeSocketVector', 'NodeSocketFloat', 'NodeSocketVectorEuler']:
            socket.min_value = socket_info.get('min_value', -inf)
            socket.max_value = socket_info.get('max_value', inf)
        elif socket_type == 'NodeSocketInt':
            socket.min_value = socket_info.get('min_value', -2147483648)
            socket.max_value = socket_info.get('max_value', 2147483647)

        # Update Attribute Domain for out
        if inout == 'out' and socket_type in ['NodeSocketVector', 'NodeSocketFloat', 'NodeSocketBool', 'NodeSocketInt', 'NodeSocketColor', 'NodeSocketVectorEuler']:
            socket.attribute_domain = socket_info.get(
                'attribute_domain', 'POINT')

    for socket_info in data:
        if inout == 'in':
            socket = nodetree.inputs.new(
                socket_info['type'], socket_info['name'])
        else:
            socket = nodetree.outputs.new(
                socket_info['type'], socket_info['name'])
        update_socket_info(socket, socket_info)



def create_gn(name, inputs, outputs):
    if name in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups[name])
    nodetree = bpy.data.node_groups.new(name, 'GeometryNodeTree')
    inps = nodetree.nodes.new('NodeGroupInput')
    outs = nodetree.nodes.new('NodeGroupOutput')

    create_group_socket(nodetree, inps, inputs, 'in')
    create_group_socket(nodetree, outs, outputs, 'out')
    return nodetree, inps, outs



def create_node_function(node_type):

    def create_node(**kwargs):
        # Get the active object
        obj = bpy.context.active_object

        # Ensure object has a geometry node tree
        if not obj.modifiers:
            mod = obj.modifiers.new(name="GeometryNodes", type='NODES')
            node_group = bpy.data.node_groups.new(
                name="NodeGroup", type='GeometryNodeTree')
            mod.node_group = node_group
        else:
            mod = next((m for m in obj.modifiers if m.type == 'NODES'), None)
            if not mod:
                mod = obj.modifiers.new(name="GeometryNodes", type='NODES')
                node_group = bpy.data.node_groups.new(
                    name="NodeGroup", type='GeometryNodeTree')
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
                        node_group.links.new(
                            new_node.inputs[input_name], source_node.outputs[source_socket_name])
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



def align_euler_to_vector(ng, rotation=[0.0, 0.0, 0.0], factor=1.0, vector=[0.0, 0.0, 1.0], axis='X', pivot_axis='AUTO'):

    node = ng.nodes.new("FunctionNodeAlignEulerToVector")
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"].default_value = rotation
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    node.axis = axis
    node.pivot_axis = pivot_axis


    return node

def boolean_math(ng, a=False, b=False, operation='AND'):

    node = ng.nodes.new("FunctionNodeBooleanMath")
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], a)
    else:
        node.inputs[0] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], b)
    else:
        node.inputs[1] = b
    node.operation = operation


    return node

def combine_color(ng, red=0.0, green=0.0, blue=0.0, alpha=1.0, mode='RGB'):

    node = ng.nodes.new("FunctionNodeCombineColor")
    if isinstance(red, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Red"], red)
    else:
        node.inputs["Red"].default_value = red
    if isinstance(green, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Green"], green)
    else:
        node.inputs["Green"].default_value = green
    if isinstance(blue, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Blue"], blue)
    else:
        node.inputs["Blue"].default_value = blue
    if isinstance(alpha, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Alpha"], alpha)
    else:
        node.inputs["Alpha"].default_value = alpha
    node.mode = mode


    return node

def compare_float(ng, a=0, b=0, c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='FLOAT'):

    node = ng.nodes.new("FunctionNodeCompare")
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], a)
    else:
        node.inputs[0] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], b)
    else:
        node.inputs[1] = b
    if isinstance(c, bpy.types.NodeSocket):
        ng.links.new(node.inputs["C"], c)
    else:
        node.inputs["C"].default_value = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"].default_value = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"].default_value = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type


    return node

def compare_int(ng, a=0, b=0, c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='INT'):

    node = ng.nodes.new("FunctionNodeCompare")
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], a)
    else:
        node.inputs[2] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], b)
    else:
        node.inputs[3] = b
    if isinstance(c, bpy.types.NodeSocket):
        ng.links.new(node.inputs["C"], c)
    else:
        node.inputs["C"].default_value = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"].default_value = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"].default_value = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type


    return node

def compare_vector(ng, a=(0, 0, 0), b=(0, 0, 0), c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='VECTOR'):

    node = ng.nodes.new("FunctionNodeCompare")
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], a)
    else:
        node.inputs[4] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[5], b)
    else:
        node.inputs[5] = b
    if isinstance(c, bpy.types.NodeSocket):
        ng.links.new(node.inputs["C"], c)
    else:
        node.inputs["C"].default_value = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"].default_value = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"].default_value = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type


    return node

def compare_string(ng, a='', b='', c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='STRING'):

    node = ng.nodes.new("FunctionNodeCompare")
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[6], a)
    else:
        node.inputs[6] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[7], b)
    else:
        node.inputs[7] = b
    if isinstance(c, bpy.types.NodeSocket):
        ng.links.new(node.inputs["C"], c)
    else:
        node.inputs["C"].default_value = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"].default_value = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"].default_value = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type


    return node

def compare_color(ng, a=(0, 0, 0, 0), b=(0, 0, 0, 0), c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='COLOR'):

    node = ng.nodes.new("FunctionNodeCompare")
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[6], a)
    else:
        node.inputs[6] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[7], b)
    else:
        node.inputs[7] = b
    if isinstance(c, bpy.types.NodeSocket):
        ng.links.new(node.inputs["C"], c)
    else:
        node.inputs["C"].default_value = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"].default_value = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"].default_value = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type


    return node

def float_to_int(ng, float=0.0, rounding_mode='ROUND'):

    node = ng.nodes.new("FunctionNodeFloatToInt")
    if isinstance(float, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Float"], float)
    else:
        node.inputs["Float"].default_value = float
    node.rounding_mode = rounding_mode


    return node

def input_bool(ng, boolean=False):

    node = ng.nodes.new("FunctionNodeInputBool")
    node.boolean = boolean


    return node

def input_color(ng, color=(0, 0, 0, 0)):

    node = ng.nodes.new("FunctionNodeInputColor")
    node.color = color


    return node

def input_int(ng, integer=0):

    node = ng.nodes.new("FunctionNodeInputInt")
    node.integer = integer


    return node

def input_special_characters(ng, ):

    node = ng.nodes.new("FunctionNodeInputSpecialCharacters")


    return node

def input_string(ng, string=''):

    node = ng.nodes.new("FunctionNodeInputString")
    node.string = string


    return node

def input_vector(ng, vector=(0.0000, 0.0000, 0.0000)):

    node = ng.nodes.new("FunctionNodeInputVector")
    node.vector = vector


    return node

def random_value_float(ng, min=(0, 0, 0), max=(1, 1, 1), probability=0.5, id=None, seed=None, data_type='FLOAT'):

    node = ng.nodes.new("FunctionNodeRandomValue")
    if isinstance(min, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], min)
    else:
        node.inputs[0] = min
    if isinstance(max, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], max)
    else:
        node.inputs[1] = max
    if isinstance(probability, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Probability"], probability)
    else:
        node.inputs["Probability"].default_value = probability
    if isinstance(id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["ID"], id)
    else:
        node.inputs["ID"].default_value = id
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"].default_value = seed
    node.data_type = data_type


    return node

def random_value_int(ng, min=(0, 0, 0), max=(1, 1, 1), probability=0.5, id=None, seed=None, data_type='INT'):

    node = ng.nodes.new("FunctionNodeRandomValue")
    if isinstance(min, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], min)
    else:
        node.inputs[2] = min
    if isinstance(max, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], max)
    else:
        node.inputs[3] = max
    if isinstance(probability, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Probability"], probability)
    else:
        node.inputs["Probability"].default_value = probability
    if isinstance(id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["ID"], id)
    else:
        node.inputs["ID"].default_value = id
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"].default_value = seed
    node.data_type = data_type


    return node

def random_value_vector(ng, min=(0, 0, 0), max=(1, 1, 1), probability=0.5, id=None, seed=None, data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("FunctionNodeRandomValue")
    if isinstance(min, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], min)
    else:
        node.inputs[4] = min
    if isinstance(max, bpy.types.NodeSocket):
        ng.links.new(node.inputs[5], max)
    else:
        node.inputs[5] = max
    if isinstance(probability, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Probability"], probability)
    else:
        node.inputs["Probability"].default_value = probability
    if isinstance(id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["ID"], id)
    else:
        node.inputs["ID"].default_value = id
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"].default_value = seed
    node.data_type = data_type


    return node

def replace_string(ng, string,  find=None, replace=None, ):

    node = ng.nodes.new("FunctionNodeReplaceString")
    if isinstance(string,  bpy.types.NodeSocket):
        ng.links.new(node.inputs["String"], string)
    else:
        node.inputs["String"].default_value = string
    if isinstance(find, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Find"], find)
    else:
        node.inputs["Find"].default_value = find
    if isinstance(replace, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Replace"], replace)
    else:
        node.inputs["Replace"].default_value = replace


    return node

def rotate_euler(ng, rotation=[0.0, 0.0, 0.0], rotate_by=[0.0, 0.0, 0.0], axis=[0.0, 0.0, 1.0], angle=0.0, space='OBJECT'):

    node = ng.nodes.new("FunctionNodeRotateEuler")
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"].default_value = rotation
    if isinstance(rotate_by, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotate By"], rotate_by)
    else:
        node.inputs["Rotate By"].default_value = rotate_by
    if isinstance(axis, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Axis"], axis)
    else:
        node.inputs["Axis"].default_value = axis
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"].default_value = angle
    node.space = space


    return node

def separate_color(ng, color=None, mode='RGB'):

    node = ng.nodes.new("FunctionNodeSeparateColor")
    if isinstance(color, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color"], color)
    else:
        node.inputs["Color"].default_value = color
    node.mode = mode


    return node

def slice_string(ng, string,  position=None, length=None, ):

    node = ng.nodes.new("FunctionNodeSliceString")
    if isinstance(string,  bpy.types.NodeSocket):
        ng.links.new(node.inputs["String"], string)
    else:
        node.inputs["String"].default_value = string
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"].default_value = position
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length


    return node

def string_length(ng, string,):

    node = ng.nodes.new("FunctionNodeStringLength")
    if isinstance(string,  bpy.types.NodeSocket):
        ng.links.new(node.inputs["String"], string)
    else:
        node.inputs["String"].default_value = string


    return node

def value_to_string(ng, value=0.0, decimals=None, ):

    node = ng.nodes.new("FunctionNodeValueToString")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"].default_value = value
    if isinstance(decimals, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Decimals"], decimals)
    else:
        node.inputs["Decimals"].default_value = decimals


    return node

def accumulate_field_float(ng, value=[1.0, 1.0, 1.0], group_id=None, domain='POINT', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeAccumulateField")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Group ID"], group_id)
    else:
        node.inputs["Group ID"].default_value = group_id
    node.domain = domain
    node.data_type = data_type


    return node

def accumulate_field_int(ng, value=[1.0, 1.0, 1.0], group_id=None, domain='POINT', data_type='INT'):

    node = ng.nodes.new("GeometryNodeAccumulateField")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Group ID"], group_id)
    else:
        node.inputs["Group ID"].default_value = group_id
    node.domain = domain
    node.data_type = data_type


    return node

def accumulate_field_vector(ng, value=[1.0, 1.0, 1.0], group_id=None, domain='POINT', data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeAccumulateField")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Group ID"], group_id)
    else:
        node.inputs["Group ID"].default_value = group_id
    node.domain = domain
    node.data_type = data_type


    return node

def attribute_domain_size(ng, geometry=None, component='MESH'):

    node = ng.nodes.new("GeometryNodeAttributeDomainSize")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    node.component = component


    return node

def attribute_statistic_float(ng, geometry=None, selection=None, attribute=0.0, domain='POINT', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeAttributeStatistic")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], attribute)
    else:
        node.inputs[0] = attribute

    node.domain = domain
    node.data_type = data_type


    return node

def attribute_statistic_vector(ng, geometry=None, selection=None, attribute=0.0, domain='POINT', data_type='FLOAT_VECTOR'):

    node = ng.nodes.new("GeometryNodeAttributeStatistic")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], attribute)
    else:
        node.inputs[1] = attribute

    node.domain = domain
    node.data_type = data_type


    return node

def blur_attribute_color(ng, value=0.0, iterations=None, weight=1.0, data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeBlurAttribute")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value

    if isinstance(iterations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Iterations"], iterations)
    else:
        node.inputs["Iterations"].default_value = iterations
    if isinstance(weight, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weight"], weight)
    else:
        node.inputs["Weight"].default_value = weight
    node.data_type = data_type


    return node

def blur_attribute_float(ng, value=0.0, iterations=None, weight=1.0, data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeBlurAttribute")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value

    if isinstance(iterations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Iterations"], iterations)
    else:
        node.inputs["Iterations"].default_value = iterations
    if isinstance(weight, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weight"], weight)
    else:
        node.inputs["Weight"].default_value = weight
    node.data_type = data_type


    return node

def blur_attribute_int(ng, value=0.0, iterations=None, weight=1.0, data_type='INT'):

    node = ng.nodes.new("GeometryNodeBlurAttribute")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value

    if isinstance(iterations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Iterations"], iterations)
    else:
        node.inputs["Iterations"].default_value = iterations
    if isinstance(weight, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weight"], weight)
    else:
        node.inputs["Weight"].default_value = weight
    node.data_type = data_type


    return node

def blur_attribute_vector(ng, value=0.0, iterations=None, weight=1.0, data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeBlurAttribute")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value

    if isinstance(iterations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Iterations"], iterations)
    else:
        node.inputs["Iterations"].default_value = iterations
    if isinstance(weight, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weight"], weight)
    else:
        node.inputs["Weight"].default_value = weight
    node.data_type = data_type


    return node

def bound_box(ng, geometry=None, ):

    node = ng.nodes.new("GeometryNodeBoundBox")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry


    return node

def capture_attribute_float(ng, geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    node.domain = domain
    node.data_type = data_type


    return node

def capture_attribute_int(ng, geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='INT'):

    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    node.domain = domain
    node.data_type = data_type


    return node

def capture_attribute_vector(ng, geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    node.domain = domain
    node.data_type = data_type


    return node

def capture_attribute_color(ng, geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    node.domain = domain
    node.data_type = data_type


    return node

def capture_attribute_boolean(ng, geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    node.domain = domain
    node.data_type = data_type


    return node

def collection_info(ng, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):

    node = ng.nodes.new("GeometryNodeCollectionInfo")
    if isinstance(collection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Collection"], collection)
    else:
        node.inputs["Collection"].default_value = collection
    if isinstance(separate_children, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Separate Children"], separate_children)
    else:
        node.inputs["Separate Children"].default_value = separate_children
    if isinstance(reset_children, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Reset Children"], reset_children)
    else:
        node.inputs["Reset Children"].default_value = reset_children
    node.transform_space = transform_space


    return node

def convex_hull(ng, geometry=None, ):

    node = ng.nodes.new("GeometryNodeConvexHull")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry


    return node

def corners_of_face(ng, face_index=None, weights=0.0, sort_index=None, ):

    node = ng.nodes.new("GeometryNodeCornersOfFace")
    if isinstance(face_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Face Index"], face_index)
    else:
        node.inputs["Face Index"].default_value = face_index
    if isinstance(weights, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weights"], weights)
    else:
        node.inputs["Weights"].default_value = weights
    if isinstance(sort_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sort Index"], sort_index)
    else:
        node.inputs["Sort Index"].default_value = sort_index


    return node

def corners_of_vertex(ng, vertex_index=None, weights=0.0, sort_index=None, ):

    node = ng.nodes.new("GeometryNodeCornersOfVertex")
    if isinstance(vertex_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertex Index"], vertex_index)
    else:
        node.inputs["Vertex Index"].default_value = vertex_index
    if isinstance(weights, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weights"], weights)
    else:
        node.inputs["Weights"].default_value = weights
    if isinstance(sort_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sort Index"], sort_index)
    else:
        node.inputs["Sort Index"].default_value = sort_index


    return node

def curve_arc(ng, resolution=None, start=[-1.0, 0.0, 0.0], middle=[0.0, 2.0, 0.0], end=[1.0, 0.0, 0.0], radius=1.0, start_angle=0.0, sweep_angle=5.497786998748779, offset_angle=0.0, connect_center=None, invert_arc=None, mode='RADIUS'):

    node = ng.nodes.new("GeometryNodeCurveArc")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"].default_value = resolution
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start"], start)
    else:
        node.inputs["Start"].default_value = start
    if isinstance(middle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Middle"], middle)
    else:
        node.inputs["Middle"].default_value = middle
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End"], end)
    else:
        node.inputs["End"].default_value = end
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius
    if isinstance(start_angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Angle"], start_angle)
    else:
        node.inputs["Start Angle"].default_value = start_angle
    if isinstance(sweep_angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sweep Angle"], sweep_angle)
    else:
        node.inputs["Sweep Angle"].default_value = sweep_angle
    if isinstance(offset_angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset Angle"], offset_angle)
    else:
        node.inputs["Offset Angle"].default_value = offset_angle
    if isinstance(connect_center, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Connect Center"], connect_center)
    else:
        node.inputs["Connect Center"].default_value = connect_center
    if isinstance(invert_arc, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Invert Arc"], invert_arc)
    else:
        node.inputs["Invert Arc"].default_value = invert_arc
    node.mode = mode


    return node

def curve_endpoint_selection(ng, start_size=None, end_size=None, ):

    node = ng.nodes.new("GeometryNodeCurveEndpointSelection")
    if isinstance(start_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Size"], start_size)
    else:
        node.inputs["Start Size"].default_value = start_size
    if isinstance(end_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End Size"], end_size)
    else:
        node.inputs["End Size"].default_value = end_size


    return node

def curve_handle_type_selection(ng, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

    node = ng.nodes.new("GeometryNodeCurveHandleTypeSelection")
    node.handle_type = handle_type
    node.mode = mode


    return node

def curve_length(ng, curve=None, ):

    node = ng.nodes.new("GeometryNodeCurveLength")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve


    return node

def curve_of_point(ng, point_index=None, ):

    node = ng.nodes.new("GeometryNodeCurveOfPoint")
    if isinstance(point_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point Index"], point_index)
    else:
        node.inputs["Point Index"].default_value = point_index


    return node

def curve_primitive_bezier_segment(ng, resolution=None, start=[-1.0, 0.0, 0.0], start_handle=[-0.5, 0.5, 0.0], end_handle=[0.0, 0.0, 0.0], end=[1.0, 0.0, 0.0], mode='POSITION'):

    node = ng.nodes.new("GeometryNodeCurvePrimitiveBezierSegment")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"].default_value = resolution
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start"], start)
    else:
        node.inputs["Start"].default_value = start
    if isinstance(start_handle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Handle"], start_handle)
    else:
        node.inputs["Start Handle"].default_value = start_handle
    if isinstance(end_handle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End Handle"], end_handle)
    else:
        node.inputs["End Handle"].default_value = end_handle
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End"], end)
    else:
        node.inputs["End"].default_value = end
    node.mode = mode


    return node

def curve_primitive_circle(ng, resolution=None, point_1=[-1.0, 0.0, 0.0], point_2=[0.0, 1.0, 0.0], point_3=[1.0, 0.0, 0.0], radius=1.0, mode='RADIUS'):

    node = ng.nodes.new("GeometryNodeCurvePrimitiveCircle")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"].default_value = resolution
    if isinstance(point_1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 1"], point_1)
    else:
        node.inputs["Point 1"].default_value = point_1
    if isinstance(point_2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 2"], point_2)
    else:
        node.inputs["Point 2"].default_value = point_2
    if isinstance(point_3, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 3"], point_3)
    else:
        node.inputs["Point 3"].default_value = point_3
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius
    node.mode = mode


    return node

def curve_primitive_line(ng, start=[0.0, 0.0, 0.0], end=[0.0, 0.0, 1.0], direction=[0.0, 0.0, 1.0], length=1.0, mode='POINTS'):

    node = ng.nodes.new("GeometryNodeCurvePrimitiveLine")
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start"], start)
    else:
        node.inputs["Start"].default_value = start
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End"], end)
    else:
        node.inputs["End"].default_value = end
    if isinstance(direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Direction"], direction)
    else:
        node.inputs["Direction"].default_value = direction
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length
    node.mode = mode


    return node

def curve_primitive_quadrilateral(ng, width=2.0, height=2.0, bottom_width=4.0, top_width=2.0, offset=1.0, bottom_height=3.0, top_height=1.0, point_1=[-1.0, -1.0, 0.0], point_2=[1.0, -1.0, 0.0], point_3=[1.0, 1.0, 0.0], point_4=[-1.0, 1.0, 0.0], mode='RECTANGLE'):

    node = ng.nodes.new("GeometryNodeCurvePrimitiveQuadrilateral")
    if isinstance(width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Width"], width)
    else:
        node.inputs["Width"].default_value = width
    if isinstance(height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Height"], height)
    else:
        node.inputs["Height"].default_value = height
    if isinstance(bottom_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Bottom Width"], bottom_width)
    else:
        node.inputs["Bottom Width"].default_value = bottom_width
    if isinstance(top_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Top Width"], top_width)
    else:
        node.inputs["Top Width"].default_value = top_width
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"].default_value = offset
    if isinstance(bottom_height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Bottom Height"], bottom_height)
    else:
        node.inputs["Bottom Height"].default_value = bottom_height
    if isinstance(top_height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Top Height"], top_height)
    else:
        node.inputs["Top Height"].default_value = top_height
    if isinstance(point_1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 1"], point_1)
    else:
        node.inputs["Point 1"].default_value = point_1
    if isinstance(point_2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 2"], point_2)
    else:
        node.inputs["Point 2"].default_value = point_2
    if isinstance(point_3, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 3"], point_3)
    else:
        node.inputs["Point 3"].default_value = point_3
    if isinstance(point_4, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 4"], point_4)
    else:
        node.inputs["Point 4"].default_value = point_4
    node.mode = mode


    return node

def curve_quadratic_bezier(ng, resolution=None, start=[-1.0, 0.0, 0.0], middle=[0.0, 2.0, 0.0], end=[1.0, 0.0, 0.0], ):

    node = ng.nodes.new("GeometryNodeCurveQuadraticBezier")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"].default_value = resolution
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start"], start)
    else:
        node.inputs["Start"].default_value = start
    if isinstance(middle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Middle"], middle)
    else:
        node.inputs["Middle"].default_value = middle
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End"], end)
    else:
        node.inputs["End"].default_value = end


    return node

def curve_set_handles(ng, curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

    node = ng.nodes.new("GeometryNodeCurveSetHandles")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    node.handle_type = handle_type
    node.mode = mode


    return node

def curve_spiral(ng, resolution=None, rotations=2.0, start_radius=1.0, end_radius=2.0, height=2.0, reverse=None, ):

    node = ng.nodes.new("GeometryNodeCurveSpiral")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"].default_value = resolution
    if isinstance(rotations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotations"], rotations)
    else:
        node.inputs["Rotations"].default_value = rotations
    if isinstance(start_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Radius"], start_radius)
    else:
        node.inputs["Start Radius"].default_value = start_radius
    if isinstance(end_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End Radius"], end_radius)
    else:
        node.inputs["End Radius"].default_value = end_radius
    if isinstance(height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Height"], height)
    else:
        node.inputs["Height"].default_value = height
    if isinstance(reverse, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Reverse"], reverse)
    else:
        node.inputs["Reverse"].default_value = reverse


    return node

def curve_spline_type(ng, curve=None, selection=None, spline_type='POLY'):

    node = ng.nodes.new("GeometryNodeCurveSplineType")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    node.spline_type = spline_type


    return node

def curve_star(ng, points=None, inner_radius=1.0, outer_radius=2.0, twist=0.0, ):

    node = ng.nodes.new("GeometryNodeCurveStar")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"].default_value = points
    if isinstance(inner_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Inner Radius"], inner_radius)
    else:
        node.inputs["Inner Radius"].default_value = inner_radius
    if isinstance(outer_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Outer Radius"], outer_radius)
    else:
        node.inputs["Outer Radius"].default_value = outer_radius
    if isinstance(twist, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Twist"], twist)
    else:
        node.inputs["Twist"].default_value = twist


    return node

def curve_to_mesh(ng, curve=None, profile_curve=None, fill_caps=None, ):

    node = ng.nodes.new("GeometryNodeCurveToMesh")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(profile_curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Profile Curve"], profile_curve)
    else:
        node.inputs["Profile Curve"].default_value = profile_curve
    if isinstance(fill_caps, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Caps"], fill_caps)
    else:
        node.inputs["Fill Caps"].default_value = fill_caps


    return node

def curve_to_points(ng, curve=None, count=None, length=0.10000000149011612, mode='COUNT'):

    node = ng.nodes.new("GeometryNodeCurveToPoints")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"].default_value = count
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length
    node.mode = mode


    return node

def deform_curves_on_surface(ng, curves=None, ):

    node = ng.nodes.new("GeometryNodeDeformCurvesOnSurface")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"].default_value = curves


    return node

def delete_geometry(ng, geometry=None, selection=None, mode='ALL', domain='POINT'):

    node = ng.nodes.new("GeometryNodeDeleteGeometry")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    node.mode = mode
    node.domain = domain


    return node

def distribute_points_in_volume(ng, volume=None, density=1.0, seed=None, spacing=[0.30000001192092896, 0.30000001192092896, 0.30000001192092896], threshold=0.10000000149011612, mode='DENSITY_RANDOM'):

    node = ng.nodes.new("GeometryNodeDistributePointsInVolume")
    if isinstance(volume, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Volume"], volume)
    else:
        node.inputs["Volume"].default_value = volume
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"].default_value = density
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"].default_value = seed
    if isinstance(spacing,  bpy.types.NodeSocket):
        ng.links.new(node.inputs["Spacing"], spacing)
    else:
        node.inputs["Spacing"].default_value = spacing
    if isinstance(threshold, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Threshold"], threshold)
    else:
        node.inputs["Threshold"].default_value = threshold
    node.mode = mode


    return node

def distribute_points_on_faces(ng, mesh=None, selection=None, distance_min=0.0, density_max=10.0, density=10.0, density_factor=1.0, seed=None, use_legacy_normal=False, distribute_method='RANDOM'):

    node = ng.nodes.new("GeometryNodeDistributePointsOnFaces")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(distance_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distance Min"], distance_min)
    else:
        node.inputs["Distance Min"].default_value = distance_min
    if isinstance(density_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density Max"], density_max)
    else:
        node.inputs["Density Max"].default_value = density_max
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"].default_value = density
    if isinstance(density_factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density Factor"], density_factor)
    else:
        node.inputs["Density Factor"].default_value = density_factor
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"].default_value = seed
    node.use_legacy_normal = use_legacy_normal
    node.distribute_method = distribute_method


    return node

def dual_mesh(ng, mesh=None, keep_boundaries=None, ):

    node = ng.nodes.new("GeometryNodeDualMesh")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(keep_boundaries, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Keep Boundaries"], keep_boundaries)
    else:
        node.inputs["Keep Boundaries"].default_value = keep_boundaries


    return node

def duplicate_elements(ng, geometry=None, selection=None, amount=None, domain='POINT'):

    node = ng.nodes.new("GeometryNodeDuplicateElements")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(amount, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Amount"], amount)
    else:
        node.inputs["Amount"].default_value = amount
    node.domain = domain


    return node

def edge_paths_to_curves(ng, mesh=None, start_vertices=None, next_vertex_index=None, ):

    node = ng.nodes.new("GeometryNodeEdgePathsToCurves")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(start_vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Vertices"], start_vertices)
    else:
        node.inputs["Start Vertices"].default_value = start_vertices
    if isinstance(next_vertex_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Next Vertex Index"], next_vertex_index)
    else:
        node.inputs["Next Vertex Index"].default_value = next_vertex_index


    return node

def edge_paths_to_selection(ng, start_vertices=None, next_vertex_index=None, ):

    node = ng.nodes.new("GeometryNodeEdgePathsToSelection")
    if isinstance(start_vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Vertices"], start_vertices)
    else:
        node.inputs["Start Vertices"].default_value = start_vertices
    if isinstance(next_vertex_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Next Vertex Index"], next_vertex_index)
    else:
        node.inputs["Next Vertex Index"].default_value = next_vertex_index


    return node

def edges_of_corner(ng, corner_index=None, ):

    node = ng.nodes.new("GeometryNodeEdgesOfCorner")
    if isinstance(corner_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Corner Index"], corner_index)
    else:
        node.inputs["Corner Index"].default_value = corner_index


    return node

def edges_of_vertex(ng, vertex_index=None, weights=0.0, sort_index=None, ):

    node = ng.nodes.new("GeometryNodeEdgesOfVertex")
    if isinstance(vertex_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertex Index"], vertex_index)
    else:
        node.inputs["Vertex Index"].default_value = vertex_index
    if isinstance(weights, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weights"], weights)
    else:
        node.inputs["Weights"].default_value = weights
    if isinstance(sort_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sort Index"], sort_index)
    else:
        node.inputs["Sort Index"].default_value = sort_index


    return node

def edges_to_face_groups(ng, boundary_edges=None, ):

    node = ng.nodes.new("GeometryNodeEdgesToFaceGroups")
    if isinstance(boundary_edges, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Boundary Edges"], boundary_edges)
    else:
        node.inputs["Boundary Edges"].default_value = boundary_edges


    return node

def extrude_mesh(ng, mesh=None, selection=None, offset=[0.0, 0.0, 0.0], offset_scale=1.0, individual=None, mode='FACES'):

    node = ng.nodes.new("GeometryNodeExtrudeMesh")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"].default_value = offset
    if isinstance(offset_scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset Scale"], offset_scale)
    else:
        node.inputs["Offset Scale"].default_value = offset_scale
    if isinstance(individual, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Individual"], individual)
    else:
        node.inputs["Individual"].default_value = individual
    node.mode = mode


    return node

def face_of_corner(ng, corner_index=None, ):

    node = ng.nodes.new("GeometryNodeFaceOfCorner")
    if isinstance(corner_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Corner Index"], corner_index)
    else:
        node.inputs["Corner Index"].default_value = corner_index


    return node

def field_at_index_float(ng, index=None, value=0.0, domain='POINT', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_at_index_int(ng, index=None, value=0.0, domain='POINT', data_type='INT'):

    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_at_index_vector(ng, index=None, value=0.0, domain='POINT', data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_at_index_color(ng, index=None, value=0.0, domain='POINT', data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_at_index_boolean(ng, index=None, value=0.0, domain='POINT', data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_on_domain_float(ng, value=0.0, domain='POINT', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_on_domain_int(ng, value=0.0, domain='POINT', data_type='INT'):

    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_on_domain_vector(ng, value=0.0, domain='POINT', data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_on_domain_color(ng, value=0.0, domain='POINT', data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    node.domain = domain
    node.data_type = data_type


    return node

def field_on_domain_boolean(ng, value=0.0, domain='POINT', data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    node.domain = domain
    node.data_type = data_type


    return node

def fill_curve(ng, curve=None, mode='TRIANGLES'):

    node = ng.nodes.new("GeometryNodeFillCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    node.mode = mode


    return node

def fillet_curve(ng, curve=None, count=None, radius=0.25, limit_radius=None, mode='BEZIER'):

    node = ng.nodes.new("GeometryNodeFilletCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"].default_value = count
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius
    if isinstance(limit_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Limit Radius"], limit_radius)
    else:
        node.inputs["Limit Radius"].default_value = limit_radius
    node.mode = mode


    return node

def flip_faces(ng, mesh=None, selection=None, ):

    node = ng.nodes.new("GeometryNodeFlipFaces")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection


    return node

def geometry_to_instance(ng, geometry=None, ):

    node = ng.nodes.new("GeometryNodeGeometryToInstance")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry


    return node

def group(ng, node_tree=None):

    node = ng.nodes.new("GeometryNodeGroup")
    node.node_tree = node_tree


    return node

def image_info(ng, image=None, frame=None, ):

    node = ng.nodes.new("GeometryNodeImageInfo")
    if isinstance(image, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Image"], image)
    else:
        node.inputs["Image"].default_value = image
    if isinstance(frame, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Frame"], frame)
    else:
        node.inputs["Frame"].default_value = frame


    return node

def image_texture(ng, image=None, vector=[0.0, 0.0, 0.0], frame=None, interpolation='Linear', extension='REPEAT'):

    node = ng.nodes.new("GeometryNodeImageTexture")
    if isinstance(image, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Image"], image)
    else:
        node.inputs["Image"].default_value = image
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(frame, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Frame"], frame)
    else:
        node.inputs["Frame"].default_value = frame
    node.interpolation = interpolation
    node.extension = extension


    return node

def input_curve_handle_positions(ng, relative=None, ):

    node = ng.nodes.new("GeometryNodeInputCurveHandlePositions")
    if isinstance(relative, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Relative"], relative)
    else:
        node.inputs["Relative"].default_value = relative


    return node

def input_curve_tilt(ng, ):

    node = ng.nodes.new("GeometryNodeInputCurveTilt")


    return node

def input_id(ng, ):

    node = ng.nodes.new("GeometryNodeInputID")


    return node

def input_image(ng, image=None):

    node = ng.nodes.new("GeometryNodeInputImage")
    node.image = image


    return node

def input_index(ng, ):

    node = ng.nodes.new("GeometryNodeInputIndex")


    return node

def input_instance_rotation(ng, ):

    node = ng.nodes.new("GeometryNodeInputInstanceRotation")


    return node

def input_instance_scale(ng, ):

    node = ng.nodes.new("GeometryNodeInputInstanceScale")


    return node

def input_material(ng, material=None):

    node = ng.nodes.new("GeometryNodeInputMaterial")
    node.material = material


    return node

def input_material_index(ng, ):

    node = ng.nodes.new("GeometryNodeInputMaterialIndex")


    return node

def input_mesh_edge_angle(ng, ):

    node = ng.nodes.new("GeometryNodeInputMeshEdgeAngle")


    return node

def input_mesh_edge_neighbors(ng, ):

    node = ng.nodes.new("GeometryNodeInputMeshEdgeNeighbors")


    return node

def input_mesh_edge_vertices(ng, ):

    node = ng.nodes.new("GeometryNodeInputMeshEdgeVertices")


    return node

def input_mesh_face_area(ng, ):

    node = ng.nodes.new("GeometryNodeInputMeshFaceArea")


    return node

def input_mesh_face_is_planar(ng, threshold=0.009999999776482582, ):

    node = ng.nodes.new("GeometryNodeInputMeshFaceIsPlanar")
    if isinstance(threshold, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Threshold"], threshold)
    else:
        node.inputs["Threshold"].default_value = threshold


    return node

def input_mesh_face_neighbors(ng, ):

    node = ng.nodes.new("GeometryNodeInputMeshFaceNeighbors")


    return node

def input_mesh_island(ng, ):

    node = ng.nodes.new("GeometryNodeInputMeshIsland")


    return node

def input_mesh_vertex_neighbors(ng, ):

    node = ng.nodes.new("GeometryNodeInputMeshVertexNeighbors")


    return node

def input_named_attribute(ng, name=None, data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeInputNamedAttribute")
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"].default_value = name
    node.data_type = data_type


    return node

def input_normal(ng, ):

    node = ng.nodes.new("GeometryNodeInputNormal")


    return node

def input_position(ng, ):

    node = ng.nodes.new("GeometryNodeInputPosition")


    return node

def input_radius(ng, ):

    node = ng.nodes.new("GeometryNodeInputRadius")


    return node

def input_scene_time(ng, ):

    node = ng.nodes.new("GeometryNodeInputSceneTime")


    return node

def input_shade_smooth(ng, ):

    node = ng.nodes.new("GeometryNodeInputShadeSmooth")


    return node

def input_shortest_edge_paths(ng, end_vertex=None, edge_cost=1.0, ):

    node = ng.nodes.new("GeometryNodeInputShortestEdgePaths")
    if isinstance(end_vertex, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End Vertex"], end_vertex)
    else:
        node.inputs["End Vertex"].default_value = end_vertex
    if isinstance(edge_cost, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Edge Cost"], edge_cost)
    else:
        node.inputs["Edge Cost"].default_value = edge_cost


    return node

def input_spline_cyclic(ng, ):

    node = ng.nodes.new("GeometryNodeInputSplineCyclic")


    return node

def input_spline_resolution(ng, ):

    node = ng.nodes.new("GeometryNodeInputSplineResolution")


    return node

def input_tangent(ng, ):

    node = ng.nodes.new("GeometryNodeInputTangent")


    return node

def instance_on_points(ng, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=[0.0, 0.0, 0.0], scale=[1.0, 1.0, 1.0], ):

    node = ng.nodes.new("GeometryNodeInstanceOnPoints")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"].default_value = points
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(instance, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instance"], instance)
    else:
        node.inputs["Instance"].default_value = instance
    if isinstance(pick_instance, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Pick Instance"], pick_instance)
    else:
        node.inputs["Pick Instance"].default_value = pick_instance
    if isinstance(instance_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instance Index"], instance_index)
    else:
        node.inputs["Instance Index"].default_value = instance_index
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"].default_value = rotation
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale


    return node

def instances_to_points(ng, instances=None, selection=None, position=[0.0, 0.0, 0.0], radius=0.05000000074505806, ):

    node = ng.nodes.new("GeometryNodeInstancesToPoints")
    if isinstance(instances, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instances"], instances)
    else:
        node.inputs["Instances"].default_value = instances
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"].default_value = position
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius


    return node

def interpolate_curves(ng, guide_curves=None, guide_up=[0.0, 0.0, 0.0], guide_group_id=None, points=None, point_up=[0.0, 0.0, 0.0], point_group_id=None, max_neighbors=None, ):

    node = ng.nodes.new("GeometryNodeInterpolateCurves")
    if isinstance(guide_curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Guide Curves"], guide_curves)
    else:
        node.inputs["Guide Curves"].default_value = guide_curves
    if isinstance(guide_up, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Guide Up"], guide_up)
    else:
        node.inputs["Guide Up"].default_value = guide_up
    if isinstance(guide_group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Guide Group ID"], guide_group_id)
    else:
        node.inputs["Guide Group ID"].default_value = guide_group_id
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"].default_value = points
    if isinstance(point_up, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point Up"], point_up)
    else:
        node.inputs["Point Up"].default_value = point_up
    if isinstance(point_group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point Group ID"], point_group_id)
    else:
        node.inputs["Point Group ID"].default_value = point_group_id
    if isinstance(max_neighbors, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Max Neighbors"], max_neighbors)
    else:
        node.inputs["Max Neighbors"].default_value = max_neighbors


    return node

def is_viewport(ng, ):

    node = ng.nodes.new("GeometryNodeIsViewport")


    return node

def join_geometry(ng, geometry=None, ):

    node = ng.nodes.new("GeometryNodeJoinGeometry")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry


    return node

def material_selection(ng, material=None, ):

    node = ng.nodes.new("GeometryNodeMaterialSelection")
    if isinstance(material, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Material"], material)
    else:
        node.inputs["Material"].default_value = material


    return node

def merge_by_distance(ng, geometry=None, selection=None, distance=0.0010000000474974513, mode='ALL'):

    node = ng.nodes.new("GeometryNodeMergeByDistance")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(distance, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distance"], distance)
    else:
        node.inputs["Distance"].default_value = distance
    node.mode = mode


    return node

def mesh_boolean(ng, mesh_1=None, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE'):

    node = ng.nodes.new("GeometryNodeMeshBoolean")
    if isinstance(mesh_1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh 1"], mesh_1)
    else:
        node.inputs["Mesh 1"].default_value = mesh_1
    if isinstance(mesh_2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh 2"], mesh_2)
    else:
        node.inputs["Mesh 2"].default_value = mesh_2
    if isinstance(self_intersection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Self Intersection"], self_intersection)
    else:
        node.inputs["Self Intersection"].default_value = self_intersection
    if isinstance(hole_tolerant, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Hole Tolerant"], hole_tolerant)
    else:
        node.inputs["Hole Tolerant"].default_value = hole_tolerant
    node.operation = operation


    return node

def mesh_circle(ng, vertices=None, radius=1.0, fill_type='NONE'):

    node = ng.nodes.new("GeometryNodeMeshCircle")
    if isinstance(vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices"], vertices)
    else:
        node.inputs["Vertices"].default_value = vertices
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius
    node.fill_type = fill_type


    return node

def mesh_cone(ng, vertices=None, side_segments=None, fill_segments=None, radius_top=0.0, radius_bottom=1.0, depth=2.0, fill_type='NGON'):

    node = ng.nodes.new("GeometryNodeMeshCone")
    if isinstance(vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices"], vertices)
    else:
        node.inputs["Vertices"].default_value = vertices
    if isinstance(side_segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Side Segments"], side_segments)
    else:
        node.inputs["Side Segments"].default_value = side_segments
    if isinstance(fill_segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Segments"], fill_segments)
    else:
        node.inputs["Fill Segments"].default_value = fill_segments
    if isinstance(radius_top, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius Top"], radius_top)
    else:
        node.inputs["Radius Top"].default_value = radius_top
    if isinstance(radius_bottom, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius Bottom"], radius_bottom)
    else:
        node.inputs["Radius Bottom"].default_value = radius_bottom
    if isinstance(depth, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Depth"], depth)
    else:
        node.inputs["Depth"].default_value = depth
    node.fill_type = fill_type


    return node

def mesh_cube(ng, size=[1.0, 1.0, 1.0], vertices_x=2, vertices_y=2, vertices_z=2, ):
    node = ng.nodes.new("GeometryNodeMeshCube")
    if isinstance(size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Size"], size)
    else:
        node.inputs["Size"].default_value = size
    if isinstance(vertices_x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices X"], vertices_x)
    else:
        node.inputs["Vertices X"].default_value = vertices_x
    if isinstance(vertices_y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices Y"], vertices_y)
    else:
        node.inputs["Vertices Y"].default_value = vertices_y
    if isinstance(vertices_z, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices Z"], vertices_z)
    else:
        node.inputs["Vertices Z"].default_value = vertices_z


    return node

def mesh_cylinder(ng, vertices=None, side_segments=None, fill_segments=None, radius=1.0, depth=2.0, fill_type='NGON'):

    node = ng.nodes.new("GeometryNodeMeshCylinder")
    if isinstance(vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices"], vertices)
    else:
        node.inputs["Vertices"].default_value = vertices
    if isinstance(side_segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Side Segments"], side_segments)
    else:
        node.inputs["Side Segments"].default_value = side_segments
    if isinstance(fill_segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Segments"], fill_segments)
    else:
        node.inputs["Fill Segments"].default_value = fill_segments
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius
    if isinstance(depth, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Depth"], depth)
    else:
        node.inputs["Depth"].default_value = depth
    node.fill_type = fill_type


    return node

def mesh_face_set_boundaries(ng, face_group_id=None, ):

    node = ng.nodes.new("GeometryNodeMeshFaceSetBoundaries")
    if isinstance(face_group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Face Group ID"], face_group_id)
    else:
        node.inputs["Face Group ID"].default_value = face_group_id


    return node

def mesh_grid(ng, size_x=1.0, size_y=1.0, vertices_x=None, vertices_y=None, ):

    node = ng.nodes.new("GeometryNodeMeshGrid")
    if isinstance(size_x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Size X"], size_x)
    else:
        node.inputs["Size X"].default_value = size_x
    if isinstance(size_y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Size Y"], size_y)
    else:
        node.inputs["Size Y"].default_value = size_y
    if isinstance(vertices_x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices X"], vertices_x)
    else:
        node.inputs["Vertices X"].default_value = vertices_x
    if isinstance(vertices_y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices Y"], vertices_y)
    else:
        node.inputs["Vertices Y"].default_value = vertices_y


    return node

def mesh_ico_sphere(ng, radius=1.0, subdivisions=None, ):

    node = ng.nodes.new("GeometryNodeMeshIcoSphere")
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius
    if isinstance(subdivisions, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Subdivisions"], subdivisions)
    else:
        node.inputs["Subdivisions"].default_value = subdivisions


    return node

def mesh_line(ng, count=None, resolution=1.0, start_location=[0.0, 0.0, 0.0], offset=[0.0, 0.0, 1.0], mode='OFFSET', count_mode='TOTAL'):

    node = ng.nodes.new("GeometryNodeMeshLine")
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"].default_value = count
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"].default_value = resolution
    if isinstance(start_location, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Location"], start_location)
    else:
        node.inputs["Start Location"].default_value = start_location
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"].default_value = offset
    node.mode = mode
    node.count_mode = count_mode


    return node

def mesh_to_curve(ng, mesh=None, selection=None, ):

    node = ng.nodes.new("GeometryNodeMeshToCurve")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection


    return node

def mesh_to_points(ng, mesh=None, selection=None, position=[0.0, 0.0, 0.0], radius=0.05000000074505806, mode='VERTICES'):

    node = ng.nodes.new("GeometryNodeMeshToPoints")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"].default_value = position
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius
    node.mode = mode


    return node

def mesh_to_volume(ng, mesh=None, density=1.0, voxel_size=0.30000001192092896, voxel_amount=64.0, exterior_band_width=0.10000000149011612, interior_band_width=0.0, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

    node = ng.nodes.new("GeometryNodeMeshToVolume")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"].default_value = density
    if isinstance(voxel_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Size"], voxel_size)
    else:
        node.inputs["Voxel Size"].default_value = voxel_size
    if isinstance(voxel_amount, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Amount"], voxel_amount)
    else:
        node.inputs["Voxel Amount"].default_value = voxel_amount
    if isinstance(exterior_band_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Exterior Band Width"], exterior_band_width)
    else:
        node.inputs["Exterior Band Width"].default_value = exterior_band_width
    if isinstance(interior_band_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Interior Band Width"], interior_band_width)
    else:
        node.inputs["Interior Band Width"].default_value = interior_band_width
    if isinstance(fill_volume, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Volume"], fill_volume)
    else:
        node.inputs["Fill Volume"].default_value = fill_volume
    node.resolution_mode = resolution_mode


    return node

def mesh_uv_sphere(ng, segments=None, rings=None, radius=1.0, ):

    node = ng.nodes.new("GeometryNodeMeshUVSphere")
    if isinstance(segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Segments"], segments)
    else:
        node.inputs["Segments"].default_value = segments
    if isinstance(rings, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rings"], rings)
    else:
        node.inputs["Rings"].default_value = rings
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius


    return node

def object_info(ng, object=None, as_instance=None, transform_space='ORIGINAL'):

    node = ng.nodes.new("GeometryNodeObjectInfo")
    if isinstance(object, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Object"], object)
    else:
        node.inputs["Object"].default_value = object
    if isinstance(as_instance, bpy.types.NodeSocket):
        ng.links.new(node.inputs["As Instance"], as_instance)
    else:
        node.inputs["As Instance"].default_value = as_instance
    node.transform_space = transform_space


    return node

def offset_corner_in_face(ng, corner_index=None, offset=None, ):

    node = ng.nodes.new("GeometryNodeOffsetCornerInFace")
    if isinstance(corner_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Corner Index"], corner_index)
    else:
        node.inputs["Corner Index"].default_value = corner_index
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"].default_value = offset


    return node

def offset_point_in_curve(ng, point_index=None, offset=None, ):

    node = ng.nodes.new("GeometryNodeOffsetPointInCurve")
    if isinstance(point_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point Index"], point_index)
    else:
        node.inputs["Point Index"].default_value = point_index
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"].default_value = offset


    return node

def points(ng, count=None, position=[0.0, 0.0, 0.0], radius=0.10000000149011612, ):

    node = ng.nodes.new("GeometryNodePoints")
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"].default_value = count
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"].default_value = position
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius


    return node

def points_of_curve(ng, curve_index=None, weights=0.0, sort_index=None, ):

    node = ng.nodes.new("GeometryNodePointsOfCurve")
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"].default_value = curve_index
    if isinstance(weights, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weights"], weights)
    else:
        node.inputs["Weights"].default_value = weights
    if isinstance(sort_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sort Index"], sort_index)
    else:
        node.inputs["Sort Index"].default_value = sort_index


    return node

def points_to_vertices(ng, points=None, selection=None, ):

    node = ng.nodes.new("GeometryNodePointsToVertices")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"].default_value = points
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection


    return node

def points_to_volume(ng, points=None, density=1.0, voxel_size=0.30000001192092896, voxel_amount=64.0, radius=0.5, resolution_mode='VOXEL_AMOUNT'):

    node = ng.nodes.new("GeometryNodePointsToVolume")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"].default_value = points
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"].default_value = density
    if isinstance(voxel_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Size"], voxel_size)
    else:
        node.inputs["Voxel Size"].default_value = voxel_size
    if isinstance(voxel_amount, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Amount"], voxel_amount)
    else:
        node.inputs["Voxel Amount"].default_value = voxel_amount
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius
    node.resolution_mode = resolution_mode


    return node

def proximity(ng, target=None, source_position=[0.0, 0.0, 0.0], target_element='FACES'):

    node = ng.nodes.new("GeometryNodeProximity")
    if isinstance(target, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target"], target)
    else:
        node.inputs["Target"].default_value = target
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"].default_value = source_position
    node.target_element = target_element


    return node

def raycast_float(ng, target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"].default_value = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], attribute)
    else:
        node.inputs[0] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"].default_value = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"].default_value = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"].default_value = ray_length
    node.mapping = mapping
    node.data_type = data_type


    return node

def raycast_int(ng, target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='INT'):

    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"].default_value = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], attribute)
    else:
        node.inputs[1] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"].default_value = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"].default_value = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"].default_value = ray_length
    node.mapping = mapping
    node.data_type = data_type


    return node

def raycast_vector(ng, target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"].default_value = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], attribute)
    else:
        node.inputs[2] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"].default_value = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"].default_value = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"].default_value = ray_length
    node.mapping = mapping
    node.data_type = data_type


    return node

def raycast_color(ng, target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"].default_value = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], attribute)
    else:
        node.inputs[3] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"].default_value = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"].default_value = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"].default_value = ray_length
    node.mapping = mapping
    node.data_type = data_type


    return node

def raycast_boolean(ng, target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"].default_value = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], attribute)
    else:
        node.inputs[4] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"].default_value = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"].default_value = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"].default_value = ray_length
    node.mapping = mapping
    node.data_type = data_type


    return node

def realize_instances(ng, geometry=None, legacy_behavior=False):

    node = ng.nodes.new("GeometryNodeRealizeInstances")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    node.legacy_behavior = legacy_behavior


    return node

def remove_attribute(ng, geometry=None, name=None, ):

    node = ng.nodes.new("GeometryNodeRemoveAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"].default_value = name


    return node

def replace_material(ng, geometry=None, old=None, new=None, ):

    node = ng.nodes.new("GeometryNodeReplaceMaterial")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(old, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Old"], old)
    else:
        node.inputs["Old"].default_value = old
    if isinstance(new, bpy.types.NodeSocket):
        ng.links.new(node.inputs["New"], new)
    else:
        node.inputs["New"].default_value = new


    return node

def resample_curve(ng, curve=None, selection=None, count=None, length=0.10000000149011612, mode='COUNT'):

    node = ng.nodes.new("GeometryNodeResampleCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"].default_value = count
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length
    node.mode = mode


    return node

def reverse_curve(ng, curve=None, selection=None, ):

    node = ng.nodes.new("GeometryNodeReverseCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection


    return node

def rotate_instances(ng, instances=None, selection=None, rotation=[0.0, 0.0, 0.0], pivot_point=[0.0, 0.0, 0.0], local_space=None, ):

    node = ng.nodes.new("GeometryNodeRotateInstances")
    if isinstance(instances, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instances"], instances)
    else:
        node.inputs["Instances"].default_value = instances
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"].default_value = rotation
    if isinstance(pivot_point, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Pivot Point"], pivot_point)
    else:
        node.inputs["Pivot Point"].default_value = pivot_point
    if isinstance(local_space, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Local Space"], local_space)
    else:
        node.inputs["Local Space"].default_value = local_space


    return node

def sample_curve_float(ng, curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"].default_value = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"].default_value = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type


    return node

def sample_curve_int(ng, curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='INT'):

    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"].default_value = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"].default_value = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type


    return node

def sample_curve_vector(ng, curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"].default_value = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"].default_value = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type


    return node

def sample_curve_color(ng, curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"].default_value = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"].default_value = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type


    return node

def sample_curve_boolean(ng, curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"].default_value = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"].default_value = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"].default_value = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type


    return node

def sample_index_float(ng, geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type


    return node

def sample_index_int(ng, geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='INT'):

    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type


    return node

def sample_index_vector(ng, geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type


    return node

def sample_index_color(ng, geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type


    return node

def sample_index_boolean(ng, geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"].default_value = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type


    return node

def sample_nearest(ng, geometry=None, sample_position=[0.0, 0.0, 0.0], domain='POINT'):

    node = ng.nodes.new("GeometryNodeSampleNearest")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"].default_value = sample_position
    node.domain = domain


    return node

def sample_nearest_surface_float(ng, mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"].default_value = sample_position
    node.data_type = data_type


    return node

def sample_nearest_surface_int(ng, mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='INT'):

    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"].default_value = sample_position
    node.data_type = data_type


    return node

def sample_nearest_surface_vector(ng, mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"].default_value = sample_position
    node.data_type = data_type


    return node

def sample_nearest_surface_color(ng, mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"].default_value = sample_position
    node.data_type = data_type


    return node

def sample_nearest_surface_boolean(ng, mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"].default_value = sample_position
    node.data_type = data_type


    return node

def sample_uv_surface_float(ng, mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"].default_value = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"].default_value = sample_uv
    node.data_type = data_type


    return node

def sample_uv_surface_int(ng, mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='INT'):

    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"].default_value = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"].default_value = sample_uv
    node.data_type = data_type


    return node

def sample_uv_surface_vector(ng, mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"].default_value = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"].default_value = sample_uv
    node.data_type = data_type


    return node

def sample_uv_surface_color(ng, mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"].default_value = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"].default_value = sample_uv
    node.data_type = data_type


    return node

def sample_uv_surface_boolean(ng, mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"].default_value = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"].default_value = sample_uv
    node.data_type = data_type


    return node

def scale_elements(ng, geometry=None, selection=None, scale=1.0, center=[0.0, 0.0, 0.0], axis=[1.0, 0.0, 0.0], scale_mode='UNIFORM', domain='FACE'):

    node = ng.nodes.new("GeometryNodeScaleElements")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    if isinstance(center, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Center"], center)
    else:
        node.inputs["Center"].default_value = center
    if isinstance(axis, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Axis"], axis)
    else:
        node.inputs["Axis"].default_value = axis
    node.scale_mode = scale_mode
    node.domain = domain


    return node

def scale_instances(ng, instances=None, selection=None, scale=[1.0, 1.0, 1.0], center=[0.0, 0.0, 0.0], local_space=None, ):

    node = ng.nodes.new("GeometryNodeScaleInstances")
    if isinstance(instances, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instances"], instances)
    else:
        node.inputs["Instances"].default_value = instances
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    if isinstance(center, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Center"], center)
    else:
        node.inputs["Center"].default_value = center
    if isinstance(local_space, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Local Space"], local_space)
    else:
        node.inputs["Local Space"].default_value = local_space


    return node

def self_object(ng, ):

    node = ng.nodes.new("GeometryNodeSelfObject")


    return node

def separate_components(ng, geometry=None, ):

    node = ng.nodes.new("GeometryNodeSeparateComponents")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry


    return node

def separate_geometry(ng, geometry=None, selection=None, domain='POINT'):

    node = ng.nodes.new("GeometryNodeSeparateGeometry")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    node.domain = domain


    return node

def set_curve_handle_positions(ng, curve=None, selection=None, position=[0.0, 0.0, 0.0], offset=[0.0, 0.0, 0.0], mode='LEFT'):

    node = ng.nodes.new("GeometryNodeSetCurveHandlePositions")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"].default_value = position
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"].default_value = offset
    node.mode = mode


    return node

def set_curve_normal(ng, curve=None, selection=None, mode='MINIMUM_TWIST'):

    node = ng.nodes.new("GeometryNodeSetCurveNormal")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    node.mode = mode


    return node

def set_curve_radius(ng, curve=None, selection=None, radius=0.004999999888241291, ):

    node = ng.nodes.new("GeometryNodeSetCurveRadius")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius


    return node

def set_curve_tilt(ng, curve=None, selection=None, tilt=0.0, ):

    node = ng.nodes.new("GeometryNodeSetCurveTilt")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(tilt, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Tilt"], tilt)
    else:
        node.inputs["Tilt"].default_value = tilt


    return node

def set_id(ng, geometry=None, selection=None, id=None, ):

    node = ng.nodes.new("GeometryNodeSetID")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["ID"], id)
    else:
        node.inputs["ID"].default_value = id


    return node

def set_material(ng, geometry=None, selection=None, material=None, ):

    node = ng.nodes.new("GeometryNodeSetMaterial")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(material, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Material"], material)
    else:
        node.inputs["Material"].default_value = material


    return node

def set_material_index(ng, geometry=None, selection=None, material_index=None, ):

    node = ng.nodes.new("GeometryNodeSetMaterialIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(material_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Material Index"], material_index)
    else:
        node.inputs["Material Index"].default_value = material_index


    return node

def set_point_radius(ng, points=None, selection=None, radius=0.05000000074505806, ):

    node = ng.nodes.new("GeometryNodeSetPointRadius")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"].default_value = points
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"].default_value = radius


    return node

def set_position(ng, geometry=None, selection=None, position=[0.0, 0.0, 0.0], offset=[0.0, 0.0, 0.0], ):

    node = ng.nodes.new("GeometryNodeSetPosition")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"].default_value = position
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"].default_value = offset


    return node

def set_shade_smooth(ng, geometry=None, selection=None, shade_smooth=None, ):

    node = ng.nodes.new("GeometryNodeSetShadeSmooth")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(shade_smooth, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Shade Smooth"], shade_smooth)
    else:
        node.inputs["Shade Smooth"].default_value = shade_smooth


    return node

def set_spline_cyclic(ng, geometry=None, selection=None, cyclic=None, ):

    node = ng.nodes.new("GeometryNodeSetSplineCyclic")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(cyclic, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Cyclic"], cyclic)
    else:
        node.inputs["Cyclic"].default_value = cyclic


    return node

def set_spline_resolution(ng, geometry=None, selection=None, resolution=None, ):

    node = ng.nodes.new("GeometryNodeSetSplineResolution")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"].default_value = resolution


    return node

def spline_length(ng, ):

    node = ng.nodes.new("GeometryNodeSplineLength")


    return node

def spline_parameter(ng, ):

    node = ng.nodes.new("GeometryNodeSplineParameter")


    return node

def split_edges(ng, mesh=None, selection=None, ):

    node = ng.nodes.new("GeometryNodeSplitEdges")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection


    return node

def store_named_attribute_float(ng, geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"].default_value = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    node.domain = domain
    node.data_type = data_type


    return node

def store_named_attribute_int(ng, geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='INT'):

    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"].default_value = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    node.domain = domain
    node.data_type = data_type


    return node

def store_named_attribute_vector(ng, geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"].default_value = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    node.domain = domain
    node.data_type = data_type


    return node

def store_named_attribute_color(ng, geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='COLOR'):

    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"].default_value = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    node.domain = domain
    node.data_type = data_type


    return node

def store_named_attribute_boolean(ng, geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"].default_value = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    node.domain = domain
    node.data_type = data_type


    return node

def string_join(ng, delimiter=None, strings=None):

    node = ng.nodes.new("GeometryNodeStringJoin")
    if isinstance(delimiter, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Delimiter"], delimiter)
    else:
        node.inputs["Delimiter"].default_value = delimiter
    if isinstance(strings, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Strings"], strings)
    else:
        node.inputs["Strings"].default_value = strings


    return node

def string_to_curves(ng, string,  size=1.0, character_spacing=1.0, word_spacing=1.0, line_spacing=1.0, text_box_width=0.0, text_box_height=0.0, align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT', overflow='OVERFLOW', font=None, align_x='LEFT'):

    node = ng.nodes.new("GeometryNodeStringToCurves")
    if isinstance(string,  bpy.types.NodeSocket):
        ng.links.new(node.inputs["String"], string)
    else:
        node.inputs["String"].default_value = string
    if isinstance(size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Size"], size)
    else:
        node.inputs["Size"].default_value = size
    if isinstance(character_spacing,  bpy.types.NodeSocket):
        ng.links.new(node.inputs["Character Spacing"], character_spacing)
    else:
        node.inputs["Character Spacing"].default_value = character_spacing
    if isinstance(word_spacing,  bpy.types.NodeSocket):
        ng.links.new(node.inputs["Word Spacing"], word_spacing)
    else:
        node.inputs["Word Spacing"].default_value = word_spacing
    if isinstance(line_spacing,  bpy.types.NodeSocket):
        ng.links.new(node.inputs["Line Spacing"], line_spacing)
    else:
        node.inputs["Line Spacing"].default_value = line_spacing
    if isinstance(text_box_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Text Box Width"], text_box_width)
    else:
        node.inputs["Text Box Width"].default_value = text_box_width
    if isinstance(text_box_height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Text Box Height"], text_box_height)
    else:
        node.inputs["Text Box Height"].default_value = text_box_height
    node.align_y = align_y
    node.pivot_mode = pivot_mode
    node.overflow = overflow
    node.font = font
    node.align_x = align_x


    return node

def subdivide_curve(ng, curve=None, cuts=None):

    node = ng.nodes.new("GeometryNodeSubdivideCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(cuts, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Cuts"], cuts)
    else:
        node.inputs["Cuts"].default_value = cuts


    return node

def subdivide_mesh(ng, mesh=None, level=None):

    node = ng.nodes.new("GeometryNodeSubdivideMesh")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(level, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Level"], level)
    else:
        node.inputs["Level"].default_value = level


    return node

def subdivision_surface(ng, mesh=None, level=None, edge_crease=0.0, vertex_crease=0.0, uv_smooth='PRESERVE_BOUNDARIES', boundary_smooth='ALL'):

    node = ng.nodes.new("GeometryNodeSubdivisionSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(level, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Level"], level)
    else:
        node.inputs["Level"].default_value = level
    if isinstance(edge_crease, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Edge Crease"], edge_crease)
    else:
        node.inputs["Edge Crease"].default_value = edge_crease
    if isinstance(vertex_crease, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertex Crease"], vertex_crease)
    else:
        node.inputs["Vertex Crease"].default_value = vertex_crease
    node.uv_smooth = uv_smooth
    node.boundary_smooth = boundary_smooth


    return node

def switch_float(ng, switch=False, false=0.0, true=0.0, input_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], switch)
    else:
        node.inputs[0] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], false)
    else:
        node.inputs[2] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], true)
    else:
        node.inputs[3] = true
    node.input_type = input_type


    return node

def switch_int(ng, switch=False, false=0.0, true=0.0, input_type='INT'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], switch)
    else:
        node.inputs[0] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], false)
    else:
        node.inputs[4] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[5], true)
    else:
        node.inputs[5] = true
    node.input_type = input_type


    return node

def switch_boolean(ng, switch=False, false=0.0, true=0.0, input_type='BOOLEAN'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], switch)
    else:
        node.inputs[0] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[6], false)
    else:
        node.inputs[6] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[7], true)
    else:
        node.inputs[7] = true
    node.input_type = input_type


    return node

def switch_vector(ng, switch=False, false=0.0, true=0.0, input_type='VECTOR'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], switch)
    else:
        node.inputs[0] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[8], false)
    else:
        node.inputs[8] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[9], true)
    else:
        node.inputs[9] = true
    node.input_type = input_type


    return node

def switch_color(ng, switch=False, false=0.0, true=0.0, input_type='RGBA'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], switch)
    else:
        node.inputs[0] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[10], false)
    else:
        node.inputs[10] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[11], true)
    else:
        node.inputs[11] = true
    node.input_type = input_type


    return node

def switch_string(ng, switch=False, false=0.0, true=0.0, input_type='STRING'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], switch)
    else:
        node.inputs[0] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[12], false)
    else:
        node.inputs[12] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[13], true)
    else:
        node.inputs[13] = true
    node.input_type = input_type


    return node

def switch_geometry(ng, switch=False, false=0.0, true=0.0, input_type='GEOMETRY'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], switch)
    else:
        node.inputs[1] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[14], false)
    else:
        node.inputs[14] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[15], true)
    else:
        node.inputs[15] = true
    node.input_type = input_type


    return node

def switch_object(ng, switch=False, false=0.0, true=0.0, input_type='OBJECT'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], switch)
    else:
        node.inputs[1] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[16], false)
    else:
        node.inputs[16] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[17], true)
    else:
        node.inputs[17] = true
    node.input_type = input_type


    return node

def switch_collection(ng, switch=False, false=0.0, true=0.0, input_type='COLLECTION'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], switch)
    else:
        node.inputs[1] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[18], false)
    else:
        node.inputs[18] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[19], true)
    else:
        node.inputs[19] = true
    node.input_type = input_type


    return node

def switch_texture(ng, switch=False, false=0.0, true=0.0, input_type='TEXTURE'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], switch)
    else:
        node.inputs[1] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[20], false)
    else:
        node.inputs[20] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[21], true)
    else:
        node.inputs[21] = true
    node.input_type = input_type


    return node

def switch_material(ng, switch=False, false=0.0, true=0.0, input_type='MATERIAL'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], switch)
    else:
        node.inputs[1] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[22], false)
    else:
        node.inputs[22] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[23], true)
    else:
        node.inputs[23] = true
    node.input_type = input_type


    return node

def switch_image(ng, switch=False, false=0.0, true=0.0, input_type='IMAGE'):

    node = ng.nodes.new("GeometryNodeSwitch")
    if isinstance(switch, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], switch)
    else:
        node.inputs[1] = switch
    if isinstance(false, bpy.types.NodeSocket):
        ng.links.new(node.inputs[24], false)
    else:
        node.inputs[24] = false
    if isinstance(true, bpy.types.NodeSocket):
        ng.links.new(node.inputs[25], true)
    else:
        node.inputs[25] = true
    node.input_type = input_type


    return node

def transform(ng, geometry=None, translation=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0], scale=[1.0, 1.0, 1.0], ):

    node = ng.nodes.new("GeometryNodeTransform")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(translation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Translation"], translation)
    else:
        node.inputs["Translation"].default_value = translation
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"].default_value = rotation
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale


    return node

def translate_instances(ng, instances=None, selection=None, translation=[0.0, 0.0, 0.0], local_space=None, ):

    node = ng.nodes.new("GeometryNodeTranslateInstances")
    if isinstance(instances, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instances"], instances)
    else:
        node.inputs["Instances"].default_value = instances
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(translation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Translation"], translation)
    else:
        node.inputs["Translation"].default_value = translation
    if isinstance(local_space, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Local Space"], local_space)
    else:
        node.inputs["Local Space"].default_value = local_space


    return node

def triangulate(ng, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

    node = ng.nodes.new("GeometryNodeTriangulate")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"].default_value = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(minimum_vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Minimum Vertices"], minimum_vertices)
    else:
        node.inputs["Minimum Vertices"].default_value = minimum_vertices
    node.ngon_method = ngon_method
    node.quad_method = quad_method


    return node

def trim_curve(ng, curve=None, selection=None, start=0.0, end=1.0, mode='FACTOR'):

    node = ng.nodes.new("GeometryNodeTrimCurve")
    if mode == 'FACTOR':
        start_ind, end_ind = 1, 2
    else:
        start_ind, end_ind = 3, 4
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"].default_value = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs[start_ind], start)
    else:
        node.inputs[start_ind] = start
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs[end_ind], end)
    else:
        node.inputs[end_ind] = end
    node.mode = mode


    return node

def uv_pack_islands(ng, uv=[0.0, 0.0, 0.0], selection=None, margin=0.0010000000474974513, rotate=None, ):

    node = ng.nodes.new("GeometryNodeUVPackIslands")
    if isinstance(uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["UV"], uv)
    else:
        node.inputs["UV"].default_value = uv
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(margin, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Margin"], margin)
    else:
        node.inputs["Margin"].default_value = margin
    if isinstance(rotate, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotate"], rotate)
    else:
        node.inputs["Rotate"].default_value = rotate


    return node

def uv_unwrap(ng, selection=None, seam=None, margin=0.0010000000474974513, fill_holes=None, method='ANGLE_BASED'):

    node = ng.nodes.new("GeometryNodeUVUnwrap")
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"].default_value = selection
    if isinstance(seam, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seam"], seam)
    else:
        node.inputs["Seam"].default_value = seam
    if isinstance(margin, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Margin"], margin)
    else:
        node.inputs["Margin"].default_value = margin
    if isinstance(fill_holes, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Holes"], fill_holes)
    else:
        node.inputs["Fill Holes"].default_value = fill_holes
    node.method = method


    return node

def vertex_of_corner(ng, corner_index=None, ):

    node = ng.nodes.new("GeometryNodeVertexOfCorner")
    if isinstance(corner_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Corner Index"], corner_index)
    else:
        node.inputs["Corner Index"].default_value = corner_index


    return node

def viewer(ng, geometry=None, value=0.0, domain='AUTO', data_type='FLOAT'):

    node = ng.nodes.new("GeometryNodeViewer")
    index = {'FLOAT': 0, 'VECTOR': 1, 'FLOAT_COLOR': 2,
             'INT': 3, 'BOOLEAN': 4}[data_type]
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[index], value)
    else:
        node.inputs[index] = value

    node.domain = domain
    node.data_type = data_type


    return node

def volume_cube(ng, density=1.0, background=0.0, min=[-1.0, -1.0, -1.0], max=[1.0, 1.0, 1.0], resolution_x=None, resolution_y=None, resolution_z=None, ):

    node = ng.nodes.new("GeometryNodeVolumeCube")
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"].default_value = density
    if isinstance(background, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Background"], background)
    else:
        node.inputs["Background"].default_value = background
    if isinstance(min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Min"], min)
    else:
        node.inputs["Min"].default_value = min
    if isinstance(max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Max"], max)
    else:
        node.inputs["Max"].default_value = max
    if isinstance(resolution_x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution X"], resolution_x)
    else:
        node.inputs["Resolution X"].default_value = resolution_x
    if isinstance(resolution_y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution Y"], resolution_y)
    else:
        node.inputs["Resolution Y"].default_value = resolution_y
    if isinstance(resolution_z, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution Z"], resolution_z)
    else:
        node.inputs["Resolution Z"].default_value = resolution_z


    return node

def volume_to_mesh(ng, volume=None, voxel_size=0.30000001192092896, voxel_amount=64.0, threshold=0.10000000149011612, adaptivity=0.0, resolution_mode='GRID'):

    node = ng.nodes.new("GeometryNodeVolumeToMesh")
    if isinstance(volume, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Volume"], volume)
    else:
        node.inputs["Volume"].default_value = volume
    if isinstance(voxel_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Size"], voxel_size)
    else:
        node.inputs["Voxel Size"].default_value = voxel_size
    if isinstance(voxel_amount, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Amount"], voxel_amount)
    else:
        node.inputs["Voxel Amount"].default_value = voxel_amount
    if isinstance(threshold, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Threshold"], threshold)
    else:
        node.inputs["Threshold"].default_value = threshold
    if isinstance(adaptivity, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Adaptivity"], adaptivity)
    else:
        node.inputs["Adaptivity"].default_value = adaptivity
    node.resolution_mode = resolution_mode


    return node

def frame(ng, shrink=True, text=None, label_size=20):

    node = ng.nodes.new("NodeFrame")
    node.shrink = shrink
    node.text = text
    node.label_size = label_size


    return node

def group_input(ng, ):

    node = ng.nodes.new("NodeGroupInput")


    return node

def group_output(ng, geometry=None, is_active_output=True):

    node = ng.nodes.new("NodeGroupOutput")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"].default_value = geometry
    node.is_active_output = is_active_output


    return node

def reroute(ng, input=None, ):

    node = ng.nodes.new("NodeReroute")
    if isinstance(input, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Input"], input)
    else:
        node.inputs["Input"].default_value = input


    return node

def clamp(ng, value=1.0, min=0.0, max=1.0, clamp_type='MINMAX'):

    node = ng.nodes.new("ShaderNodeClamp")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"].default_value = value
    if isinstance(min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Min"], min)
    else:
        node.inputs["Min"].default_value = min
    if isinstance(max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Max"], max)
    else:
        node.inputs["Max"].default_value = max
    node.clamp_type = clamp_type


    return node

def combine_rgb(ng, r=0.0, g=0.0, b=0.0, ):

    node = ng.nodes.new("ShaderNodeCombineRGB")
    if isinstance(r, bpy.types.NodeSocket):
        ng.links.new(node.inputs["R"], r)
    else:
        node.inputs["R"].default_value = r
    if isinstance(g, bpy.types.NodeSocket):
        ng.links.new(node.inputs["G"], g)
    else:
        node.inputs["G"].default_value = g
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs["B"], b)
    else:
        node.inputs["B"].default_value = b


    return node

def combine_xyz(ng, x=0.0, y=0.0, z=0.0, ):

    node = ng.nodes.new("ShaderNodeCombineXYZ")
    if isinstance(x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["X"], x)
    else:
        node.inputs["X"].default_value = x
    if isinstance(y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Y"], y)
    else:
        node.inputs["Y"].default_value = y
    if isinstance(z, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Z"], z)
    else:
        node.inputs["Z"].default_value = z

# TODO : Mapping


    return node

def float_curve(ng, factor=1.0, value=1.0):

    node = ng.nodes.new("ShaderNodeFloatCurve")
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"].default_value = value


    return node

def map_range_float(ng, value=1.0, from_min=0.0, from_max=1.0, to_min=0.0, to_max=1.0, steps=4.0, vector=[0.0, 0.0, 0.0], interpolation_type='LINEAR', clamp=True, data_type='FLOAT'):

    node = ng.nodes.new("ShaderNodeMapRange")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"].default_value = value
    if isinstance(from_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["From Min"], from_min)
    else:
        node.inputs["From Min"].default_value = from_min
    if isinstance(from_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["From Max"], from_max)
    else:
        node.inputs["From Max"].default_value = from_max
    if isinstance(to_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["To Min"], to_min)
    else:
        node.inputs["To Min"].default_value = to_min
    if isinstance(to_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["To Max"], to_max)
    else:
        node.inputs["To Max"].default_value = to_max
    if isinstance(steps, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Steps"], steps)
    else:
        node.inputs["Steps"].default_value = steps
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector

    node.interpolation_type = interpolation_type
    node.clamp = clamp
    node.data_type = data_type


    return node

def map_range_vector(ng, value=1.0, from_min=0.0, from_max=1.0, to_min=0.0, to_max=1.0, steps=4.0, vector=[0.0, 0.0, 0.0], interpolation_type='LINEAR', clamp=True, data_type='VECTOR_FLOAT'):

    node = ng.nodes.new("ShaderNodeMapRange")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"].default_value = value
    if isinstance(from_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs[7], from_min)
    else:
        node.inputs[7] = from_min
    if isinstance(from_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs[8], from_max)
    else:
        node.inputs[8] = from_max
    if isinstance(to_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs[9], to_min)
    else:
        node.inputs[9] = to_min
    if isinstance(to_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs[10], to_max)
    else:
        node.inputs[10] = to_max
    if isinstance(steps, bpy.types.NodeSocket):
        ng.links.new(node.inputs[11], steps)
    else:
        node.inputs[11] = steps
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector

    node.interpolation_type = interpolation_type
    node.clamp = clamp
    node.data_type = data_type


    return node

def math(ng, a=0.5, b=0.5, c=0.5, operation='ADD', use_clamp=False):

    node = ng.nodes.new("ShaderNodeMath")
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], a)
    else:
        node.inputs[0].default_value = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], b)
    else:
        node.inputs[1].default_value = b
    if isinstance(c, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], c)
    else:
        node.inputs[2].default_value = c
    node.operation = operation
    node.use_clamp = use_clamp


    return node

def mix_float(ng, factor=0.5, a=0.0, b=0.0, clamp_result=False, blend_type='MIX', clamp_factor=True, data_type='FLOAT', factor_mode='UNIFORM'):

    node = ng.nodes.new("ShaderNodeMix")
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor

    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs["A"], a)
    else:
        node.inputs["A"].default_value = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs["B"], b)
    else:
        node.inputs["B"].default_value = b

    node.clamp_result = clamp_result
    node.blend_type = blend_type
    node.clamp_factor = clamp_factor
    node.data_type = data_type
    node.factor_mode = factor_mode


    return node

def mix_vector(ng, factor=0.5, a=0.0, b=0.0, clamp_result=False, blend_type='MIX', clamp_factor=True, data_type='VECTOR_FLOAT', factor_mode='UNIFORM'):

    node = ng.nodes.new("ShaderNodeMix")
    if factor_mode == 'UNIFORM':
        if isinstance(factor, bpy.types.NodeSocket):
            ng.links.new(node.inputs["Factor"], factor)
        else:
            node.inputs["Factor"].default_value = factor
    else:
        if isinstance(factor, bpy.types.NodeSocket):
            ng.links.new(node.inputs[1], factor)
        else:
            node.inputs[1] = factor
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], a)
    else:
        node.inputs[4] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[5], b)
    else:
        node.inputs[5] = b

    node.clamp_result = clamp_result
    node.blend_type = blend_type
    node.clamp_factor = clamp_factor
    node.data_type = data_type
    node.factor_mode = factor_mode


    return node

def mix_color(ng, factor=0.5,  a=0.0, b=0.0, clamp_result=False, blend_type='MIX', clamp_factor=True, data_type='COLOR', factor_mode='UNIFORM'):

    node = ng.nodes.new("ShaderNodeMix")
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"].default_value = factor

    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[6], a)
    else:
        node.inputs[6] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[7], b)
    else:
        node.inputs[7] = b

    node.clamp_result = clamp_result
    node.blend_type = blend_type
    node.clamp_factor = clamp_factor
    node.data_type = data_type
    node.factor_mode = factor_mode


    return node

def mix_rgb(ng, fac=0.5, color1=None, color2=None, blend_type='MIX', use_clamp=False, use_alpha=False):

    node = ng.nodes.new("ShaderNodeMixRGB")
    if isinstance(fac, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fac"], fac)
    else:
        node.inputs["Fac"].default_value = fac
    if isinstance(color1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color1"], color1)
    else:
        node.inputs["Color1"].default_value = color1
    if isinstance(color2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color2"], color2)
    else:
        node.inputs["Color2"].default_value = color2
    node.blend_type = blend_type
    node.use_clamp = use_clamp
    node.use_alpha = use_alpha

# TODO : Mapping


    return node

def rgb_curve(ng, fac=1.0, color=None):

    node = ng.nodes.new("ShaderNodeRGBCurve")
    if isinstance(fac, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fac"], fac)
    else:
        node.inputs["Fac"].default_value = fac
    if isinstance(color, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color"], color)
    else:
        node.inputs["Color"].default_value = color


    return node

def separate_rgb(ng, image=None, ):

    node = ng.nodes.new("ShaderNodeSeparateRGB")
    if isinstance(image, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Image"], image)
    else:
        node.inputs["Image"].default_value = image


    return node

def separate_xyz(ng, vector=[0.0, 0.0, 0.0], ):

    node = ng.nodes.new("ShaderNodeSeparateXYZ")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector

# TODO: color_mapping,  texture_mappiing


    return node

def tex_brick(ng, vector=[0.0, 0.0, 0.0], color1=None, color2=None, mortar=None, scale=5.0, mortar_size=0.019999999552965164, mortar_smooth=0.10000000149011612, bias=0.0, brick_width=0.5, row_height=0.25, offset=0.5, squash=1.0,  squash_frequency=2, offset_frequency=2):

    node = ng.nodes.new("ShaderNodeTexBrick")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(color1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color1"], color1)
    else:
        node.inputs["Color1"].default_value = color1
    if isinstance(color2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color2"], color2)
    else:
        node.inputs["Color2"].default_value = color2
    if isinstance(mortar, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mortar"], mortar)
    else:
        node.inputs["Mortar"].default_value = mortar
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    if isinstance(mortar_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mortar Size"], mortar_size)
    else:
        node.inputs["Mortar Size"].default_value = mortar_size
    if isinstance(mortar_smooth, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mortar Smooth"], mortar_smooth)
    else:
        node.inputs["Mortar Smooth"].default_value = mortar_smooth
    if isinstance(bias, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Bias"], bias)
    else:
        node.inputs["Bias"].default_value = bias
    if isinstance(brick_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Brick Width"], brick_width)
    else:
        node.inputs["Brick Width"].default_value = brick_width
    if isinstance(row_height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Row Height"], row_height)
    else:
        node.inputs["Row Height"].default_value = row_height
    node.offset = offset
    node.squash = squash
    node.squash_frequency = squash_frequency
    node.offset_frequency = offset_frequency

# TODO : color_mapping,  texture_mapping


    return node

def tex_checker(ng, vector=[0.0, 0.0, 0.0], color1=None, color2=None, scale=5.0):

    node = ng.nodes.new("ShaderNodeTexChecker")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(color1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color1"], color1)
    else:
        node.inputs["Color1"].default_value = color1
    if isinstance(color2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color2"], color2)
    else:
        node.inputs["Color2"].default_value = color2
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale

# TOOD: color_mapping,  texture_mapping


    return node

def tex_gradient(ng, vector=[0.0, 0.0, 0.0], gradient_type='LINEAR'):

    node = ng.nodes.new("ShaderNodeTexGradient")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    node.gradient_type = gradient_type

# TOOD: color_mapping,  texture_mapping


    return node

def tex_magic(ng, vector=[0.0, 0.0, 0.0], scale=5.0, distortion=1.0, turbulence_depth=2):

    node = ng.nodes.new("ShaderNodeTexMagic")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    if isinstance(distortion, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distortion"], distortion)
    else:
        node.inputs["Distortion"].default_value = distortion
    node.turbulence_depth = turbulence_depth

# TOOD: color_mapping,  texture_mapping


    return node

def tex_musgrave(ng, vector=[0.0, 0.0, 0.0], w=0.0, scale=5.0, detail=2.0, dimension=2.0, lacunarity=2.0, offset=0.0, gain=1.0, musgrave_type='FBM', musgrave_dimensions='3D'):

    node = ng.nodes.new("ShaderNodeTexMusgrave")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(w, bpy.types.NodeSocket):
        ng.links.new(node.inputs["W"], w)
    else:
        node.inputs["W"].default_value = w
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    if isinstance(detail, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail"], detail)
    else:
        node.inputs["Detail"].default_value = detail
    if isinstance(dimension, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Dimension"], dimension)
    else:
        node.inputs["Dimension"].default_value = dimension
    if isinstance(lacunarity, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Lacunarity"], lacunarity)
    else:
        node.inputs["Lacunarity"].default_value = lacunarity
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"].default_value = offset
    if isinstance(gain, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Gain"], gain)
    else:
        node.inputs["Gain"].default_value = gain
    node.musgrave_type = musgrave_type
    node.musgrave_dimensions = musgrave_dimensions

# TOOD: color_mapping,  texture_mapping


    return node

def tex_noise(ng, vector=[0.0, 0.0, 0.0], w=0.0, scale=5.0, detail=2.0, roughness=0.5, distortion=0.0, noise_dimensions='3D'):

    node = ng.nodes.new("ShaderNodeTexNoise")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(w, bpy.types.NodeSocket):
        ng.links.new(node.inputs["W"], w)
    else:
        node.inputs["W"].default_value = w
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    if isinstance(detail, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail"], detail)
    else:
        node.inputs["Detail"].default_value = detail
    if isinstance(roughness, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Roughness"], roughness)
    else:
        node.inputs["Roughness"].default_value = roughness
    if isinstance(distortion, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distortion"], distortion)
    else:
        node.inputs["Distortion"].default_value = distortion
    node.noise_dimensions = noise_dimensions

# TOOD: color_mapping,  texture_mapping


    return node

def tex_voronoi(ng, vector=[0.0, 0.0, 0.0], w=0.0, scale=5.0, smoothness=1.0, exponent=0.5, randomness=1.0, distance='EUCLIDEAN', voronoi_dimensions='3D', feature='F1'):

    node = ng.nodes.new("ShaderNodeTexVoronoi")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(w, bpy.types.NodeSocket):
        ng.links.new(node.inputs["W"], w)
    else:
        node.inputs["W"].default_value = w
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    if isinstance(smoothness, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Smoothness"], smoothness)
    else:
        node.inputs["Smoothness"].default_value = smoothness
    if isinstance(exponent, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Exponent"], exponent)
    else:
        node.inputs["Exponent"].default_value = exponent
    if isinstance(randomness, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Randomness"], randomness)
    else:
        node.inputs["Randomness"].default_value = randomness
    node.distance = distance
    node.voronoi_dimensions = voronoi_dimensions
    node.feature = feature

# TOOD: color_mapping,  texture_mapping


    return node

def tex_wave(ng, vector=[0.0, 0.0, 0.0], scale=5.0, distortion=0.0, detail=2.0, detail_scale=1.0, detail_roughness=0.5, phase_offset=0.0, wave_profile='SIN', wave_type='BANDS', bands_direction='X', rings_direction='X'):

    node = ng.nodes.new("ShaderNodeTexWave")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    if isinstance(distortion, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distortion"], distortion)
    else:
        node.inputs["Distortion"].default_value = distortion
    if isinstance(detail, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail"], detail)
    else:
        node.inputs["Detail"].default_value = detail
    if isinstance(detail_scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail Scale"], detail_scale)
    else:
        node.inputs["Detail Scale"].default_value = detail_scale
    if isinstance(detail_roughness, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail Roughness"], detail_roughness)
    else:
        node.inputs["Detail Roughness"].default_value = detail_roughness
    if isinstance(phase_offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Phase Offset"], phase_offset)
    else:
        node.inputs["Phase Offset"].default_value = phase_offset
    node.wave_profile = wave_profile
    node.wave_type = wave_type
    node.bands_direction = bands_direction
    node.rings_direction = rings_direction


    return node

def tex_white_noise(ng, vector=[0.0, 0.0, 0.0], w=0.0, noise_dimensions='3D'):

    node = ng.nodes.new("ShaderNodeTexWhiteNoise")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(w, bpy.types.NodeSocket):
        ng.links.new(node.inputs["W"], w)
    else:
        node.inputs["W"].default_value = w
    node.noise_dimensions = noise_dimensions

# TODO : ColorRamp


    return node

def val_to_rgb(ng, fac=0.5):

    node = ng.nodes.new("ShaderNodeValToRGB")
    if isinstance(fac, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fac"], fac)
    else:
        node.inputs["Fac"].default_value = fac


    return node

def value(ng, ):

    node = ng.nodes.new("ShaderNodeValue")

# TODO: CurveMapping


    return node

def vector_curve(ng, fac=1.0, vector=[0.0, 0.0, 0.0]):

    node = ng.nodes.new("ShaderNodeVectorCurve")
    if isinstance(fac, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fac"], fac)
    else:
        node.inputs["Fac"].default_value = fac
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector


    return node

def vector_math(ng, a=[0.0, 0.0, 0.0], b=[0.0, 0.0, 0.0], c=[0.0, 0.0, 0.0], scale=1.0, operation='ADD'):

    node = ng.nodes.new("ShaderNodeVectorMath")
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], a)
    else:
        node.inputs[0] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], b)
    else:
        node.inputs[1] = b
    if isinstance(c, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], c)
    else:
        node.inputs[2] = c
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"].default_value = scale
    node.operation = operation


    return node

def vector_rotate(ng, vector=[0.0, 0.0, 0.0], center=[0.0, 0.0, 0.0], axis=[0.0, 0.0, 1.0], angle=0.0, rotation=[0.0, 0.0, 0.0], rotation_type='AXIS_ANGLE', invert=False):

    node = ng.nodes.new("ShaderNodeVectorRotate")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"].default_value = vector
    if isinstance(center, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Center"], center)
    else:
        node.inputs["Center"].default_value = center
    if isinstance(axis, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Axis"], axis)
    else:
        node.inputs["Axis"].default_value = axis
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"].default_value = angle
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"].default_value = rotation
    node.rotation_type = rotation_type
    node.invert = invert

    return node
