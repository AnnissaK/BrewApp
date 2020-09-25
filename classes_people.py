class Person():
     def __init__(self,name):
         self.name = name

people=[]
name =['bil','bob','susan']

for i in name:
    people.append(Person(name))
print([person.name for person in people])

