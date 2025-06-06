a = "sayyam"

# Changing case 
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())

# Removing white space 
print(a.strip())
print(a.lstrip())
print(a.rstrip())

# Replacing and changing case 
b = "Python is fun and easy "
print(b.find("fun"))
print(b.replace("fun" , "awesome"))

# splitting and joining
c = "Apple,Bananas,chikoo,watermelon"
print(c.split(","))
print(",".join(['Apple,Bananas,chikoo,watermelon']))

text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace()) 