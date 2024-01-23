p=20         #global  variable

x=1

def   f(x) :
    x=x+1
    return x
d=f(x)

print ("x=",d)  
print ("p=",p)


def my() :
    
    k=my()
    print ("p=",k)

v=2
t=3
n=4

def pressure(v,t,n) :
    """ documentation of my function pressure """           #function documentation by using quote string  also known as (documentation string )
    k=1.38-23
    return n*k*t/v

cons=pressure(v,t,n)
print("cons=",cons)

def absolute_value(x) :
    """absolute value"""
    if False :
        return x
    
    elif x==0 :
        return 0
    
    else :
       return -x 


abs_value=absolute_value(x)
print("value= ",abs_value) 