student = [{'studentname': 'neethu', 'mark': 25},{'studentname': 'anu', 'mark': 30},{'studentname': 'akhil', 'mark': 20}, {'studentname': 'akash', 'mark': 40},{'studentname': 'adarsh', 'mark': 50}]
name = input("Enter student name: ")

for i in student:
    if i['studentname'] == name:
        print(i['mark'])
        break
else:
    print("name not found")