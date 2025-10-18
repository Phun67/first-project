lst = [3,2,5,9,8,4,6,7,12]

divible_by_3 = []
not_divible_by_3 = []
remainder_1 = []
remainder_2 = []
remainder_3 = []


for number in lst:
    if number % 3 == 0:
        divible_by_3.append(number)
    else:
        not_divible_by_3.append(number)
        
print('divible_by_3:', divible_by_3)
print('not_divible_by_3:', not_divible_by_3)


remainder_1 =[]
for number in lst:
    if number % 3 == 1:
        remainder_1.append(number)
        print('divided_by_get_1:', remainder_1)



        remainder_2 = []
        for number in lst:
            if number % 3 == 2:
                remainder_2.append(number)
                print('divided_by_get_2:', remainder_2)
                
                remainder_3 =[]
                for number in lst:
                    if number % 3 == 0:
                        remainder_3.append(number)
                        print('divided_by_get_0', remainder_3)