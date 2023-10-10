# Set: A collection which is unordered and unindexed. No duplicate values allowed. 

utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup"}

utensils.add("napkin")

for x in utensils: 
    print(x)

utensils.remove("fork")

for x in utensils: 
    print(x)


utensils.clear()

print(utensils)
for x in utensils: 
    print(x)

utensils.update(dishes)

for x in utensils: 
    print(x)

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)


print(utensils.difference(dishes))
