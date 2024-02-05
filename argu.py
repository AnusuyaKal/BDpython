def argu(height,*arg,**kwarg ):
    print(''Height of the triangle is '' height)
    for x in args:
        print(x)
    for kw in kwarg:
        print(kw, kwarg[kw])
            
