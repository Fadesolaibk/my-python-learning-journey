#1
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
dicta = {}
for i in range(len(list2)):
    dicta[list1[i]] = list2[i]
print (dicta)

#2
dict1 = {0:10, 1:20}
dict1[2] = 30
print(dict1)

#3
dict3 = {1:10, 2:20}
dict4 = {3:30, 4:40}
dict5 = {5:50, 6:60}
dict3.update(dict4)
print(dict3)
dict3.update(dict5)
print(dict3)

#4
dict6 = {0:'zero',1:'one'}
print (2 in dict6)

#5 #sum all the items in a dictionary
dict7 = {1:20,2:30,3:60}
print(sum(dict7.values()))
