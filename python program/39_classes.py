class student:
    def __init__(self,name,city):
        self.name=name
        self.city=city
s1=student("muskan","beed")
print(s1.name)
print(s1.city)

class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def __str__(self) -> str:
        return f"{self.name} ({self.age})"
p1=person("muskan",22)
print(p1)

class shape:
    def __init__(self,name) -> None:
        self.name=name
    def circle(self):
         print("heloo my name is "+self.name)
s1=shape("muskan")
s1.circle()