"""""
age = 22
height = 1.80
complex = 1 + 2j

base = float (input("Enter base: "))
heightTriangle = float(input("Enter height: "))

area= base * heightTriangle * 0.5
print("Area: ",area)

sideA = float(input("Enter side A: "))
sideC = float(input("Enter side B: "))
sideB = float(input("Enter side C: "))

perimeter = sideA + sideC + sideB
print("Perimeter: ",perimeter)
"""""

print(len("python"))
print(len("python") != len("Dragon"))
print('on' in 'pyhton' , 'on' in 'dragon')

cantidadLetras = float(len("Pyhton"))
cantidadLetrasStr = str(cantidadLetras)

print(f"{cantidadLetras:.2f}")

print(cantidadLetrasStr)

number =int(input("Enter number: "))
if number %2 == 0:
    print("Even")
else:
    print("Not even")

resto = int(7 // 3)
if resto == 3:
    print("Correct")
else:
    print("Not correct")



print(int(9.8) == 10)

years = int(input("Enter number of years you have lived: "))
#31,536,000 segundos un anio
secondsLive= 31536000 * years
print("You have lived: ",secondsLive," seconds")

"""
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

for n in range(1,6):
    print(n,n**0,n,n**2,n**3)
    