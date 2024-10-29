number = int(input("Enter the Number:"))
if(number > 0): # this condition is used for identify the number is less zero which means -1,-2,-3 and so on..
    print("The given number",number,"is positive")
else:
    print("The given number",number,"is negative")
    
#Two
election = input("Result of TVK is :")
if(election == "win"):
    print("CM VIJAY")
else:
    print("ACTOR VIJAY")
    
#Three
mark = int(input("Enter the Mark:"))
if(mark > 35):
    print("YOU'R PASS")
else:
    print("Sorry failed")

#Four
income = int(input("Enter your income:"))
if (income >7000):
    print("Your are not eligible for this Scholarship")
else:
    print("Your eligible")
    
    
#Five
num = int(input("Enter the number:"))
if(num%3 == 0 and num%5 == 0):
    print("yes it will ")
else:
    print("no , it wont")
    
#Six
number = int(input("Enter the number:"))
if (number%2 == 0): # diviable by 2 table number are even only..
    print("it is even")
else:
    print("its odd")

#Seven
mark = int(input("Enter your mark:"))
if(mark <= 35):
    print("Poor Student")
elif(mark <= 70):
    print("Average Student")
else:
    print("best student")

#Eight
a = int(input("Enter the number 1:"))
b = int(input("Enter the number 2:"))
operations = input("what kind of operations youe are going to do (add/sub/mul/div)?:")
add = a + b
sub = a - b
mul = a*b
div = a/b

if(operations == "add" ):
    print("your answer is:", add)
elif (operations == "sub" ):
    print("your answer is:", sub)
elif (operations == "mul" ):
    print("your answer is:", mul)
elif (operations == "div" ):
    print("your answer is:", div)
else:
    print("Invaild Number")

#Nine
percentage = int(input("Enter your Percentage:"))
if(percentage > 70):
    name = input("Enter Your Name:")
    department = input("Enter your Dept:")
    location = input("Enter your Location:")
    print("Name:",name)
    print("Department:", department)
    print("Location:", location)
else:
    print("Sorry Your not eligible")

#Ten
salary = int(input("Enter Your salary:"))
age = int(input("Enter your age:"))
if(salary >= 20000 or age >= 20):
    loan = int(input("Enter your load amount"))
    print("You Are eligible")  
    if(loan >= 50000):
        print("Maximum amount is 50000")
else:
    print("your not eligible")

#Eleven
tamil = int(input("Enter tamil mark:"))
english = int(input("Enter eng mark:"))
maths = int(input("Enter maths mark:"))
sci = int(input("Enter sci mark:"))
social = int(input("Enter social mark:"))
add = tamil + english + maths + sci + social
avg = add / 500 * 100
if (avg <= 35):
    print("Additinal Class is Required bez,  your avg is", avg , "only")
else:
    print("good to gooo")
    
    



