numbers_to_sum = []

for x in range(1, 1000):
    print("Testing " + str(x)) 
    if x % 3 == 0 or x % 5 == 0:
        numbers_to_sum.append(x)

print(sum(numbers_to_sum))
