import datetime,time,math,os
from time import gmtime,strftime

#ques1:
print("Time tuple is used to represen time in a way it is easy to understand.And it is stored in tuple.And also that these tuples aree made of nine numbers..")
print("eg:index:0->year...index:1->Month...index:2->Day...index:3->hour...index:4->Minute..index:5->Sec..index:6->Day of Week..index:7->day f year..index:8->Dst")

#quest2:

print("Formitted time:"+time.asctime(time.localtime()))

#ques 3:
print(time.strftime("%b"))

#ques4:

print(time.strftime("%A"))

#ques 5:

dateen=int(input("Enter date"))
yearen=int(input("Enter Year"))
monen=int(input("Enter month"))

dateentered=datetime.date(yearen,monen,dateen)
print(dateentered.strftime("%b"))

#ques 6:
print(strftime("%H:%M:%S", gmtime()))
#ques 7:

x=int(input("Enter your number"))
print("the factorial is"+" "+str(math.factorial(x)))

#ques8:
a= int(input("Enter 1 numbers"))
b= int(input("Enter 2 numbers"))
print("gcd is:"+str(math.gcd(a, b)))

#ques 9:

print("Current Working Directory"+str(os.getcwd()))
print("User environment"+str(os.environ))