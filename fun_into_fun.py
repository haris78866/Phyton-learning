x=4
y=6

def square_x(x) :
    return x*x

def square_y(y) :
    return y*y

a=square_x(x)
b=square_y(y)


print("square of x : ",a)
print("square of y : ",b)

def fun_add(x,y) :
    return square_x(x)+square_y(y) 

c=fun_add(x,y)

print("add of both fun : ",c)


