# Tuple: A collection which is ordered and unchangeable. Used to group together related data. 

student = ("Bro",21,"Male")

print(student.count("Bro"))
print(student.index("Male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")

