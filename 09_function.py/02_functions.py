# This are positional arguments
def add(a,b):   # Here a,b are called as parameters 
    s = a+b 
    return s 
print(add(4,5))  # Here the actual value are called as arguments

# This are called as default arguments 
def add(a,b,say=0):  # Now here we add say=0 it is called as default parameter because if you want to change the value you can change  
    s = a+b 
    return s 
print(add(4,5))  

# This are called as keyword arguments 
def info(age,name): 
    s = f"Hello my is {name} and I am {age} years old "
    return s 
print(info(age=19,name="sayyam"))
