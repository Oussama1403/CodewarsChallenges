def array_diff(a, b):
    nwl = []
    for n in a:
        if not n in b:
            nwl.append(n)             
    return nwl