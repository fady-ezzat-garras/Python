#s = input("Enter a string: ")
#arr = {'a', 'e', 'i', 'o', 'u'}
#count = 0

#for char in s:
#    if char in arr:
#        count += 1

#print("Number ", count)



#====================2===================
# def generate(length, start):
#     numbers = []  
#     for i in range(length):  
#         numbers.append(start + i) 
#     return numbers  
# print(generate(5, 9))  

# ===================3=====================

# numbers = []

# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))  
#     numbers.append(num)

# ascending = sorted(numbers)

# descending = sorted(numbers, reverse=True)

# print("Ascending:", ascending)
# print("Descending", descending)

# ==================4=========================

# def reverse(input):
#     return input[::2]  

# text = input("Enter a string: ")

# print("Reversed String:", reverse(text))

# =================5=============================

# def FizzBuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return number  

# number = int(input("Enter a number: "))
# print(FizzBuzz(number))

# ================6======================

# import math 

# def circle_properties(radius):
#     area = math.pi * radius ** 2 
#     circumference = 2 * math.pi * radius  
#     return area, circumference


# area, circumference = circle_properties(15)
# print(f"Area: {area}")
# print(f"Circumference: {circumference}")

#===================7=====================

# def valid_name(name):
#     return all(char.isalpha() or char.isspace() for char in name)  
#         #allهترجع true لو كل القيم صح 

# while True:
#     name = input("Enter your name: ").strip()
#     if name and valid_name(name):  
#         break
#     print("Invalid name")


# email = input("Enter your email: ").strip()


# print("\n User Information:")
# print(f"Name: {name}")
# print(f"Email: {email}")

# ================8=======================


# text = input("Enter a text: ")


# count = text.count("iti")


# print(f"'iti'  {count} ")

# =====================9=======================

