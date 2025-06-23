#User input 
numberA = int(input("Enter number: ").strip()) # Strip quita espacios en blanco

numberB = int(input("Enter number: ").strip())

#Testing operands
print( numberA + numberB ) #Suma
print( numberA - numberB ) #Resta
print( numberA * numberB ) #Multiplicacion
print( numberA % numberB ) #Modulo -> muestra el resto
print( numberA / numberB ) #Division
print( numberA **numberB ) #Exponencial
print( numberA //numberB ) #Devuelve la parte entera de la division

#Writing strings
print('Hello world!')
print("Ignacio Reyna") 

#Checking data types
print(type(numberA))
print(type(3.5))
print(type(4-4j))
print(type(["Juan","Pedro","Nacho"]))
print(type(True))

#Euclidian Distance
x1= float(input("Enter X1: ").strip())
y1= float(input("Enter Y1: ").strip())

x2= float(input("Enter X2: ").strip())
y2= float(input("Enter Y2: ").strip())

euclidian_Distance = ((x2 - x1) ** 2 + (y2-y1) ** 2) ** 0.5

print(f"Result: {euclidian_Distance:.2f}")