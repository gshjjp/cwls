#coding=utf-8

class Cat:

    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
    def __str__(self):
        return "%s age: %d"%(self.name,self.age)

    def eat(self):
        print("chiyu......")
    def drink(self):
        print("heshui.....")
    def jieshao(self):
        print("%s age:%d"%(self.name,self.age))

wls = Cat("wls",30)

wls.drink()
wls.eat()
#wls.jieshao()
print(wls)

wlsc = Cat("jp",29)
print(wlsc)
#wlsc.jieshao()
