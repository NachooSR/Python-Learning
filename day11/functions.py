import math
#Level 1
#1
def add_two_numbers (A,B):
    return A+B

print(add_two_numbers(2,5))

#2
def area_circle(radius):
    return math.pi * (radius ** 2)

print(f"\nArea: {area_circle(5):.2f}")

#3
def add_all_numbers(*numbers):
    acumulador=0
    for i in numbers:
        if isinstance(i,(int,float)):
         acumulador+=i
        else:
           return "No son todos numeros para sumar"
    return acumulador

rta_function= add_all_numbers(2,4,6)

if isinstance(rta_function,(str)):
   print(rta_function)
else:
   print(f"\nSuma: {rta_function}")

#4
def convert_celsius(celsius):
   return (celsius * 9/5) +32

print(f"30 Celsius = {convert_celsius(30):.2f} F\n")

#5


def check_season (month):
 Summer= ["Diciembre","Enero","Febrero"]
 Autumn= ["Marzo","Abril","Mayo"]
 Winter= ["Junio","Julio","Agosto"]
 Spring= ["Septiembre","Octubre","Noviembre"]   
   
 if month in Summer:
    return("Summer season")
 elif month in Autumn:
    return("Autum season")
 elif month in Winter:
    return("Winter season")
 else:
    return("Spring season")

print(check_season("Enero"))

#6 
def calculate_slope(x1,y1,x2,y2):
   return (y2-y1) / (x2-x1)

slope = calculate_slope (2,3,6,11)
print(f"Slope: {slope :.2f}\n")

#7
def solve_quadratic_eqn(a,b,c):
    
    x1= ( -b + math.sqrt((b**2 -4*a*c)) )/ 2*a
    x2= ( -b - math.sqrt((b**2 -4*a*c)) )/ 2*a
    return x1,x2


x1,x2= solve_quadratic_eqn(1,5,6)


#8
def print_list(list):
   for i in list:
      print(i)

list_names=["Nacho","Juan","Pedro","Carlos"]

print_list(list_names)
print('\n')

#9
def reverse_list(list):
   reverse_list= []
   i=len(list)
   for item in range(i-1,-1,-1):
      reverse_list.append(list[item])
   return reverse_list

reverse_lt= reverse_list(list_names)
print(reverse_lt)

#10
def capitalize_items(list):
   
   cap_list=[]
   for i in list:
      cap_list.append(i.capitalize())
   
   return cap_list

cap_lt= capitalize_items(list_names)
print(cap_lt)

#11
def add_item(*item,lista):
   for i in item:
      lista.append(i)
   
   return lista

list_names=add_item("Lorena","Luz",lista=list_names)
print("\n",list_names)

#12
def remove_item(lista,item):
   lista.remove(item)
   return lista

list_names=remove_item(list_names,"Lorena")

print(list_names)

#13
def sum_numbers(number):
    
    sum=0
    for i in range(1,number+1):
       sum+=i
    return sum
print(sum_numbers(5)) 

#14

#Func aux
def is_even(number):
   return number %2 ==0

def sum_of_odds(number):
   suma=0
   for i in range(1,number+1):
      if not is_even(i):
       suma+= i
   return suma

suma_odds= sum_of_odds(5)
print(suma_odds)

#15
def sum_even(number):
   suma=0
   for i in range(1,number+1):
      if is_even(i):
       suma+=i
   return suma

suma_even= sum_even(4)
print(suma_even)

#Level 2

#1
def even_odds(number):
   even_numbers,odd_numbers=0,0
   for i in range(1,number+1):
      if is_even(i):
         even_numbers+=1
      else:
         odd_numbers+=1
   return even_numbers,odd_numbers

even_num,odd_num= even_odds(41)

print(f"Even: {even_num}. Odds: {odd_num}")

'''
Recursividad
def factorial(number):
   if number==0:
      return 1
   else:
     return  number * factorial(number-1) 
   
number_factorial= factorial(5)
print(number_factorial)
'''

def factorial_loop(number):
   acumulator= 1
   for i in range(1,number+1):
      acumulator *= i
   return acumulator

print(factorial_loop(5))

def is_empty(param):
   return param=="" or param=={} or param==[] or param is None

print(is_empty(""))

'''
Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
'''

def calculate_mean(lista):
   return sum(lista)/len(lista)

listita=[1,2,4,5,6,7,2]
print(calculate_mean(listita))

def calculate_median(lista):
   lista.sort()
   middle= len(lista) //2

   if len(lista) %2 != 0:
      middleItem=lista[middle]
   else:
      middleItem= (lista[middle-1] + lista[middle]) /2 

   return middleItem

median= calculate_median(listita)
print(median)

def valor_tupla(tupla):
   return tupla[1]

def calculate_mode(lista):
   valor_modal=dict()

   for valor in lista:
        if valor in valor_modal:
            valor_modal[valor]+=1
        else:
            valor_modal[valor]=1
   
   lista_valores=list( valor_modal.items())
   lista_valores= sorted(lista_valores,key=valor_tupla,reverse=True)

   return lista_valores[0]

moda= calculate_mode(listita)

print(moda[0])

def calculate_range(lista):
   max_value= max(listita)
   min_value= min(listita)
   return max_value-min_value

range_value = calculate_range(listita)
print(range_value)

def calculate_variance(listita,media):
   
   acumulador=0
   for i in listita:
    acumulador+= (i-media) **2

   return acumulador /len(listita)

media= calculate_median(listita)
variance =calculate_variance(listita,media)

print(variance)
   
def calculate_desvio(variance):
   return variance ** 0.5

print(calculate_desvio(variance))