#1. sum all the items in a list
list1 = [1,5,20,60,200,2]
sumtotal = 0
for num in list1:
    sumtotal += num
print(sumtotal)

#2. multiply all the items in a list
multotal = 1
for num in list1:
    multotal *= num
print(multotal)


#3. program to get the largest number from a list
print(max(list1))
#style 2
largest = 0
for num in list1:
    if num > largest:
        largest = num
print (largest)


#4. program to get the smallest number from a list
print(min(list1))
#style 2
smallest = max(list1)
for num in list1:
    if num < smallest:
        smallest = num
print (smallest)

#5.
strlist = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in strlist:
    if len(i) >= 2:
        if i[0] == i[-1]:
            count += 1
print (count)

