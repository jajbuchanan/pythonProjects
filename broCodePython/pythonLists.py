# List: Used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

print(food[0])
food[0] = "sushi"

food.append("ice cream")
food.remove("hotdog")

barf = food.pop()
print("after popping: " + barf)
food.sort()

food.insert(0, "cake")

for x in food: 
    print(x)

food.clear()
print(food)
