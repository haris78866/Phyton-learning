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
    """ documentation of my function pressure """
    k=1.38-23
    return n*k*t/v

cons=pressure(v,t,n)
print("cons=",cons)


