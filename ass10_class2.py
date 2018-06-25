#ques 1:
class Animal():
	def animal_attribute(self):
		print("Base class called")

class Tiger(Animal):
	def show1(self):
		self.animal_attribute()

t=Tiger()
t.show1()

#ques 2:

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

#ques 3:

class Cop():
	def __init__(self):
		self.name = input("Enter the name")
		self.age = int(input("Enter the age"))
		self.work = input("Enter the work")
		self.experience = input("Enter the experience")
		self.designation = input("Enter the designation")

	def add(self):
		pass
	def display(self):
		print("The name is %s \n the age is %s \n the work is %s \n the experience is %s \n the designation is %s"%(self.name,self.age,self.work,self.experience,self.designation))
	def update(self):
		cc = input(
			"What is the information that you want to change \n 1.Enter 1 for name \n 2.Enter 2 for age\n "
			"3.Enter 3 for work\n 4.Enter 4 for experience \n 5.Enter 5 for designation")
		if (cc == "1"):
			cn = input("Enter the new name")
			self.name = cn
			self.display()
		elif (cc == "2"):
			ca = input("Enter the new age")
			self.age = ca
			self.display()
		elif (cc == "3"):
			cy = input("Enter the new work")
			self.work = cy
			self.display()
		elif (cc == "4"):
			cr = input("Enter the new experience")
			self.experience = cr
			self.display()
		else:
			cr = input("Enter the new designation")
			self.designation = cr
			self.display()

class Mission(Cop):
	def add_mission_details(self):
		self.deta=input("Enter details of the mission")
		print("the details of mission are:"+str(self.deta))
		self.display()

m = Mission()
m.add_mission_details()

#ques 4:

class Shape():
	def sh2(self):
		self.ll = int(input("Enter the length"))
		self.br = int(input("Enter the breadth"))

class Rectangle(Shape):
	def __init__(self):
		self.sh2()
		if(self.ll != self.br):
			print("Rectangle area")
			print( self.ll*self.br)
		else:
			pass
class Square(Shape):
	def __init__(self):
		self.sh2()
		if (self.ll == self.br):
			print("square area")
			print(self.ll * self.br)
		else:
			pass

r = Rectangle()
s = Square()
###########################################################2nd option####################################################

class Shape():
	def sh2(self):
		self.l = int(input("Enter the length"))
		self.b = int(input("Enter the breadth"))
class Rectangle(Shape):
	def area(self):
		self.sh2()
		self.A=self.l*self.b
	def sh1(self):
		print("area of rect"+str(self.A))
class Square(Shape):
	def sarea(self):
		self.sh2()
		self.C=self.l*self.b
	def sh4(self):
		print("area of square"+str(self.C))

R=Rectangle()
S=Square()
R.area()
R.sh1()
S.sarea()
S.sh4()
