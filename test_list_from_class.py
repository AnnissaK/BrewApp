class Robot():
    """Test class"""
    def __init__(self, age,name):
        self.age = age
        self.name=name

r = Robot(10,'r')
r1 = Robot(15,'r1')

mylist1 = [r, r1]
d={}

for item in mylist1:
    d[item.name]=item
print(d)