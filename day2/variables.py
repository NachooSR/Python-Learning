#Day 2: 30 Days of python programming

import math

firstName = "Ignacio"
lastName  = "Reyna"
fullName  = "Ignacio Nicolas Reyna"
country   = "Argentina"
city      = "Mar del Plata"
age       = 22
year      = 2025
isMarried = False
is_True   = True
isLighton = False
nombre,edad,equipo = "Carlos",49, "Boca Juniors"

#Excercise 2 
print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(age))
print(type(isLighton))

print(len(firstName))

if len(firstName) > len(lastName):
    print("First Name longer tan last name")
else:
    print("Last name longer")

num_one= 5
num_two= 4

total= num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division= num_one // num_two

'''''
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
'''''


area_of_circle = math.pi * 30**2
circum_of_circle = 2 * math.pi * 30

print(f"{area_of_circle:.2f}")
print(f"{circum_of_circle:.2f}")

radiusInput = float(input("Radius: ").strip())
calculateArea= math.pi * radiusInput**2
print(f"{calculateArea:.2f}")

firstNameInput = str(input("First Name: ").strip())
lastNameInput  = str(input("Last Name: ").strip())
countryInput   = str(input("Country: ").strip())
ageInput       = int(input("Age: ").strip())

print(firstName,lastName,ageInput,countryInput)
