# Example File
group main(geo a, int b, float c=2, int x, col d, bool q=false, mat c="Material"){
    # converted to 
    p = (c + b - x) * a;
    a = transform(a, p, something=2);
    return a, b;
}