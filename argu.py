def argu(height,*arg,**kwarg):
    print("Height of the triangle is")
    for x in arg:
        print(x)
    for kw in kwarg:
        print(kw, kwarg[kw])
            
argu(100,"python is good program")