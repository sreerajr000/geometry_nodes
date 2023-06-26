# Example File
group main(geo a, int b, float c, int x, col d, mat c='Default'):
    # converted to 
    p = (c + b - x) % a;
    a = transform(a, p, something=2);
    return a, b;