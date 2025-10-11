lst = [3,2,5,9,8,4,6,7,12]

divible_by_3 = []

not_divible_by_3 = []



for number in lst:
    if number % 3 == 0:
        divible_by_3.append(number)
    else:
        not_divible_by_3.append(number)
        
print('divible_by_3:', divible_by_3)
print('not_divible_by_3:', not_divible_by_3)