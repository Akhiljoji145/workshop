name=input("enter your name")
list=[]
for i in range(len(name)):
    list.append('_')
print(list)
for i in range(len(name)):
    list.pop(i)
    list.insert(i,name[i])
    print(list)