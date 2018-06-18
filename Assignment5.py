
#ques 1: Leap year or not

a=int(input("Enter the year"))
if not a % 4:
    print("year is not a leap year")
else:
    print("year is a leap year")


#ques2:Rectangle and squre
length=0
breadth=0
s,d = input("Enter the length and breadth").split(",")

if(length==breadth):
    print("Square dimesions")
else:
    print("Rectangle dimensions")

#ques 3:input of 3 people's age and detemine the youngest and oldest

freya,goli,hero=input("Enter age of 3 people").split(",")

if freya>goli and freya>hero:
    print("freya is the youngest")
elif goli>freya and goli>hero:
    print("goli is youngest")
elif hero>freya and hero>goli:
    print("hero is the youngest")

if freya<goli and freya<hero:
    print("freya is the oldest")
elif goli<freya and goli<hero:
    print("goli is oldest")
elif hero<freya and hero<goli:
    print("hero is the oldest")

#ques 4:

a=int(input("enter the number of points"))

if a<=50:
    print("No Prize")
elif a>=51 and a<=150:
    print("Wooden Dog")
elif a>=151 and a<=180:
    print("Book")
elif a>=181 and a<=200:
    print("Chocolates")
else:
    print("Sorry!No Prize Won")

#ques 5:


quan=int(input("Enter the quntity"))
quan = quan*100

if quan>=1000:
    dis = quan*(10/100)
    print("You got disount of 10%")
    print("your total price is"+str(quan-dis))
else:
    print("Your Prize is:"+str(quan*100))





