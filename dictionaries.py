student={'name':'sadia','age':'22','sub':['math','english','Art']}
print(student)
print(student['name'])
print(student.get('age'))
print(student.get('phn'))
print(student.get('phn','not found'))
student['phn']='8576987987'
print(student.get('phn'))
print(student)

student.update({'name':'deya','age':'23'})
print(student)

del student['phn']
print(student)

age=student.pop('age')
print(age)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())


for key in student:
    print(key)

for key,value in student.items():
    print(key,value)