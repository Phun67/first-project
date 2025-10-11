lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]#

even = []

odd = []


for i in range(0,21):
    if lst[i] % 2 == 0:
      
      even.append(lst[i])
    else:
        odd.append(lst[i])

print(odd)
print(even)
   