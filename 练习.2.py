#def demo(a,b,c,d=5,e=7,h=9):
   # a=a+1
   # b=b+1
    #c=c+1
    #print(a,b,c,d,e,h)


#x,y,z=1000,2000,3000
#demo(x,y,z,x,y,z)
#demo(10,c-1000,b-90)
#print(x,y,z)





#class Dog():
    #def __init__(self,name,age,height):
       # self.name=name
       # self.age=age
        #self.height=height
        

  # def sit(self):
        #print(self.name.title()+'is now eating shit.')

    #def r_over(self):
       # print(self.name.title()+'rolled over!')

    #def jiao(self):
       # print(self.name.title()+'在汪汪叫！！')

#dog1=Dog('大黄狗',18,180)
#print(dog1.name,dog1.age,dog1.height)
#dog1.sit()
#dog1.jiao()



class Student():
    school='青岛工学院'
    def __init__(self,name):
        self.__name=name
    def out(self):
        print('mane:',self.__name)
        print('school:',Student.school)
class M_Student(Student):
    def __init__(self,name,grade):
        super().__init__(name)
        self.__grade=grade
    def out(self):
        Student.out(self)
        print('grade:',self.__grade)
class C_Student(M_Student):
    def out(self):
        super().out()
        print('信息工程学院')
class 


s=Student('大黄狗')
s.out()
ms=M_Student('渣渣猫',90)
ms.out()

cs=C_Student('杨狗',85)
cs.out()



