def argu(i,*arg,**kwarg):
    print(i, end='')
    for x in arg:
        print(x)
    for kw in kwarg:
        print(kw, ':', kwarg[kw])
            
argu("python"," is a simple program", use=" to use in Big Data", oops="also it is a object oriented program")