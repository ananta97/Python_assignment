# 1. leap year challangee


# year = int(input("Enter the year to check leap year or not:"))

# if year % 4 == 0:
#     if year % 100 != 0:
#         print("Leap year")
#     elif year % 400 == 0:
#         print("Leap year")
#     else:
#         print("Not a leap year")
# else:
#     print("Not a leap year")



# 2. check the price of pizza with  multiple options..
# print("Welcome to the pizza world")
# size = input("What size of pizza do you want? (S, M, or L): ").upper()
# add_pepporoni = input("Do you want to add pepperoni? (Y or N): ").upper()
# extra_cheese = input("Do you want extra cheese? (Y or N): ").upper()
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepporoni == "Y":
#     if size == "S":
#         bill += 2
#     elif size == "M" or size == "L":
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"The total price of your pizza is: ${bill}")
 
# 3. check through age and height to check to ride rollercoaster
# height = int(input("Enter your height in cm:"))

# if height < 120:
#     print("You cannot ride a rollercoaster.")
# elif height == 120:
#     print("Please increase 1 cm to ride the roller-coaster")
#     exit()

# age = int(input("Enter your age:"))
# bill = 0

# if height > 120:
#     if age <= 5:
#         print("Under age to play rollercoaster")
#         exit()
#     elif age <= 12:
#         bill += 5
#     elif 12 < age <= 18:
#         bill += 7
#     elif 18 <= age <= 44:
#         bill += 12
#     elif 45 <= age <= 55:
#         bill += 0
#     else:
#         print("Invalid age.")

# photos = str(input("If you want photos or not: Y or N :"))
# if photos == "Y":
#     bill += 3

# print(f"The total bill of Ridding Roller-Coaster is ${bill}".upper())

# x="10"
# y = 5
# print(x*y)

# # 4.love calculator
# name1 = input("What is your name?\n".lower())
# name2 = input("What is their name?\n".lower())
# count_name1 = 0
# count_name2 = 0

# true_love_chars ="true"+"love"

# for char in true_love_chars:
#     if char in name1:
#         count_name1 += name1.count(char)

# for char in true_love_chars:
#     if char in name2:
#         count_name2 += name2.count(char)

# love_score = str(count_name1) + str(count_name2)

# print(f"The love score is {love_score}")

# if int(love_score) < 10 or int(love_score) > 90:
#     print("You go together like coke and mentos!")
# else:
#     print("You are perfect together!")

#import ramdom
# random_integer =random.randint(0,10)
# print(random_integer)

# import my_module
# print(my_module.a)

# import random
# random_number =random.randint(0,1)
# if random_number==1:
#     print("Head is generated")
# else:
#     print("Tail is generated")
 
# import random
# random_names =str(input("Enter the names of the people who are currently available: "))
# op = random_names.split(" ")
# random_value =random.choice(op)
# print(f"{random_value} is going to pay for today meal")

# # tick-tack 
# row1 =["◻","◻","◻"]
# row2 =["◻","◻","◻"]
# row3 =["◻","◻","◻"]
# map =[row1,row2,row3]
# print(f"{row1}\n,{row2}\n,{row3}\n")
# position =input("Where do you want to put the treasure:")
# horizonatal =int(position[0])
# vertical = int(position [1])

# print("   1 2 3")
# print("1."," ".join(row1))
# print("2."," ".join(row2))
# print("3."," ".join(row3))
# selected_rows=map[vertical -1]
# selected_rows[horizonatal -1] = "X"

# scissors,paper and rock game:
# import random
# choices =["R","S","P"]
# user_choice =input("What do you want to choose? Type R for Rock, P for Paper or S for Scissors: S , P or R:\n").upper()

# computer_choice =random.choice(choices)
# print(f"Computer choose {computer_choice}")
# print(f"user choose {user_choice}")

# if user_choice not in choices:
#      print("Invalid choice")

# elif user_choice == 'R' and computer_choice == 'S':
#     print("User win")
# elif user_choice == 'S' and computer_choice == 'P':
#     print("User Win")

# elif user_choice == 'P' and computer_choice == 'R':
#     print("User Win")
# elif computer_choice == user_choice:
#    print("Draw matches:")
# else:
#     print("Computer Win")

# calculate the average using for loops:
# student_heights = input("Input a list of student heights: ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height = 0
# for height in student_heights:
#     total_height += height

# number_of_students = len(student_heights)

# average_height = round(total_height / number_of_students)

# print(f"Average height is {average_height}")

# highest among the list using for loops:
# student_score =(input("Input a list of students Marks").split())
# for n in range(0,len(student_score)):
#    student_score[n] =int(student_score[n])
# print(student_score)

# highest_marks =0
# for marks in student_score:
#   if marks > highest_marks:
#      highest_marks = marks
# print(f"The highest among the marks is {highest_marks}")

# total_sum =0
# add_num =""
# for num in range(1,101):
#     total_sum +=num
#     add_num += str(num)
#     if num<100 :
#         add_num += " + "
# print(f"Added number are: {add_num}")
# print(f"Total Sum is {total_sum}")
 
# # add even numbers from 1 to 100:
# total =0
# even_numbers =''
# for num in range(1,101):
#     if num%2 ==0:
#         total +=num
#         even_numbers +=str(num)
#         if num < 100:
#             even_numbers += "+"

# print(f"Even numbers are {even_numbers} ")
# print(f"Sum of Even numbers are {total} ")

# # fizz Buzz game exercise
# for num in range(1,31):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#       print(num)
 
# A simple password Generator

import random
letters =['F', 'q', 'Y', 'x', 'C', 'G', 'N', 'J', 'n', 'o', 'P', 'V', 'w', 'a', 'X', 'v', 'B', 'h', 'Z', 'd', 'T', 'g', 's', 'R', 'l', 'U', 'I', 'u', 'b', 'm', 'W', 'k', 'f', 'L', 'A', 'y', 'e', 'p', 'H', 'j', 'S', 'D', 'r', 'K', 'q', 'O', 't', 'i']


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
           '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', 
           '?', '/', '~', '`', '€', '©', '®', '¶', '°', '∆', '÷', '×', '±', '∑', 
           '√', '∞', '§', '™', '♪', '♫', '☼', '☻']
print("Welcome to password Generator")
nr_letters =int(input("How many letters would you like to create a password:\n"))
nr_numbers =int(input("How many numbers would you like to create a password:\n"))
nr_symbols =int(input("How many symbols would you like to create a password:\n"))
# print (input("Which category of password do you want to generate: Easy OR Hard\n".upper()))
password_list=[]
for char in range(1,nr_letters +1):
  password_list.append(random.choice(letters))
  
for char in range(1,nr_numbers +1):
  password_list.append(random.choice(numbers))
  

for char in range(1,nr_symbols +1):
  password_list.append(random.choice(symbols))
  

print(f"Password before shuffle {password_list}")
random.shuffle(password_list)
print(f"Password after shuffle {password_list}")

password =""
for char in password_list:
   password += char


print(f"Your password is:\n{password}")

    