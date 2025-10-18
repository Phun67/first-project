lst = [3, 2, 5, 9, 8, 4, 6, 7, 12]

remainder_1 = []
remainder_2 = []
remainder_3 = []

for number in lst:
    r = number % 3
    if r == 0:
    
        remainder_3.append(number)
    else:
    
        if r == 1:
            remainder_1.append(number)
        else:  # r == 2
            remainder_2.append(number)

print('remainder_0:', remainder_3)
print('remainder_1:', remainder_1)
print('remainder_2:', remainder_2)