numbers_to_sum = []

for x in range 1, 1000: 
    printf("Testing {x}")
    if x % 3 == 0 or x % 5 == 0:
        numbers_to_sum.add(x)

print(numbers_to_sum.sum())
