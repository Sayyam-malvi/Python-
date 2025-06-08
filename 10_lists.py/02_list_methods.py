marks = [23,34,45,56,78,89,76,54] 

print(marks.count(45))  # count()- To count the element

marks.append(99)
print(marks)  # To add the element in last

marks.pop()
print(marks)  # To remove one element in last

new_marks = [32,87,98]
marks.extend(new_marks)
print(marks) # To add two lists 

marks.sort()
print(marks)  # To sort the lists 

marks.clear()
print(marks)   # To remove the all element and make a empty list 
 
# There are more methods of list 
marks.insert(3,99)
print(marks)