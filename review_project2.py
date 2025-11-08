lst = [3, 2, 5, 9, 8, 4, 6, 7, 12]

remainder_0 = []
remainder_1 = []
remainder_2 = []
remainder_3 = []


for number in lst:
    r = number % 4 
    if r == 0:
        remainder_0.append(number)
    elif r == 1:
        remainder_1.append(number)
    elif r == 2:
        remainder_2.append(number)
    else: #r == 3 
        remainder_3.append(number)


print('remainder_0:',remainder_0)
print('remainder_1:',remainder_1)
print('remainder_2:',remainder_2)
print('remainder_3:',remainder_3)