Name = input("Full name: ")
ID = input(" ID #: ")
Course = input("course: ")
Section = input(" section: ")
a1 = eval(input("first Quarter Grade: "))
a2 = eval(input("Second Quarter Grade: "))
a3 = eval(input("Third Quarter Grade: "))
a4 = eval(input("Fourth Quarter Grade: "))
avg = (a1 + a2 + a3 + a4)/4
print("average: " + str(avg), "is", avg)
print("your details are")
print("Full name is " + Name)
print("ID# is " + ID)
print("course is " + Course)
print("Section Number is" + Section )
print("Average is:" + str(avg))
