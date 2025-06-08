# It is short method of creating a list 

a = []
for i in range(1,11):
    a.append(5*i)
print(a) 
#  To write this type of code it is quite easy but there is a short method also 

a = [5*i for i in range(1,11)]
print(a)