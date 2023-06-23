import bpy
ng=bpy.context.space_data.edit_tree

def align_euler_to_vector(rotation=[0.0, 0.0, 0.0], factor=1.0, vector=[0.0, 0.0, 1.0], axis='X', pivot_axis='AUTO'):
    node = ng.nodes.new("FunctionNodeAlignEulerToVector")
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"] = rotation
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    node.axis = axis
    node.pivot_axis = pivot_axis

def boolean_math(a=None, b=None, operation='AND'):
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

def combine_color(red=0.0, green=0.0, blue=0.0, alpha=1.0, mode='RGB'):
    node = ng.nodes.new("FunctionNodeCombineColor")
    if isinstance(red, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Red"], red)
    else:
        node.inputs["Red"] = red
    if isinstance(green, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Green"], green)
    else:
        node.inputs["Green"] = green
    if isinstance(blue, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Blue"], blue)
    else:
        node.inputs["Blue"] = blue
    if isinstance(alpha, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Alpha"], alpha)
    else:
        node.inputs["Alpha"] = alpha
    node.mode = mode

def compare_float(a=0, b=0, c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='FLOAT'):
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
        node.inputs["C"] = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"] = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"] = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type

def compare_int(a=0, b=0, c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='INT'):
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
        node.inputs["C"] = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"] = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"] = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type

def compare_vector(a=(0,0,0), b=(0,0,0), c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='VECTOR'):
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
        node.inputs["C"] = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"] = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"] = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type

def compare_string(a='', b='', c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='STRING'):
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
        node.inputs["C"] = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"] = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"] = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type
    

def compare_color(a=(0,0,0,0), b=(0,0,0,0), c=0.8999999761581421, angle=0.08726649731397629, epsilon=0.0010000000474974513, operation='GREATER_THAN', mode='ELEMENT', data_type='COLOR'):
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
        node.inputs["C"] = c
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"] = angle
    if isinstance(epsilon, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Epsilon"], epsilon)
    else:
        node.inputs["Epsilon"] = epsilon
    node.operation = operation
    node.mode = mode
    node.data_type = data_type
    

def float_to_int(float=0.0, rounding_mode='ROUND'):
    node = ng.nodes.new("FunctionNodeFloatToInt")
    if isinstance(float, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Float"], float)
    else:
        node.inputs["Float"] = float
    node.rounding_mode = rounding_mode

def input_bool(boolean=False):
    node = ng.nodes.new("FunctionNodeInputBool")
    node.boolean = boolean

def input_color(color=(0,0,0,0)):
    node = ng.nodes.new("FunctionNodeInputColor")
    node.color = color

def input_int(integer=0):
    node = ng.nodes.new("FunctionNodeInputInt")
    node.integer = integer

def input_special_characters():
    node = ng.nodes.new("FunctionNodeInputSpecialCharacters")

def input_string(string=''):
    node = ng.nodes.new("FunctionNodeInputString")
    node.string = string

def input_vector(vector=(0.0000, 0.0000, 0.0000)):
    node = ng.nodes.new("FunctionNodeInputVector")
    node.vector = vector

def random_value_float(min=(0,0,0), max=(1,1,1), probability=0.5, id=None, seed=None, data_type='FLOAT'):
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
        node.inputs["Probability"] = probability
    if isinstance(id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["ID"], id)
    else:
        node.inputs["ID"] = id
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"] = seed
    node.data_type = data_type

def random_value_int(min=(0,0,0), max=(1,1,1), probability=0.5, id=None, seed=None, data_type='INT'):
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
        node.inputs["Probability"] = probability
    if isinstance(id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["ID"], id)
    else:
        node.inputs["ID"] = id
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"] = seed
    node.data_type = data_type

def random_value_vector(min=(0,0,0), max=(1,1,1), probability=0.5, id=None, seed=None, data_type='VECTOR_FLOAT'):
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
        node.inputs["Probability"] = probability
    if isinstance(id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["ID"], id)
    else:
        node.inputs["ID"] = id
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"] = seed
    node.data_type = data_type


def replace_string(string=None, find=None, replace=None, ):
    node = ng.nodes.new("FunctionNodeReplaceString")
    if isinstance(string, bpy.types.NodeSocket):
        ng.links.new(node.inputs["String"], string)
    else:
        node.inputs["String"] = string
    if isinstance(find, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Find"], find)
    else:
        node.inputs["Find"] = find
    if isinstance(replace, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Replace"], replace)
    else:
        node.inputs["Replace"] = replace

def rotate_euler(rotation=[0.0, 0.0, 0.0], rotate_by=[0.0, 0.0, 0.0], axis=[0.0, 0.0, 1.0], angle=0.0, space='OBJECT'):
    node = ng.nodes.new("FunctionNodeRotateEuler")
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"] = rotation
    if isinstance(rotate_by, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotate By"], rotate_by)
    else:
        node.inputs["Rotate By"] = rotate_by
    if isinstance(axis, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Axis"], axis)
    else:
        node.inputs["Axis"] = axis
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"] = angle
    node.space = space

def separate_color(color=None, mode='RGB'):
    node = ng.nodes.new("FunctionNodeSeparateColor")
    if isinstance(color, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color"], color)
    else:
        node.inputs["Color"] = color
    node.mode = mode

def slice_string(string=None, position=None, length=None, ):
    node = ng.nodes.new("FunctionNodeSliceString")
    if isinstance(string, bpy.types.NodeSocket):
        ng.links.new(node.inputs["String"], string)
    else:
        node.inputs["String"] = string
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"] = position
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length

def string_length(string=None, ):
    node = ng.nodes.new("FunctionNodeStringLength")
    if isinstance(string, bpy.types.NodeSocket):
        ng.links.new(node.inputs["String"], string)
    else:
        node.inputs["String"] = string

def value_to_string(value=0.0, decimals=None, ):
    node = ng.nodes.new("FunctionNodeValueToString")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(decimals, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Decimals"], decimals)
    else:
        node.inputs["Decimals"] = decimals


def accumulate_field_float(value=[1.0, 1.0, 1.0], group_id=None, domain='POINT', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeAccumulateField")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Group ID"], group_id)
    else:
        node.inputs["Group ID"] = group_id
    node.domain = domain
    node.data_type = data_type

def accumulate_field_int(value=[1.0, 1.0, 1.0], group_id=None, domain='POINT', data_type='INT'):
    node = ng.nodes.new("GeometryNodeAccumulateField")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Group ID"], group_id)
    else:
        node.inputs["Group ID"] = group_id
    node.domain = domain
    node.data_type = data_type


def accumulate_field_vector(value=[1.0, 1.0, 1.0], group_id=None, domain='POINT', data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeAccumulateField")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Group ID"], group_id)
    else:
        node.inputs["Group ID"] = group_id
    node.domain = domain
    node.data_type = data_type

def attribute_domain_size(geometry=None, component='MESH'):
    node = ng.nodes.new("GeometryNodeAttributeDomainSize")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    node.component = component

def attribute_statistic_float(geometry=None, selection=None, attribute=0.0, domain='POINT', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeAttributeStatistic")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], attribute)
    else:
        node.inputs[0] = attribute
    
    node.domain = domain
    node.data_type = data_type

def attribute_statistic_vector(geometry=None, selection=None, attribute=0.0, domain='POINT', data_type='FLOAT_VECTOR'):
    node = ng.nodes.new("GeometryNodeAttributeStatistic")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], attribute)
    else:
        node.inputs[1] = attribute
    
    node.domain = domain
    node.data_type = data_type

def blur_attribute_color(value=0.0, iterations=None, weight=1.0, data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeBlurAttribute")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
   
    if isinstance(iterations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Iterations"], iterations)
    else:
        node.inputs["Iterations"] = iterations
    if isinstance(weight, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weight"], weight)
    else:
        node.inputs["Weight"] = weight
    node.data_type = data_type

def blur_attribute_float(value=0.0, iterations=None, weight=1.0, data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeBlurAttribute")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    
    if isinstance(iterations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Iterations"], iterations)
    else:
        node.inputs["Iterations"] = iterations
    if isinstance(weight, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weight"], weight)
    else:
        node.inputs["Weight"] = weight
    node.data_type = data_type

def blur_attribute_int(value=0.0, iterations=None, weight=1.0, data_type='INT'):
    node = ng.nodes.new("GeometryNodeBlurAttribute")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    
    if isinstance(iterations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Iterations"], iterations)
    else:
        node.inputs["Iterations"] = iterations
    if isinstance(weight, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weight"], weight)
    else:
        node.inputs["Weight"] = weight
    node.data_type = data_type

def blur_attribute_vector(value=0.0, iterations=None, weight=1.0, data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeBlurAttribute")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    
    if isinstance(iterations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Iterations"], iterations)
    else:
        node.inputs["Iterations"] = iterations
    if isinstance(weight, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weight"], weight)
    else:
        node.inputs["Weight"] = weight
    node.data_type = data_type

def bound_box(geometry=None, ):
    node = ng.nodes.new("GeometryNodeBoundBox")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry

def capture_attribute_float(geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    node.domain = domain
    node.data_type = data_type

def capture_attribute_int(geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='INT'):
    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    node.domain = domain
    node.data_type = data_type

def capture_attribute_vector(geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    node.domain = domain
    node.data_type = data_type

def capture_attribute_color(geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    node.domain = domain
    node.data_type = data_type

def capture_attribute_boolean(geometry=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeCaptureAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    node.domain = domain
    node.data_type = data_type

def collection_info(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
    node = ng.nodes.new("GeometryNodeCollectionInfo")
    if isinstance(collection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Collection"], collection)
    else:
        node.inputs["Collection"] = collection
    if isinstance(separate_children, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Separate Children"], separate_children)
    else:
        node.inputs["Separate Children"] = separate_children
    if isinstance(reset_children, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Reset Children"], reset_children)
    else:
        node.inputs["Reset Children"] = reset_children
    node.transform_space = transform_space

def convex_hull(geometry=None, ):
    node = ng.nodes.new("GeometryNodeConvexHull")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry

def corners_of_face(face_index=None, weights=0.0, sort_index=None, ):
    node = ng.nodes.new("GeometryNodeCornersOfFace")
    if isinstance(face_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Face Index"], face_index)
    else:
        node.inputs["Face Index"] = face_index
    if isinstance(weights, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weights"], weights)
    else:
        node.inputs["Weights"] = weights
    if isinstance(sort_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sort Index"], sort_index)
    else:
        node.inputs["Sort Index"] = sort_index

def corners_of_vertex(vertex_index=None, weights=0.0, sort_index=None, ):
    node = ng.nodes.new("GeometryNodeCornersOfVertex")
    if isinstance(vertex_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertex Index"], vertex_index)
    else:
        node.inputs["Vertex Index"] = vertex_index
    if isinstance(weights, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weights"], weights)
    else:
        node.inputs["Weights"] = weights
    if isinstance(sort_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sort Index"], sort_index)
    else:
        node.inputs["Sort Index"] = sort_index

def curve_arc(resolution=None, start=[-1.0, 0.0, 0.0], middle=[0.0, 2.0, 0.0], end=[1.0, 0.0, 0.0], radius=1.0, start_angle=0.0, sweep_angle=5.497786998748779, offset_angle=0.0, connect_center=None, invert_arc=None, mode='RADIUS'):
    node = ng.nodes.new("GeometryNodeCurveArc")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"] = resolution
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start"], start)
    else:
        node.inputs["Start"] = start
    if isinstance(middle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Middle"], middle)
    else:
        node.inputs["Middle"] = middle
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End"], end)
    else:
        node.inputs["End"] = end
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius
    if isinstance(start_angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Angle"], start_angle)
    else:
        node.inputs["Start Angle"] = start_angle
    if isinstance(sweep_angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sweep Angle"], sweep_angle)
    else:
        node.inputs["Sweep Angle"] = sweep_angle
    if isinstance(offset_angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset Angle"], offset_angle)
    else:
        node.inputs["Offset Angle"] = offset_angle
    if isinstance(connect_center, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Connect Center"], connect_center)
    else:
        node.inputs["Connect Center"] = connect_center
    if isinstance(invert_arc, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Invert Arc"], invert_arc)
    else:
        node.inputs["Invert Arc"] = invert_arc
    node.mode = mode

def curve_endpoint_selection(start_size=None, end_size=None, ):
    node = ng.nodes.new("GeometryNodeCurveEndpointSelection")
    if isinstance(start_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Size"], start_size)
    else:
        node.inputs["Start Size"] = start_size
    if isinstance(end_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End Size"], end_size)
    else:
        node.inputs["End Size"] = end_size

def curve_handle_type_selection(handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
    node = ng.nodes.new("GeometryNodeCurveHandleTypeSelection")
    node.handle_type = handle_type
    node.mode = mode

def curve_length(curve=None, ):
    node = ng.nodes.new("GeometryNodeCurveLength")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve

def curve_of_point(point_index=None, ):
    node = ng.nodes.new("GeometryNodeCurveOfPoint")
    if isinstance(point_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point Index"], point_index)
    else:
        node.inputs["Point Index"] = point_index

def curve_primitive_bezier_segment(resolution=None, start=[-1.0, 0.0, 0.0], start_handle=[-0.5, 0.5, 0.0], end_handle=[0.0, 0.0, 0.0], end=[1.0, 0.0, 0.0], mode='POSITION'):
    node = ng.nodes.new("GeometryNodeCurvePrimitiveBezierSegment")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"] = resolution
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start"], start)
    else:
        node.inputs["Start"] = start
    if isinstance(start_handle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Handle"], start_handle)
    else:
        node.inputs["Start Handle"] = start_handle
    if isinstance(end_handle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End Handle"], end_handle)
    else:
        node.inputs["End Handle"] = end_handle
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End"], end)
    else:
        node.inputs["End"] = end
    node.mode = mode

def curve_primitive_circle(resolution=None, point_1=[-1.0, 0.0, 0.0], point_2=[0.0, 1.0, 0.0], point_3=[1.0, 0.0, 0.0], radius=1.0, mode='RADIUS'):
    node = ng.nodes.new("GeometryNodeCurvePrimitiveCircle")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"] = resolution
    if isinstance(point_1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 1"], point_1)
    else:
        node.inputs["Point 1"] = point_1
    if isinstance(point_2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 2"], point_2)
    else:
        node.inputs["Point 2"] = point_2
    if isinstance(point_3, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 3"], point_3)
    else:
        node.inputs["Point 3"] = point_3
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius
    node.mode = mode

def curve_primitive_line(start=[0.0, 0.0, 0.0], end=[0.0, 0.0, 1.0], direction=[0.0, 0.0, 1.0], length=1.0, mode='POINTS'):
    node = ng.nodes.new("GeometryNodeCurvePrimitiveLine")
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start"], start)
    else:
        node.inputs["Start"] = start
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End"], end)
    else:
        node.inputs["End"] = end
    if isinstance(direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Direction"], direction)
    else:
        node.inputs["Direction"] = direction
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length
    node.mode = mode

def curve_primitive_quadrilateral(width=2.0, height=2.0, bottom_width=4.0, top_width=2.0, offset=1.0, bottom_height=3.0, top_height=1.0, point_1=[-1.0, -1.0, 0.0], point_2=[1.0, -1.0, 0.0], point_3=[1.0, 1.0, 0.0], point_4=[-1.0, 1.0, 0.0], mode='RECTANGLE'):
    node = ng.nodes.new("GeometryNodeCurvePrimitiveQuadrilateral")
    if isinstance(width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Width"], width)
    else:
        node.inputs["Width"] = width
    if isinstance(height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Height"], height)
    else:
        node.inputs["Height"] = height
    if isinstance(bottom_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Bottom Width"], bottom_width)
    else:
        node.inputs["Bottom Width"] = bottom_width
    if isinstance(top_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Top Width"], top_width)
    else:
        node.inputs["Top Width"] = top_width
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"] = offset
    if isinstance(bottom_height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Bottom Height"], bottom_height)
    else:
        node.inputs["Bottom Height"] = bottom_height
    if isinstance(top_height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Top Height"], top_height)
    else:
        node.inputs["Top Height"] = top_height
    if isinstance(point_1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 1"], point_1)
    else:
        node.inputs["Point 1"] = point_1
    if isinstance(point_2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 2"], point_2)
    else:
        node.inputs["Point 2"] = point_2
    if isinstance(point_3, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 3"], point_3)
    else:
        node.inputs["Point 3"] = point_3
    if isinstance(point_4, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point 4"], point_4)
    else:
        node.inputs["Point 4"] = point_4
    node.mode = mode

def curve_quadratic_bezier(resolution=None, start=[-1.0, 0.0, 0.0], middle=[0.0, 2.0, 0.0], end=[1.0, 0.0, 0.0], ):
    node = ng.nodes.new("GeometryNodeCurveQuadraticBezier")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"] = resolution
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start"], start)
    else:
        node.inputs["Start"] = start
    if isinstance(middle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Middle"], middle)
    else:
        node.inputs["Middle"] = middle
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End"], end)
    else:
        node.inputs["End"] = end

def curve_set_handles(curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
    node = ng.nodes.new("GeometryNodeCurveSetHandles")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    node.handle_type = handle_type
    node.mode = mode

def curve_spiral(resolution=None, rotations=2.0, start_radius=1.0, end_radius=2.0, height=2.0, reverse=None, ):
    node = ng.nodes.new("GeometryNodeCurveSpiral")
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"] = resolution
    if isinstance(rotations, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotations"], rotations)
    else:
        node.inputs["Rotations"] = rotations
    if isinstance(start_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Radius"], start_radius)
    else:
        node.inputs["Start Radius"] = start_radius
    if isinstance(end_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End Radius"], end_radius)
    else:
        node.inputs["End Radius"] = end_radius
    if isinstance(height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Height"], height)
    else:
        node.inputs["Height"] = height
    if isinstance(reverse, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Reverse"], reverse)
    else:
        node.inputs["Reverse"] = reverse

def curve_spline_type(curve=None, selection=None, spline_type='POLY'):
    node = ng.nodes.new("GeometryNodeCurveSplineType")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    node.spline_type = spline_type

def curve_star(points=None, inner_radius=1.0, outer_radius=2.0, twist=0.0, ):
    node = ng.nodes.new("GeometryNodeCurveStar")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"] = points
    if isinstance(inner_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Inner Radius"], inner_radius)
    else:
        node.inputs["Inner Radius"] = inner_radius
    if isinstance(outer_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Outer Radius"], outer_radius)
    else:
        node.inputs["Outer Radius"] = outer_radius
    if isinstance(twist, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Twist"], twist)
    else:
        node.inputs["Twist"] = twist

def curve_to_mesh(curve=None, profile_curve=None, fill_caps=None, ):
    node = ng.nodes.new("GeometryNodeCurveToMesh")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(profile_curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Profile Curve"], profile_curve)
    else:
        node.inputs["Profile Curve"] = profile_curve
    if isinstance(fill_caps, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Caps"], fill_caps)
    else:
        node.inputs["Fill Caps"] = fill_caps

def curve_to_points(curve=None, count=None, length=0.10000000149011612, mode='COUNT'):
    node = ng.nodes.new("GeometryNodeCurveToPoints")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"] = count
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length
    node.mode = mode

def deform_curves_on_surface(curves=None, ):
    node = ng.nodes.new("GeometryNodeDeformCurvesOnSurface")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"] = curves

def delete_geometry(geometry=None, selection=None, mode='ALL', domain='POINT'):
    node = ng.nodes.new("GeometryNodeDeleteGeometry")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    node.mode = mode
    node.domain = domain

def distribute_points_in_volume(volume=None, density=1.0, seed=None, spacing=[0.30000001192092896, 0.30000001192092896, 0.30000001192092896], threshold=0.10000000149011612, mode='DENSITY_RANDOM'):
    node = ng.nodes.new("GeometryNodeDistributePointsInVolume")
    if isinstance(volume, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Volume"], volume)
    else:
        node.inputs["Volume"] = volume
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"] = density
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"] = seed
    if isinstance(spacing, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Spacing"], spacing)
    else:
        node.inputs["Spacing"] = spacing
    if isinstance(threshold, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Threshold"], threshold)
    else:
        node.inputs["Threshold"] = threshold
    node.mode = mode

def distribute_points_on_faces(mesh=None, selection=None, distance_min=0.0, density_max=10.0, density=10.0, density_factor=1.0, seed=None, use_legacy_normal=False, distribute_method='RANDOM'):
    node = ng.nodes.new("GeometryNodeDistributePointsOnFaces")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(distance_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distance Min"], distance_min)
    else:
        node.inputs["Distance Min"] = distance_min
    if isinstance(density_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density Max"], density_max)
    else:
        node.inputs["Density Max"] = density_max
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"] = density
    if isinstance(density_factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density Factor"], density_factor)
    else:
        node.inputs["Density Factor"] = density_factor
    if isinstance(seed, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seed"], seed)
    else:
        node.inputs["Seed"] = seed
    node.use_legacy_normal = use_legacy_normal
    node.distribute_method = distribute_method

def dual_mesh(mesh=None, keep_boundaries=None, ):
    node = ng.nodes.new("GeometryNodeDualMesh")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(keep_boundaries, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Keep Boundaries"], keep_boundaries)
    else:
        node.inputs["Keep Boundaries"] = keep_boundaries

def duplicate_elements(geometry=None, selection=None, amount=None, domain='POINT'):
    node = ng.nodes.new("GeometryNodeDuplicateElements")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(amount, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Amount"], amount)
    else:
        node.inputs["Amount"] = amount
    node.domain = domain

def edge_paths_to_curves(mesh=None, start_vertices=None, next_vertex_index=None, ):
    node = ng.nodes.new("GeometryNodeEdgePathsToCurves")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(start_vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Vertices"], start_vertices)
    else:
        node.inputs["Start Vertices"] = start_vertices
    if isinstance(next_vertex_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Next Vertex Index"], next_vertex_index)
    else:
        node.inputs["Next Vertex Index"] = next_vertex_index

def edge_paths_to_selection(start_vertices=None, next_vertex_index=None, ):
    node = ng.nodes.new("GeometryNodeEdgePathsToSelection")
    if isinstance(start_vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Vertices"], start_vertices)
    else:
        node.inputs["Start Vertices"] = start_vertices
    if isinstance(next_vertex_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Next Vertex Index"], next_vertex_index)
    else:
        node.inputs["Next Vertex Index"] = next_vertex_index

def edges_of_corner(corner_index=None, ):
    node = ng.nodes.new("GeometryNodeEdgesOfCorner")
    if isinstance(corner_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Corner Index"], corner_index)
    else:
        node.inputs["Corner Index"] = corner_index

def edges_of_vertex(vertex_index=None, weights=0.0, sort_index=None, ):
    node = ng.nodes.new("GeometryNodeEdgesOfVertex")
    if isinstance(vertex_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertex Index"], vertex_index)
    else:
        node.inputs["Vertex Index"] = vertex_index
    if isinstance(weights, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weights"], weights)
    else:
        node.inputs["Weights"] = weights
    if isinstance(sort_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sort Index"], sort_index)
    else:
        node.inputs["Sort Index"] = sort_index

def edges_to_face_groups(boundary_edges=None, ):
    node = ng.nodes.new("GeometryNodeEdgesToFaceGroups")
    if isinstance(boundary_edges, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Boundary Edges"], boundary_edges)
    else:
        node.inputs["Boundary Edges"] = boundary_edges

def extrude_mesh(mesh=None, selection=None, offset=[0.0, 0.0, 0.0], offset_scale=1.0, individual=None, mode='FACES'):
    node = ng.nodes.new("GeometryNodeExtrudeMesh")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"] = offset
    if isinstance(offset_scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset Scale"], offset_scale)
    else:
        node.inputs["Offset Scale"] = offset_scale
    if isinstance(individual, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Individual"], individual)
    else:
        node.inputs["Individual"] = individual
    node.mode = mode

def face_of_corner(corner_index=None, ):
    node = ng.nodes.new("GeometryNodeFaceOfCorner")
    if isinstance(corner_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Corner Index"], corner_index)
    else:
        node.inputs["Corner Index"] = corner_index

def field_at_index_float(index=None, value=0.0, domain='POINT', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    node.domain = domain
    node.data_type = data_type

def field_at_index_int(index=None, value=0.0, domain='POINT', data_type='INT'):
    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    node.domain = domain
    node.data_type = data_type

def field_at_index_vector(index=None, value=0.0, domain='POINT', data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    node.domain = domain
    node.data_type = data_type

def field_at_index_color(index=None, value=0.0, domain='POINT', data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    node.domain = domain
    node.data_type = data_type

def field_at_index_boolean(index=None, value=0.0, domain='POINT', data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeFieldAtIndex")
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    node.domain = domain
    node.data_type = data_type

def field_on_domain_float(value=0.0, domain='POINT', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    node.domain = domain
    node.data_type = data_type

def field_on_domain_int(value=0.0, domain='POINT', data_type='INT'):
    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    node.domain = domain
    node.data_type = data_type

def field_on_domain_vector(value=0.0, domain='POINT', data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    node.domain = domain
    node.data_type = data_type

def field_on_domain_color(value=0.0, domain='POINT', data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    node.domain = domain
    node.data_type = data_type

def field_on_domain_boolean(value=0.0, domain='POINT', data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeFieldOnDomain")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    node.domain = domain
    node.data_type = data_type

def fill_curve(curve=None, mode='TRIANGLES'):
    node = ng.nodes.new("GeometryNodeFillCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    node.mode = mode

def fillet_curve(curve=None, count=None, radius=0.25, limit_radius=None, mode='BEZIER'):
    node = ng.nodes.new("GeometryNodeFilletCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"] = count
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius
    if isinstance(limit_radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Limit Radius"], limit_radius)
    else:
        node.inputs["Limit Radius"] = limit_radius
    node.mode = mode

def flip_faces(mesh=None, selection=None, ):
    node = ng.nodes.new("GeometryNodeFlipFaces")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection

def geometry_to_instance(geometry=None, ):
    node = ng.nodes.new("GeometryNodeGeometryToInstance")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry

def group(node_tree=None):
    node = ng.nodes.new("GeometryNodeGroup")
    node.node_tree = node_tree

def image_info(image=None, frame=None, ):
    node = ng.nodes.new("GeometryNodeImageInfo")
    if isinstance(image, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Image"], image)
    else:
        node.inputs["Image"] = image
    if isinstance(frame, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Frame"], frame)
    else:
        node.inputs["Frame"] = frame

def image_texture(image=None, vector=[0.0, 0.0, 0.0], frame=None, interpolation='Linear', extension='REPEAT'):
    node = ng.nodes.new("GeometryNodeImageTexture")
    if isinstance(image, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Image"], image)
    else:
        node.inputs["Image"] = image
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(frame, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Frame"], frame)
    else:
        node.inputs["Frame"] = frame
    node.interpolation = interpolation
    node.extension = extension

def input_curve_handle_positions(relative=None, ):
    node = ng.nodes.new("GeometryNodeInputCurveHandlePositions")
    if isinstance(relative, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Relative"], relative)
    else:
        node.inputs["Relative"] = relative

def input_curve_tilt():
    node = ng.nodes.new("GeometryNodeInputCurveTilt")

def input_id():
    node = ng.nodes.new("GeometryNodeInputID")

def input_image(image=None):
    node = ng.nodes.new("GeometryNodeInputImage")
    node.image = image

def input_index():
    node = ng.nodes.new("GeometryNodeInputIndex")

def input_instance_rotation():
    node = ng.nodes.new("GeometryNodeInputInstanceRotation")

def input_instance_scale():
    node = ng.nodes.new("GeometryNodeInputInstanceScale")

def input_material(material=None):
    node = ng.nodes.new("GeometryNodeInputMaterial")
    node.material = material

def input_material_index():
    node = ng.nodes.new("GeometryNodeInputMaterialIndex")

def input_mesh_edge_angle():
    node = ng.nodes.new("GeometryNodeInputMeshEdgeAngle")

def input_mesh_edge_neighbors():
    node = ng.nodes.new("GeometryNodeInputMeshEdgeNeighbors")

def input_mesh_edge_vertices():
    node = ng.nodes.new("GeometryNodeInputMeshEdgeVertices")

def input_mesh_face_area():
    node = ng.nodes.new("GeometryNodeInputMeshFaceArea")

def input_mesh_face_is_planar(threshold=0.009999999776482582, ):
    node = ng.nodes.new("GeometryNodeInputMeshFaceIsPlanar")
    if isinstance(threshold, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Threshold"], threshold)
    else:
        node.inputs["Threshold"] = threshold

def input_mesh_face_neighbors():
    node = ng.nodes.new("GeometryNodeInputMeshFaceNeighbors")

def input_mesh_island():
    node = ng.nodes.new("GeometryNodeInputMeshIsland")

def input_mesh_vertex_neighbors():
    node = ng.nodes.new("GeometryNodeInputMeshVertexNeighbors")

def input_named_attribute(name=None, data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeInputNamedAttribute")
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"] = name
    node.data_type = data_type

def input_normal():
    node = ng.nodes.new("GeometryNodeInputNormal")

def input_position():
    node = ng.nodes.new("GeometryNodeInputPosition")

def input_radius():
    node = ng.nodes.new("GeometryNodeInputRadius")

def input_scene_time():
    node = ng.nodes.new("GeometryNodeInputSceneTime")

def input_shade_smooth():
    node = ng.nodes.new("GeometryNodeInputShadeSmooth")

def input_shortest_edge_paths(end_vertex=None, edge_cost=1.0, ):
    node = ng.nodes.new("GeometryNodeInputShortestEdgePaths")
    if isinstance(end_vertex, bpy.types.NodeSocket):
        ng.links.new(node.inputs["End Vertex"], end_vertex)
    else:
        node.inputs["End Vertex"] = end_vertex
    if isinstance(edge_cost, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Edge Cost"], edge_cost)
    else:
        node.inputs["Edge Cost"] = edge_cost

def input_spline_cyclic():
    node = ng.nodes.new("GeometryNodeInputSplineCyclic")

def input_spline_resolution():
    node = ng.nodes.new("GeometryNodeInputSplineResolution")

def input_tangent():
    node = ng.nodes.new("GeometryNodeInputTangent")

def instance_on_points(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=[0.0, 0.0, 0.0], scale=[1.0, 1.0, 1.0], ):
    node = ng.nodes.new("GeometryNodeInstanceOnPoints")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"] = points
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(instance, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instance"], instance)
    else:
        node.inputs["Instance"] = instance
    if isinstance(pick_instance, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Pick Instance"], pick_instance)
    else:
        node.inputs["Pick Instance"] = pick_instance
    if isinstance(instance_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instance Index"], instance_index)
    else:
        node.inputs["Instance Index"] = instance_index
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"] = rotation
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale

def instances_to_points(instances=None, selection=None, position=[0.0, 0.0, 0.0], radius=0.05000000074505806, ):
    node = ng.nodes.new("GeometryNodeInstancesToPoints")
    if isinstance(instances, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instances"], instances)
    else:
        node.inputs["Instances"] = instances
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"] = position
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius

def interpolate_curves(guide_curves=None, guide_up=[0.0, 0.0, 0.0], guide_group_id=None, points=None, point_up=[0.0, 0.0, 0.0], point_group_id=None, max_neighbors=None, ):
    node = ng.nodes.new("GeometryNodeInterpolateCurves")
    if isinstance(guide_curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Guide Curves"], guide_curves)
    else:
        node.inputs["Guide Curves"] = guide_curves
    if isinstance(guide_up, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Guide Up"], guide_up)
    else:
        node.inputs["Guide Up"] = guide_up
    if isinstance(guide_group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Guide Group ID"], guide_group_id)
    else:
        node.inputs["Guide Group ID"] = guide_group_id
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"] = points
    if isinstance(point_up, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point Up"], point_up)
    else:
        node.inputs["Point Up"] = point_up
    if isinstance(point_group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point Group ID"], point_group_id)
    else:
        node.inputs["Point Group ID"] = point_group_id
    if isinstance(max_neighbors, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Max Neighbors"], max_neighbors)
    else:
        node.inputs["Max Neighbors"] = max_neighbors

def is_viewport():
    node = ng.nodes.new("GeometryNodeIsViewport")

def join_geometry(geometry=None, ):
    node = ng.nodes.new("GeometryNodeJoinGeometry")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry

def material_selection(material=None, ):
    node = ng.nodes.new("GeometryNodeMaterialSelection")
    if isinstance(material, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Material"], material)
    else:
        node.inputs["Material"] = material

def merge_by_distance(geometry=None, selection=None, distance=0.0010000000474974513, mode='ALL'):
    node = ng.nodes.new("GeometryNodeMergeByDistance")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(distance, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distance"], distance)
    else:
        node.inputs["Distance"] = distance
    node.mode = mode

def mesh_boolean(mesh_1=None, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE'):
    node = ng.nodes.new("GeometryNodeMeshBoolean")
    if isinstance(mesh_1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh 1"], mesh_1)
    else:
        node.inputs["Mesh 1"] = mesh_1
    if isinstance(mesh_2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh 2"], mesh_2)
    else:
        node.inputs["Mesh 2"] = mesh_2
    if isinstance(self_intersection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Self Intersection"], self_intersection)
    else:
        node.inputs["Self Intersection"] = self_intersection
    if isinstance(hole_tolerant, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Hole Tolerant"], hole_tolerant)
    else:
        node.inputs["Hole Tolerant"] = hole_tolerant
    node.operation = operation

def mesh_circle(vertices=None, radius=1.0, fill_type='NONE'):
    node = ng.nodes.new("GeometryNodeMeshCircle")
    if isinstance(vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices"], vertices)
    else:
        node.inputs["Vertices"] = vertices
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius
    node.fill_type = fill_type

def mesh_cone(vertices=None, side_segments=None, fill_segments=None, radius_top=0.0, radius_bottom=1.0, depth=2.0, fill_type='NGON'):
    node = ng.nodes.new("GeometryNodeMeshCone")
    if isinstance(vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices"], vertices)
    else:
        node.inputs["Vertices"] = vertices
    if isinstance(side_segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Side Segments"], side_segments)
    else:
        node.inputs["Side Segments"] = side_segments
    if isinstance(fill_segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Segments"], fill_segments)
    else:
        node.inputs["Fill Segments"] = fill_segments
    if isinstance(radius_top, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius Top"], radius_top)
    else:
        node.inputs["Radius Top"] = radius_top
    if isinstance(radius_bottom, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius Bottom"], radius_bottom)
    else:
        node.inputs["Radius Bottom"] = radius_bottom
    if isinstance(depth, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Depth"], depth)
    else:
        node.inputs["Depth"] = depth
    node.fill_type = fill_type

def mesh_cube(size=[1.0, 1.0, 1.0], vertices_x=None, vertices_y=None, vertices_z=None, ):
    node = ng.nodes.new("GeometryNodeMeshCube")
    if isinstance(size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Size"], size)
    else:
        node.inputs["Size"] = size
    if isinstance(vertices_x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices X"], vertices_x)
    else:
        node.inputs["Vertices X"] = vertices_x
    if isinstance(vertices_y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices Y"], vertices_y)
    else:
        node.inputs["Vertices Y"] = vertices_y
    if isinstance(vertices_z, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices Z"], vertices_z)
    else:
        node.inputs["Vertices Z"] = vertices_z

def mesh_cylinder(vertices=None, side_segments=None, fill_segments=None, radius=1.0, depth=2.0, fill_type='NGON'):
    node = ng.nodes.new("GeometryNodeMeshCylinder")
    if isinstance(vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices"], vertices)
    else:
        node.inputs["Vertices"] = vertices
    if isinstance(side_segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Side Segments"], side_segments)
    else:
        node.inputs["Side Segments"] = side_segments
    if isinstance(fill_segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Segments"], fill_segments)
    else:
        node.inputs["Fill Segments"] = fill_segments
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius
    if isinstance(depth, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Depth"], depth)
    else:
        node.inputs["Depth"] = depth
    node.fill_type = fill_type

def mesh_face_set_boundaries(face_group_id=None, ):
    node = ng.nodes.new("GeometryNodeMeshFaceSetBoundaries")
    if isinstance(face_group_id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Face Group ID"], face_group_id)
    else:
        node.inputs["Face Group ID"] = face_group_id

def mesh_grid(size_x=1.0, size_y=1.0, vertices_x=None, vertices_y=None, ):
    node = ng.nodes.new("GeometryNodeMeshGrid")
    if isinstance(size_x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Size X"], size_x)
    else:
        node.inputs["Size X"] = size_x
    if isinstance(size_y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Size Y"], size_y)
    else:
        node.inputs["Size Y"] = size_y
    if isinstance(vertices_x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices X"], vertices_x)
    else:
        node.inputs["Vertices X"] = vertices_x
    if isinstance(vertices_y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertices Y"], vertices_y)
    else:
        node.inputs["Vertices Y"] = vertices_y

def mesh_ico_sphere(radius=1.0, subdivisions=None, ):
    node = ng.nodes.new("GeometryNodeMeshIcoSphere")
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius
    if isinstance(subdivisions, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Subdivisions"], subdivisions)
    else:
        node.inputs["Subdivisions"] = subdivisions

def mesh_line(count=None, resolution=1.0, start_location=[0.0, 0.0, 0.0], offset=[0.0, 0.0, 1.0], mode='OFFSET', count_mode='TOTAL'):
    node = ng.nodes.new("GeometryNodeMeshLine")
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"] = count
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"] = resolution
    if isinstance(start_location, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Start Location"], start_location)
    else:
        node.inputs["Start Location"] = start_location
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"] = offset
    node.mode = mode
    node.count_mode = count_mode

def mesh_to_curve(mesh=None, selection=None, ):
    node = ng.nodes.new("GeometryNodeMeshToCurve")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection

def mesh_to_points(mesh=None, selection=None, position=[0.0, 0.0, 0.0], radius=0.05000000074505806, mode='VERTICES'):
    node = ng.nodes.new("GeometryNodeMeshToPoints")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"] = position
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius
    node.mode = mode

def mesh_to_volume(mesh=None, density=1.0, voxel_size=0.30000001192092896, voxel_amount=64.0, exterior_band_width=0.10000000149011612, interior_band_width=0.0, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):
    node = ng.nodes.new("GeometryNodeMeshToVolume")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"] = density
    if isinstance(voxel_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Size"], voxel_size)
    else:
        node.inputs["Voxel Size"] = voxel_size
    if isinstance(voxel_amount, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Amount"], voxel_amount)
    else:
        node.inputs["Voxel Amount"] = voxel_amount
    if isinstance(exterior_band_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Exterior Band Width"], exterior_band_width)
    else:
        node.inputs["Exterior Band Width"] = exterior_band_width
    if isinstance(interior_band_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Interior Band Width"], interior_band_width)
    else:
        node.inputs["Interior Band Width"] = interior_band_width
    if isinstance(fill_volume, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Volume"], fill_volume)
    else:
        node.inputs["Fill Volume"] = fill_volume
    node.resolution_mode = resolution_mode

def mesh_uv_sphere(segments=None, rings=None, radius=1.0, ):
    node = ng.nodes.new("GeometryNodeMeshUVSphere")
    if isinstance(segments, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Segments"], segments)
    else:
        node.inputs["Segments"] = segments
    if isinstance(rings, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rings"], rings)
    else:
        node.inputs["Rings"] = rings
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius

def object_info(object=None, as_instance=None, transform_space='ORIGINAL'):
    node = ng.nodes.new("GeometryNodeObjectInfo")
    if isinstance(object, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Object"], object)
    else:
        node.inputs["Object"] = object
    if isinstance(as_instance, bpy.types.NodeSocket):
        ng.links.new(node.inputs["As Instance"], as_instance)
    else:
        node.inputs["As Instance"] = as_instance
    node.transform_space = transform_space

def offset_corner_in_face(corner_index=None, offset=None, ):
    node = ng.nodes.new("GeometryNodeOffsetCornerInFace")
    if isinstance(corner_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Corner Index"], corner_index)
    else:
        node.inputs["Corner Index"] = corner_index
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"] = offset

def offset_point_in_curve(point_index=None, offset=None, ):
    node = ng.nodes.new("GeometryNodeOffsetPointInCurve")
    if isinstance(point_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Point Index"], point_index)
    else:
        node.inputs["Point Index"] = point_index
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"] = offset

def points(count=None, position=[0.0, 0.0, 0.0], radius=0.10000000149011612, ):
    node = ng.nodes.new("GeometryNodePoints")
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"] = count
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"] = position
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius

def points_of_curve(curve_index=None, weights=0.0, sort_index=None, ):
    node = ng.nodes.new("GeometryNodePointsOfCurve")
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"] = curve_index
    if isinstance(weights, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Weights"], weights)
    else:
        node.inputs["Weights"] = weights
    if isinstance(sort_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sort Index"], sort_index)
    else:
        node.inputs["Sort Index"] = sort_index

def points_to_vertices(points=None, selection=None, ):
    node = ng.nodes.new("GeometryNodePointsToVertices")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"] = points
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection

def points_to_volume(points=None, density=1.0, voxel_size=0.30000001192092896, voxel_amount=64.0, radius=0.5, resolution_mode='VOXEL_AMOUNT'):
    node = ng.nodes.new("GeometryNodePointsToVolume")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"] = points
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"] = density
    if isinstance(voxel_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Size"], voxel_size)
    else:
        node.inputs["Voxel Size"] = voxel_size
    if isinstance(voxel_amount, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Amount"], voxel_amount)
    else:
        node.inputs["Voxel Amount"] = voxel_amount
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius
    node.resolution_mode = resolution_mode

def proximity(target=None, source_position=[0.0, 0.0, 0.0], target_element='FACES'):
    node = ng.nodes.new("GeometryNodeProximity")
    if isinstance(target, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target"], target)
    else:
        node.inputs["Target"] = target
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"] = source_position
    node.target_element = target_element

def raycast_float(target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"] = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], attribute)
    else:
        node.inputs[0] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"] = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"] = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"] = ray_length
    node.mapping = mapping
    node.data_type = data_type

def raycast_int(target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='INT'):
    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"] = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], attribute)
    else:
        node.inputs[1] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"] = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"] = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"] = ray_length
    node.mapping = mapping
    node.data_type = data_type

def raycast_vector(target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"] = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], attribute)
    else:
        node.inputs[2] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"] = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"] = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"] = ray_length
    node.mapping = mapping
    node.data_type = data_type

def raycast_color(target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"] = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], attribute)
    else:
        node.inputs[3] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"] = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"] = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"] = ray_length
    node.mapping = mapping
    node.data_type = data_type

def raycast_boolean(target_geometry=None, attribute=[0.0, 0.0, 0.0], source_position=[0.0, 0.0, 0.0], ray_direction=[0.0, 0.0, -1.0], ray_length=100.0, mapping='INTERPOLATED', data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeRaycast")
    if isinstance(target_geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Target Geometry"], target_geometry)
    else:
        node.inputs["Target Geometry"] = target_geometry
    if isinstance(attribute, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], attribute)
    else:
        node.inputs[4] = attribute
    if isinstance(source_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source Position"], source_position)
    else:
        node.inputs["Source Position"] = source_position
    if isinstance(ray_direction, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Direction"], ray_direction)
    else:
        node.inputs["Ray Direction"] = ray_direction
    if isinstance(ray_length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Ray Length"], ray_length)
    else:
        node.inputs["Ray Length"] = ray_length
    node.mapping = mapping
    node.data_type = data_type

def realize_instances(geometry=None, legacy_behavior=False):
    node = ng.nodes.new("GeometryNodeRealizeInstances")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    node.legacy_behavior = legacy_behavior

def remove_attribute(geometry=None, name=None, ):
    node = ng.nodes.new("GeometryNodeRemoveAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"] = name

def replace_material(geometry=None, old=None, new=None, ):
    node = ng.nodes.new("GeometryNodeReplaceMaterial")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(old, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Old"], old)
    else:
        node.inputs["Old"] = old
    if isinstance(new, bpy.types.NodeSocket):
        ng.links.new(node.inputs["New"], new)
    else:
        node.inputs["New"] = new

def resample_curve(curve=None, selection=None, count=None, length=0.10000000149011612, mode='COUNT'):
    node = ng.nodes.new("GeometryNodeResampleCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(count, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Count"], count)
    else:
        node.inputs["Count"] = count
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length
    node.mode = mode

def reverse_curve(curve=None, selection=None, ):
    node = ng.nodes.new("GeometryNodeReverseCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection

def rotate_instances(instances=None, selection=None, rotation=[0.0, 0.0, 0.0], pivot_point=[0.0, 0.0, 0.0], local_space=None, ):
    node = ng.nodes.new("GeometryNodeRotateInstances")
    if isinstance(instances, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instances"], instances)
    else:
        node.inputs["Instances"] = instances
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"] = rotation
    if isinstance(pivot_point, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Pivot Point"], pivot_point)
    else:
        node.inputs["Pivot Point"] = pivot_point
    if isinstance(local_space, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Local Space"], local_space)
    else:
        node.inputs["Local Space"] = local_space

def sample_curve_float(curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"] = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"] = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type

def sample_curve_int(curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='INT'):
    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"] = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"] = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type

def sample_curve_vector(curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"] = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"] = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type

def sample_curve_color(curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"] = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"] = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type

def sample_curve_boolean(curves=None, value=0.0, factor=0.0, length=0.0, curve_index=None, mode='FACTOR', use_all_curves=False, data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeSampleCurve")
    if isinstance(curves, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curves"], curves)
    else:
        node.inputs["Curves"] = curves
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(length, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Length"], length)
    else:
        node.inputs["Length"] = length
    if isinstance(curve_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve Index"], curve_index)
    else:
        node.inputs["Curve Index"] = curve_index
    node.mode = mode
    node.use_all_curves = use_all_curves
    node.data_type = data_type

def sample_index_float(geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type

def sample_index_int(geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='INT'):
    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type

def sample_index_vector(geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type

def sample_index_color(geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type

def sample_index_boolean(geometry=None, value=0.0, index=None, clamp=False, domain='POINT', data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeSampleIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    if isinstance(index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Index"], index)
    else:
        node.inputs["Index"] = index
    node.clamp = clamp
    node.domain = domain
    node.data_type = data_type

def sample_nearest(geometry=None, sample_position=[0.0, 0.0, 0.0], domain='POINT'):
    node = ng.nodes.new("GeometryNodeSampleNearest")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"] = sample_position
    node.domain = domain

def sample_nearest_surface_float(mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"] = sample_position
    node.data_type = data_type

def sample_nearest_surface_int(mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='INT'):
    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"] = sample_position
    node.data_type = data_type

def sample_nearest_surface_vector(mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"] = sample_position
    node.data_type = data_type

def sample_nearest_surface_color(mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"] = sample_position
    node.data_type = data_type

def sample_nearest_surface_boolean(mesh=None, value=0.0, sample_position=[0.0, 0.0, 0.0], data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeSampleNearestSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    if isinstance(sample_position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample Position"], sample_position)
    else:
        node.inputs["Sample Position"] = sample_position
    node.data_type = data_type

def sample_uv_surface_float(mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"] = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"] = sample_uv
    node.data_type = data_type

def sample_uv_surface_int(mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='INT'):
    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"] = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"] = sample_uv
    node.data_type = data_type

def sample_uv_surface_vector(mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"] = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"] = sample_uv
    node.data_type = data_type

def sample_uv_surface_color(mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"] = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"] = sample_uv
    node.data_type = data_type

def sample_uv_surface_boolean(mesh=None, value=0.0, source_uv_map=[0.0, 0.0, 0.0], sample_uv=[0.0, 0.0, 0.0], data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeSampleUVSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    if isinstance(source_uv_map, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Source UV Map"], source_uv_map)
    else:
        node.inputs["Source UV Map"] = source_uv_map
    if isinstance(sample_uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Sample UV"], sample_uv)
    else:
        node.inputs["Sample UV"] = sample_uv
    node.data_type = data_type

def scale_elements(geometry=None, selection=None, scale=1.0, center=[0.0, 0.0, 0.0], axis=[1.0, 0.0, 0.0], scale_mode='UNIFORM', domain='FACE'):
    node = ng.nodes.new("GeometryNodeScaleElements")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    if isinstance(center, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Center"], center)
    else:
        node.inputs["Center"] = center
    if isinstance(axis, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Axis"], axis)
    else:
        node.inputs["Axis"] = axis
    node.scale_mode = scale_mode
    node.domain = domain

def scale_instances(instances=None, selection=None, scale=[1.0, 1.0, 1.0], center=[0.0, 0.0, 0.0], local_space=None, ):
    node = ng.nodes.new("GeometryNodeScaleInstances")
    if isinstance(instances, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instances"], instances)
    else:
        node.inputs["Instances"] = instances
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    if isinstance(center, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Center"], center)
    else:
        node.inputs["Center"] = center
    if isinstance(local_space, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Local Space"], local_space)
    else:
        node.inputs["Local Space"] = local_space

def self_object():
    node = ng.nodes.new("GeometryNodeSelfObject")

def separate_components(geometry=None, ):
    node = ng.nodes.new("GeometryNodeSeparateComponents")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry

def separate_geometry(geometry=None, selection=None, domain='POINT'):
    node = ng.nodes.new("GeometryNodeSeparateGeometry")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    node.domain = domain

def set_curve_handle_positions(curve=None, selection=None, position=[0.0, 0.0, 0.0], offset=[0.0, 0.0, 0.0], mode='LEFT'):
    node = ng.nodes.new("GeometryNodeSetCurveHandlePositions")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"] = position
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"] = offset
    node.mode = mode

def set_curve_normal(curve=None, selection=None, mode='MINIMUM_TWIST'):
    node = ng.nodes.new("GeometryNodeSetCurveNormal")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    node.mode = mode

def set_curve_radius(curve=None, selection=None, radius=0.004999999888241291, ):
    node = ng.nodes.new("GeometryNodeSetCurveRadius")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius

def set_curve_tilt(curve=None, selection=None, tilt=0.0, ):
    node = ng.nodes.new("GeometryNodeSetCurveTilt")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(tilt, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Tilt"], tilt)
    else:
        node.inputs["Tilt"] = tilt

def set_id(geometry=None, selection=None, id=None, ):
    node = ng.nodes.new("GeometryNodeSetID")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(id, bpy.types.NodeSocket):
        ng.links.new(node.inputs["ID"], id)
    else:
        node.inputs["ID"] = id

def set_material(geometry=None, selection=None, material=None, ):
    node = ng.nodes.new("GeometryNodeSetMaterial")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(material, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Material"], material)
    else:
        node.inputs["Material"] = material

def set_material_index(geometry=None, selection=None, material_index=None, ):
    node = ng.nodes.new("GeometryNodeSetMaterialIndex")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(material_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Material Index"], material_index)
    else:
        node.inputs["Material Index"] = material_index

def set_point_radius(points=None, selection=None, radius=0.05000000074505806, ):
    node = ng.nodes.new("GeometryNodeSetPointRadius")
    if isinstance(points, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Points"], points)
    else:
        node.inputs["Points"] = points
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(radius, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Radius"], radius)
    else:
        node.inputs["Radius"] = radius

def set_position(geometry=None, selection=None, position=[0.0, 0.0, 0.0], offset=[0.0, 0.0, 0.0], ):
    node = ng.nodes.new("GeometryNodeSetPosition")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(position, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Position"], position)
    else:
        node.inputs["Position"] = position
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"] = offset

def set_shade_smooth(geometry=None, selection=None, shade_smooth=None, ):
    node = ng.nodes.new("GeometryNodeSetShadeSmooth")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(shade_smooth, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Shade Smooth"], shade_smooth)
    else:
        node.inputs["Shade Smooth"] = shade_smooth

def set_spline_cyclic(geometry=None, selection=None, cyclic=None, ):
    node = ng.nodes.new("GeometryNodeSetSplineCyclic")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(cyclic, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Cyclic"], cyclic)
    else:
        node.inputs["Cyclic"] = cyclic

def set_spline_resolution(geometry=None, selection=None, resolution=None, ):
    node = ng.nodes.new("GeometryNodeSetSplineResolution")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(resolution, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution"], resolution)
    else:
        node.inputs["Resolution"] = resolution

def spline_length():
    node = ng.nodes.new("GeometryNodeSplineLength")

def spline_parameter():
    node = ng.nodes.new("GeometryNodeSplineParameter")

def split_edges(mesh=None, selection=None, ):
    node = ng.nodes.new("GeometryNodeSplitEdges")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection

def store_named_attribute_float(geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"] = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[0], value)
    else:
        node.inputs[0] = value
    node.domain = domain
    node.data_type = data_type

def store_named_attribute_int(geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='INT'):
    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"] = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[1], value)
    else:
        node.inputs[1] = value
    node.domain = domain
    node.data_type = data_type

def store_named_attribute_vector(geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='VECTOR_FLOAT'):
    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"] = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[2], value)
    else:
        node.inputs[2] = value
    node.domain = domain
    node.data_type = data_type

def store_named_attribute_color(geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='COLOR'):
    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"] = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[3], value)
    else:
        node.inputs[3] = value
    node.domain = domain
    node.data_type = data_type

def store_named_attribute_boolean(geometry=None, selection=None, name=None, value=[0.0, 0.0, 0.0], domain='POINT', data_type='BOOLEAN'):
    node = ng.nodes.new("GeometryNodeStoreNamedAttribute")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(name, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Name"], name)
    else:
        node.inputs["Name"] = name
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs[4], value)
    else:
        node.inputs[4] = value
    node.domain = domain
    node.data_type = data_type

def string_join(delimiter=None, strings=None):
    node = ng.nodes.new("GeometryNodeStringJoin")
    if isinstance(delimiter, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Delimiter"], delimiter)
    else:
        node.inputs["Delimiter"] = delimiter
    if isinstance(strings, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Strings"], strings)
    else:
        node.inputs["Strings"] = strings

def string_to_curves(string=None, size=1.0, character_spacing=1.0, word_spacing=1.0, line_spacing=1.0, text_box_width=0.0, text_box_height=0.0, align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT', overflow='OVERFLOW', font=bpy.data.fonts['BFont Regular'], align_x='LEFT'):
    node = ng.nodes.new("GeometryNodeStringToCurves")
    if isinstance(string, bpy.types.NodeSocket):
        ng.links.new(node.inputs["String"], string)
    else:
        node.inputs["String"] = string
    if isinstance(size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Size"], size)
    else:
        node.inputs["Size"] = size
    if isinstance(character_spacing, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Character Spacing"], character_spacing)
    else:
        node.inputs["Character Spacing"] = character_spacing
    if isinstance(word_spacing, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Word Spacing"], word_spacing)
    else:
        node.inputs["Word Spacing"] = word_spacing
    if isinstance(line_spacing, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Line Spacing"], line_spacing)
    else:
        node.inputs["Line Spacing"] = line_spacing
    if isinstance(text_box_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Text Box Width"], text_box_width)
    else:
        node.inputs["Text Box Width"] = text_box_width
    if isinstance(text_box_height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Text Box Height"], text_box_height)
    else:
        node.inputs["Text Box Height"] = text_box_height
    node.align_y = align_y
    node.pivot_mode = pivot_mode
    node.overflow = overflow
    node.font = font
    node.align_x = align_x

def subdivide_curve(curve=None, cuts=None):
    node = ng.nodes.new("GeometryNodeSubdivideCurve")
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(cuts, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Cuts"], cuts)
    else:
        node.inputs["Cuts"] = cuts

def subdivide_mesh(mesh=None, level=None):
    node = ng.nodes.new("GeometryNodeSubdivideMesh")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(level, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Level"], level)
    else:
        node.inputs["Level"] = level

def subdivision_surface(mesh=None, level=None, edge_crease=0.0, vertex_crease=0.0, uv_smooth='PRESERVE_BOUNDARIES', boundary_smooth='ALL'):
    node = ng.nodes.new("GeometryNodeSubdivisionSurface")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(level, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Level"], level)
    else:
        node.inputs["Level"] = level
    if isinstance(edge_crease, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Edge Crease"], edge_crease)
    else:
        node.inputs["Edge Crease"] = edge_crease
    if isinstance(vertex_crease, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vertex Crease"], vertex_crease)
    else:
        node.inputs["Vertex Crease"] = vertex_crease
    node.uv_smooth = uv_smooth
    node.boundary_smooth = boundary_smooth

def switch_float(switch=False, false=0.0, true=0.0, input_type='FLOAT'):
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

def switch_int(switch=False, false=0.0, true=0.0, input_type='INT'):
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

def switch_boolean(switch=False, false=0.0, true=0.0, input_type='BOOLEAN'):
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

def switch_vector(switch=False, false=0.0, true=0.0, input_type='VECTOR'):
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

def switch_color(switch=False, false=0.0, true=0.0, input_type='RGBA'):
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

def switch_string(switch=False, false=0.0, true=0.0, input_type='STRING'):
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

def switch_geometry(switch=False, false=0.0, true=0.0, input_type='GEOMETRY'):
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

def switch_object(switch=False, false=0.0, true=0.0, input_type='OBJECT'):
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

def switch_collection(switch=False, false=0.0, true=0.0, input_type='COLLECTION'):
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

def switch_texture(switch=False, false=0.0, true=0.0, input_type='TEXTURE'):
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

def switch_material(switch=False, false=0.0, true=0.0, input_type='MATERIAL'):
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


def switch_image(switch=False, false=0.0, true=0.0, input_type='IMAGE'):
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


def transform(geometry=None, translation=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0], scale=[1.0, 1.0, 1.0], ):
    node = ng.nodes.new("GeometryNodeTransform")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(translation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Translation"], translation)
    else:
        node.inputs["Translation"] = translation
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"] = rotation
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale

def translate_instances(instances=None, selection=None, translation=[0.0, 0.0, 0.0], local_space=None, ):
    node = ng.nodes.new("GeometryNodeTranslateInstances")
    if isinstance(instances, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Instances"], instances)
    else:
        node.inputs["Instances"] = instances
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(translation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Translation"], translation)
    else:
        node.inputs["Translation"] = translation
    if isinstance(local_space, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Local Space"], local_space)
    else:
        node.inputs["Local Space"] = local_space

def triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
    node = ng.nodes.new("GeometryNodeTriangulate")
    if isinstance(mesh, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mesh"], mesh)
    else:
        node.inputs["Mesh"] = mesh
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(minimum_vertices, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Minimum Vertices"], minimum_vertices)
    else:
        node.inputs["Minimum Vertices"] = minimum_vertices
    node.ngon_method = ngon_method
    node.quad_method = quad_method

def trim_curve(curve=None, selection=None, start=0.0, end=1.0, mode='FACTOR'):
    node = ng.nodes.new("GeometryNodeTrimCurve")
    if mode == 'FACTOR':
        start_ind, end_ind = 1, 2
    else:
        start_ind, end_ind = 3, 4
    if isinstance(curve, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Curve"], curve)
    else:
        node.inputs["Curve"] = curve
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(start, bpy.types.NodeSocket):
        ng.links.new(node.inputs[start_ind], start)
    else:
        node.inputs[start_ind] = start
    if isinstance(end, bpy.types.NodeSocket):
        ng.links.new(node.inputs[end_ind], end)
    else:
        node.inputs[end_ind] = end
    node.mode = mode

def uv_pack_islands(uv=[0.0, 0.0, 0.0], selection=None, margin=0.0010000000474974513, rotate=None, ):
    node = ng.nodes.new("GeometryNodeUVPackIslands")
    if isinstance(uv, bpy.types.NodeSocket):
        ng.links.new(node.inputs["UV"], uv)
    else:
        node.inputs["UV"] = uv
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(margin, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Margin"], margin)
    else:
        node.inputs["Margin"] = margin
    if isinstance(rotate, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotate"], rotate)
    else:
        node.inputs["Rotate"] = rotate

def uv_unwrap(selection=None, seam=None, margin=0.0010000000474974513, fill_holes=None, method='ANGLE_BASED'):
    node = ng.nodes.new("GeometryNodeUVUnwrap")
    if isinstance(selection, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Selection"], selection)
    else:
        node.inputs["Selection"] = selection
    if isinstance(seam, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Seam"], seam)
    else:
        node.inputs["Seam"] = seam
    if isinstance(margin, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Margin"], margin)
    else:
        node.inputs["Margin"] = margin
    if isinstance(fill_holes, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fill Holes"], fill_holes)
    else:
        node.inputs["Fill Holes"] = fill_holes
    node.method = method

def vertex_of_corner(corner_index=None, ):
    node = ng.nodes.new("GeometryNodeVertexOfCorner")
    if isinstance(corner_index, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Corner Index"], corner_index)
    else:
        node.inputs["Corner Index"] = corner_index

def viewer(geometry=None, value=0.0, value=0.0, value=0.0, value=0.0, value=0.0, domain='AUTO', data_type='FLOAT'):
    node = ng.nodes.new("GeometryNodeViewer")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    node.domain = domain
    node.data_type = data_type

def volume_cube(density=1.0, background=0.0, min=[-1.0, -1.0, -1.0], max=[1.0, 1.0, 1.0], resolution_x=None, resolution_y=None, resolution_z=None, ):
    node = ng.nodes.new("GeometryNodeVolumeCube")
    if isinstance(density, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Density"], density)
    else:
        node.inputs["Density"] = density
    if isinstance(background, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Background"], background)
    else:
        node.inputs["Background"] = background
    if isinstance(min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Min"], min)
    else:
        node.inputs["Min"] = min
    if isinstance(max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Max"], max)
    else:
        node.inputs["Max"] = max
    if isinstance(resolution_x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution X"], resolution_x)
    else:
        node.inputs["Resolution X"] = resolution_x
    if isinstance(resolution_y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution Y"], resolution_y)
    else:
        node.inputs["Resolution Y"] = resolution_y
    if isinstance(resolution_z, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Resolution Z"], resolution_z)
    else:
        node.inputs["Resolution Z"] = resolution_z

def volume_to_mesh(volume=None, voxel_size=0.30000001192092896, voxel_amount=64.0, threshold=0.10000000149011612, adaptivity=0.0, resolution_mode='GRID'):
    node = ng.nodes.new("GeometryNodeVolumeToMesh")
    if isinstance(volume, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Volume"], volume)
    else:
        node.inputs["Volume"] = volume
    if isinstance(voxel_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Size"], voxel_size)
    else:
        node.inputs["Voxel Size"] = voxel_size
    if isinstance(voxel_amount, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Voxel Amount"], voxel_amount)
    else:
        node.inputs["Voxel Amount"] = voxel_amount
    if isinstance(threshold, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Threshold"], threshold)
    else:
        node.inputs["Threshold"] = threshold
    if isinstance(adaptivity, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Adaptivity"], adaptivity)
    else:
        node.inputs["Adaptivity"] = adaptivity
    node.resolution_mode = resolution_mode

def frame(shrink=True, text=None, label_size=20):
    node = ng.nodes.new("NodeFrame")
    node.shrink = shrink
    node.text = text
    node.label_size = label_size

def group_input():
    node = ng.nodes.new("NodeGroupInput")

def group_output(geometry=None, is_active_output=True):
    node = ng.nodes.new("NodeGroupOutput")
    if isinstance(geometry, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Geometry"], geometry)
    else:
        node.inputs["Geometry"] = geometry
    node.is_active_output = is_active_output

def reroute(input=None, ):
    node = ng.nodes.new("NodeReroute")
    if isinstance(input, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Input"], input)
    else:
        node.inputs["Input"] = input

def clamp(value=1.0, min=0.0, max=1.0, clamp_type='MINMAX'):
    node = ng.nodes.new("ShaderNodeClamp")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Min"], min)
    else:
        node.inputs["Min"] = min
    if isinstance(max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Max"], max)
    else:
        node.inputs["Max"] = max
    node.clamp_type = clamp_type

def combine_rgb(r=0.0, g=0.0, b=0.0, ):
    node = ng.nodes.new("ShaderNodeCombineRGB")
    if isinstance(r, bpy.types.NodeSocket):
        ng.links.new(node.inputs["R"], r)
    else:
        node.inputs["R"] = r
    if isinstance(g, bpy.types.NodeSocket):
        ng.links.new(node.inputs["G"], g)
    else:
        node.inputs["G"] = g
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs["B"], b)
    else:
        node.inputs["B"] = b

def combine_xyz(x=0.0, y=0.0, z=0.0, ):
    node = ng.nodes.new("ShaderNodeCombineXYZ")
    if isinstance(x, bpy.types.NodeSocket):
        ng.links.new(node.inputs["X"], x)
    else:
        node.inputs["X"] = x
    if isinstance(y, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Y"], y)
    else:
        node.inputs["Y"] = y
    if isinstance(z, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Z"], z)
    else:
        node.inputs["Z"] = z

def float_curve(factor=1.0, value=1.0, mapping=<bpy_struct, CurveMapping at 0x0000014454DA6948>):
    node = ng.nodes.new("ShaderNodeFloatCurve")
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    node.mapping = mapping

def map_range(value=1.0, from_min=0.0, from_max=1.0, to_min=0.0, to_max=1.0, steps=4.0, vector=[0.0, 0.0, 0.0], from_min=0.0, from_max=1.0, to_min=0.0, to_max=1.0, steps=4.0, interpolation_type='LINEAR', clamp=True, data_type='FLOAT'):
    node = ng.nodes.new("ShaderNodeMapRange")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(from_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["From Min"], from_min)
    else:
        node.inputs["From Min"] = from_min
    if isinstance(from_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["From Max"], from_max)
    else:
        node.inputs["From Max"] = from_max
    if isinstance(to_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["To Min"], to_min)
    else:
        node.inputs["To Min"] = to_min
    if isinstance(to_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["To Max"], to_max)
    else:
        node.inputs["To Max"] = to_max
    if isinstance(steps, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Steps"], steps)
    else:
        node.inputs["Steps"] = steps
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(from_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["From Min"], from_min)
    else:
        node.inputs["From Min"] = from_min
    if isinstance(from_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["From Max"], from_max)
    else:
        node.inputs["From Max"] = from_max
    if isinstance(to_min, bpy.types.NodeSocket):
        ng.links.new(node.inputs["To Min"], to_min)
    else:
        node.inputs["To Min"] = to_min
    if isinstance(to_max, bpy.types.NodeSocket):
        ng.links.new(node.inputs["To Max"], to_max)
    else:
        node.inputs["To Max"] = to_max
    if isinstance(steps, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Steps"], steps)
    else:
        node.inputs["Steps"] = steps
    node.interpolation_type = interpolation_type
    node.clamp = clamp
    node.data_type = data_type

def math(value=0.5, value=0.5, value=0.5, operation='ADD', use_clamp=False):
    node = ng.nodes.new("ShaderNodeMath")
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    if isinstance(value, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Value"], value)
    else:
        node.inputs["Value"] = value
    node.operation = operation
    node.use_clamp = use_clamp

def mix(factor=0.5, factor=0.5, a=0.0, b=0.0, a=0.0, b=0.0, a=0.0, b=0.0, clamp_result=False, blend_type='MIX', clamp_factor=True, data_type='FLOAT', factor_mode='UNIFORM'):
    node = ng.nodes.new("ShaderNodeMix")
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(factor, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Factor"], factor)
    else:
        node.inputs["Factor"] = factor
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs["A"], a)
    else:
        node.inputs["A"] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs["B"], b)
    else:
        node.inputs["B"] = b
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs["A"], a)
    else:
        node.inputs["A"] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs["B"], b)
    else:
        node.inputs["B"] = b
    if isinstance(a, bpy.types.NodeSocket):
        ng.links.new(node.inputs["A"], a)
    else:
        node.inputs["A"] = a
    if isinstance(b, bpy.types.NodeSocket):
        ng.links.new(node.inputs["B"], b)
    else:
        node.inputs["B"] = b
    node.clamp_result = clamp_result
    node.blend_type = blend_type
    node.clamp_factor = clamp_factor
    node.data_type = data_type
    node.factor_mode = factor_mode

def mix_rgb(fac=0.5, color1=None, color2=None, blend_type='MIX', use_clamp=False, use_alpha=False):
    node = ng.nodes.new("ShaderNodeMixRGB")
    if isinstance(fac, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fac"], fac)
    else:
        node.inputs["Fac"] = fac
    if isinstance(color1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color1"], color1)
    else:
        node.inputs["Color1"] = color1
    if isinstance(color2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color2"], color2)
    else:
        node.inputs["Color2"] = color2
    node.blend_type = blend_type
    node.use_clamp = use_clamp
    node.use_alpha = use_alpha

def rgb_curve(fac=1.0, color=None, mapping=<bpy_struct, CurveMapping at 0x0000014454DA5D08>):
    node = ng.nodes.new("ShaderNodeRGBCurve")
    if isinstance(fac, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fac"], fac)
    else:
        node.inputs["Fac"] = fac
    if isinstance(color, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color"], color)
    else:
        node.inputs["Color"] = color
    node.mapping = mapping

def separate_rgb(image=None, ):
    node = ng.nodes.new("ShaderNodeSeparateRGB")
    if isinstance(image, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Image"], image)
    else:
        node.inputs["Image"] = image

def separate_xyz(vector=[0.0, 0.0, 0.0], ):
    node = ng.nodes.new("ShaderNodeSeparateXYZ")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector

def tex_brick(vector=[0.0, 0.0, 0.0], color1=None, color2=None, mortar=None, scale=5.0, mortar_size=0.019999999552965164, mortar_smooth=0.10000000149011612, bias=0.0, brick_width=0.5, row_height=0.25, color_mapping=<bpy_struct, ColorMapping at 0x000001445A777498>, offset=0.5, squash=1.0, texture_mapping=<bpy_struct, TexMapping at 0x000001445A777408>, squash_frequency=2, offset_frequency=2):
    node = ng.nodes.new("ShaderNodeTexBrick")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(color1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color1"], color1)
    else:
        node.inputs["Color1"] = color1
    if isinstance(color2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color2"], color2)
    else:
        node.inputs["Color2"] = color2
    if isinstance(mortar, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mortar"], mortar)
    else:
        node.inputs["Mortar"] = mortar
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    if isinstance(mortar_size, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mortar Size"], mortar_size)
    else:
        node.inputs["Mortar Size"] = mortar_size
    if isinstance(mortar_smooth, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Mortar Smooth"], mortar_smooth)
    else:
        node.inputs["Mortar Smooth"] = mortar_smooth
    if isinstance(bias, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Bias"], bias)
    else:
        node.inputs["Bias"] = bias
    if isinstance(brick_width, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Brick Width"], brick_width)
    else:
        node.inputs["Brick Width"] = brick_width
    if isinstance(row_height, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Row Height"], row_height)
    else:
        node.inputs["Row Height"] = row_height
    node.color_mapping = color_mapping
    node.offset = offset
    node.squash = squash
    node.texture_mapping = texture_mapping
    node.squash_frequency = squash_frequency
    node.offset_frequency = offset_frequency

def tex_checker(vector=[0.0, 0.0, 0.0], color1=None, color2=None, scale=5.0, texture_mapping=<bpy_struct, TexMapping at 0x000001445A777808>, color_mapping=<bpy_struct, ColorMapping at 0x000001445A777898>):
    node = ng.nodes.new("ShaderNodeTexChecker")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(color1, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color1"], color1)
    else:
        node.inputs["Color1"] = color1
    if isinstance(color2, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Color2"], color2)
    else:
        node.inputs["Color2"] = color2
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    node.texture_mapping = texture_mapping
    node.color_mapping = color_mapping

def tex_gradient(vector=[0.0, 0.0, 0.0], texture_mapping=<bpy_struct, TexMapping at 0x000001445A777008>, color_mapping=<bpy_struct, ColorMapping at 0x000001445A777098>, gradient_type='LINEAR'):
    node = ng.nodes.new("ShaderNodeTexGradient")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    node.texture_mapping = texture_mapping
    node.color_mapping = color_mapping
    node.gradient_type = gradient_type

def tex_magic(vector=[0.0, 0.0, 0.0], scale=5.0, distortion=1.0, texture_mapping=<bpy_struct, TexMapping at 0x000001445A776C08>, color_mapping=<bpy_struct, ColorMapping at 0x000001445A776C98>, turbulence_depth=2):
    node = ng.nodes.new("ShaderNodeTexMagic")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    if isinstance(distortion, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distortion"], distortion)
    else:
        node.inputs["Distortion"] = distortion
    node.texture_mapping = texture_mapping
    node.color_mapping = color_mapping
    node.turbulence_depth = turbulence_depth

def tex_musgrave(vector=[0.0, 0.0, 0.0], w=0.0, scale=5.0, detail=2.0, dimension=2.0, lacunarity=2.0, offset=0.0, gain=1.0, texture_mapping=<bpy_struct, TexMapping at 0x000001445A776808>, color_mapping=<bpy_struct, ColorMapping at 0x000001445A776898>, musgrave_type='FBM', musgrave_dimensions='3D'):
    node = ng.nodes.new("ShaderNodeTexMusgrave")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(w, bpy.types.NodeSocket):
        ng.links.new(node.inputs["W"], w)
    else:
        node.inputs["W"] = w
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    if isinstance(detail, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail"], detail)
    else:
        node.inputs["Detail"] = detail
    if isinstance(dimension, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Dimension"], dimension)
    else:
        node.inputs["Dimension"] = dimension
    if isinstance(lacunarity, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Lacunarity"], lacunarity)
    else:
        node.inputs["Lacunarity"] = lacunarity
    if isinstance(offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Offset"], offset)
    else:
        node.inputs["Offset"] = offset
    if isinstance(gain, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Gain"], gain)
    else:
        node.inputs["Gain"] = gain
    node.texture_mapping = texture_mapping
    node.color_mapping = color_mapping
    node.musgrave_type = musgrave_type
    node.musgrave_dimensions = musgrave_dimensions

def tex_noise(vector=[0.0, 0.0, 0.0], w=0.0, scale=5.0, detail=2.0, roughness=0.5, distortion=0.0, texture_mapping=<bpy_struct, TexMapping at 0x000001445A776408>, color_mapping=<bpy_struct, ColorMapping at 0x000001445A776498>, noise_dimensions='3D'):
    node = ng.nodes.new("ShaderNodeTexNoise")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(w, bpy.types.NodeSocket):
        ng.links.new(node.inputs["W"], w)
    else:
        node.inputs["W"] = w
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    if isinstance(detail, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail"], detail)
    else:
        node.inputs["Detail"] = detail
    if isinstance(roughness, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Roughness"], roughness)
    else:
        node.inputs["Roughness"] = roughness
    if isinstance(distortion, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distortion"], distortion)
    else:
        node.inputs["Distortion"] = distortion
    node.texture_mapping = texture_mapping
    node.color_mapping = color_mapping
    node.noise_dimensions = noise_dimensions

def tex_voronoi(vector=[0.0, 0.0, 0.0], w=0.0, scale=5.0, smoothness=1.0, exponent=0.5, randomness=1.0, color_mapping=<bpy_struct, ColorMapping at 0x000001445A776098>, texture_mapping=<bpy_struct, TexMapping at 0x000001445A776008>, distance='EUCLIDEAN', voronoi_dimensions='3D', feature='F1'):
    node = ng.nodes.new("ShaderNodeTexVoronoi")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(w, bpy.types.NodeSocket):
        ng.links.new(node.inputs["W"], w)
    else:
        node.inputs["W"] = w
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    if isinstance(smoothness, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Smoothness"], smoothness)
    else:
        node.inputs["Smoothness"] = smoothness
    if isinstance(exponent, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Exponent"], exponent)
    else:
        node.inputs["Exponent"] = exponent
    if isinstance(randomness, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Randomness"], randomness)
    else:
        node.inputs["Randomness"] = randomness
    node.color_mapping = color_mapping
    node.texture_mapping = texture_mapping
    node.distance = distance
    node.voronoi_dimensions = voronoi_dimensions
    node.feature = feature

def tex_wave(vector=[0.0, 0.0, 0.0], scale=5.0, distortion=0.0, detail=2.0, detail_scale=1.0, detail_roughness=0.5, phase_offset=0.0, wave_profile='SIN', color_mapping=<bpy_struct, ColorMapping at 0x000001445A775C98>, wave_type='BANDS', bands_direction='X', rings_direction='X', texture_mapping=<bpy_struct, TexMapping at 0x000001445A775C08>):
    node = ng.nodes.new("ShaderNodeTexWave")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Scale"], scale)
    else:
        node.inputs["Scale"] = scale
    if isinstance(distortion, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Distortion"], distortion)
    else:
        node.inputs["Distortion"] = distortion
    if isinstance(detail, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail"], detail)
    else:
        node.inputs["Detail"] = detail
    if isinstance(detail_scale, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail Scale"], detail_scale)
    else:
        node.inputs["Detail Scale"] = detail_scale
    if isinstance(detail_roughness, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Detail Roughness"], detail_roughness)
    else:
        node.inputs["Detail Roughness"] = detail_roughness
    if isinstance(phase_offset, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Phase Offset"], phase_offset)
    else:
        node.inputs["Phase Offset"] = phase_offset
    node.wave_profile = wave_profile
    node.color_mapping = color_mapping
    node.wave_type = wave_type
    node.bands_direction = bands_direction
    node.rings_direction = rings_direction
    node.texture_mapping = texture_mapping

def tex_white_noise(vector=[0.0, 0.0, 0.0], w=0.0, noise_dimensions='3D'):
    node = ng.nodes.new("ShaderNodeTexWhiteNoise")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(w, bpy.types.NodeSocket):
        ng.links.new(node.inputs["W"], w)
    else:
        node.inputs["W"] = w
    node.noise_dimensions = noise_dimensions

def val_to_rgb(fac=0.5, color_ramp=<bpy_struct, ColorRamp at 0x0000014454DCBC88>):
    node = ng.nodes.new("ShaderNodeValToRGB")
    if isinstance(fac, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fac"], fac)
    else:
        node.inputs["Fac"] = fac
    node.color_ramp = color_ramp

def value():
    node = ng.nodes.new("ShaderNodeValue")

def vector_curve(fac=1.0, vector=[0.0, 0.0, 0.0], mapping=<bpy_struct, CurveMapping at 0x0000014454DA7208>):
    node = ng.nodes.new("ShaderNodeVectorCurve")
    if isinstance(fac, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Fac"], fac)
    else:
        node.inputs["Fac"] = fac
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    node.mapping = mapping

def vector_math(a=[0.0, 0.0, 0.0], b=[0.0, 0.0, 0.0], c=[0.0, 0.0, 0.0], scale=1.0, operation='ADD'):
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
        node.inputs["Scale"] = scale
    node.operation = operation

def vector_rotate(vector=[0.0, 0.0, 0.0], center=[0.0, 0.0, 0.0], axis=[0.0, 0.0, 1.0], angle=0.0, rotation=[0.0, 0.0, 0.0], rotation_type='AXIS_ANGLE', invert=False):
    node = ng.nodes.new("ShaderNodeVectorRotate")
    if isinstance(vector, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Vector"], vector)
    else:
        node.inputs["Vector"] = vector
    if isinstance(center, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Center"], center)
    else:
        node.inputs["Center"] = center
    if isinstance(axis, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Axis"], axis)
    else:
        node.inputs["Axis"] = axis
    if isinstance(angle, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Angle"], angle)
    else:
        node.inputs["Angle"] = angle
    if isinstance(rotation, bpy.types.NodeSocket):
        ng.links.new(node.inputs["Rotation"], rotation)
    else:
        node.inputs["Rotation"] = rotation
    node.rotation_type = rotation_type
    node.invert = invert
