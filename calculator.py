def add(a,b):
    x = a+b
    return x
def sub(a,b):
    x=a-b
    return x
def mul(a,b):
    x=a*b
    return x
def div(a,b):
    if b == 0:
        raise ValueError("It will not divide by zero")
    elif a==0 and b==0:
        raise ValueError("undefined value")
    return a/b