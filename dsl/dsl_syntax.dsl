# Expressions involving more than one nodes should be automatically made a group, with lhs as output and symbols on rhs as input 
# An expression is any line of the form, `lhs = rhs`
# groups can be alternatively defined using group, like a function def, with function args as group inputs and return symbols as group outputs
# group main will be the root nodetree and every file should contain group main
# everything should be typed
# Types are -> node, geo, int, float, vec, mat, clr, col, obj, 
# connections can be manually done using `link(a,b)`

# Example File
group main(geo a, int b, float c, int x, col d, mat c='Default'):
    # converted to 
    p = (c + b - x) % a;
    a = transform(a, p, something=2);
    return a, b;

group cube(geo a, int c):
    q = a + c;
    return q;