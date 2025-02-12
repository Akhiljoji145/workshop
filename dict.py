dict={'name':'akhil','age':22,'year':2024,'year':2025,'dept':'MCA'}
print(dict['dept'])
dict["dept"]='Mech'
print(dict)
dict.update({'dept':'EEE'})
print(dict)
dict.pop('year')
print(dict)
for i in dict:
    print(i)
for i in dict:
    print(dict[i])