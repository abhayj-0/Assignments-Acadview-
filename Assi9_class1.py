#quest 1:

class Circle():
    def __init__(self,radius):
        self.rad=radius
    def getArea(self):
        print("the area is:"+str(3.14*self.rad*self.rad))
    def getCircumference(self):
        print("the circumference:"+str(2*3.14*self.rad))
cir=Circle(4)
cir.getArea()
cir.getCircumference()

#quest 2:

class Student():
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno

    def display(self):
        print("the Student name is "+str(self.n)+"and roll no. is "+str(self.r))


s=Student("abhay",20)
s.display()

#ques 3:
class Temprature():
    def __init__(self,F,C):
        self.ff=F
        self.cc=C
    def celsius(self):
        print("The temprature in celcius is"+str((self.ff-32)*.5556))
    def fahrenheit(self):
        print("The temprature in fahrenheit is"+str((self.cc*1.8)+32))


t=Temprature(50,60)
t.celsius()
t.fahrenheit()

#ques 4:
class Moviedet():
    def __init__(self,name,artistname,year,ratings):
        self.n=name
        self.a=artistname
        self.y=year
        self.r=ratings

    def display(self):
        print("the movie name is "+str(self.n)+" artist is "+str(self.a)+" year of realese "+str(self.y)+" ratings are "+str(self.r))

    def update(self):
        cc=input("What is the information that you want to change \n 1.Enter 1 for name \n 2.Enter 2 for ArtistName\n 3.Enter 3 for year\n 4.Enter 4 for ratings")
        if (cc == "1"):
            cn = input("Enter the new name")
            self.n = cn
            self.display()
        elif (cc == "2"):
            ca = input("Enter the new artist")
            self.a = ca
            self.display()
        elif (cc == "3"):
            cy = input("Enter the new year")
            self.y = cy
            self.display()
        else:
            cr = input("Enter the new ratings")
            self.r = cr
            self.display()

#           or the other way around......JUST FOR FUN
#              if (cc == "name"):
#                 cn = input("Enter the new name")
#                 self.n = cn
#                 self.display()
#             elif (cc == "artistname"):
#                 ca = input("Enter the new artist")
#                 self.a = ca
#             elif (cc == "year"):
#                 cy = input("Enter the new year")
#                 self.y = cy
#             else:
#                 cr = input("Enter the new ratings")
#                 self.r = cr


m=Moviedet("Hacksaw Ridge","Andrew garfield",2016,5)
m.display()
m.update()

#ques5 :

class Expenditure():
    expenditure = int(input("Enter the expenditure"))
    savngs = int(input("Enter your savings"))

    def displex_sal(self):
        print("Expenditure is " + str(self.expenditure) + " and Savings is " + str(self.savngs))

    def totsal(self):
        self.salary = self.expenditure + self.savngs

    def display(self):
        print("total salary is " + str(self.salary))



e=Expenditure()
e.displex_sal()
e.totsal()
e.display()
