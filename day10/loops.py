# Ciclos While y for
import countries_list, countries_data

'''

'''
number= 0

for i in range (0,11,1):
    print(i)

while number<=10:
    print(number)
    number +=1

for i in range(1,8):
    print("#" * i)

print("***************",'\n')    

for i in range(0,7):
    for j in range (0,7):
        print("#" ,end=' ')
    print("\n")

for i in range (0,11):
    print(f"{i} x {i} = {i*i}")

tech_skills= ['Python', 'Numpy','Pandas','Django', 'Flask']

for it_skill in tech_skills:
    print(it_skill, end=' ') 

def even_number(number):
    return number%2==0

print('\n')
for i in range(0,101):
    if even_number(i):
        print(i)

for i in range(0,101):
    if not even_number(i):
        print(i)

acumulador=0
for i in range (0,101):
    acumulador+=i
print(f"\nThe sum of all numbers is {acumulador}\n")

ac_even,ac_odds= 0,0

for i in range (0,101):
    if even_number(i):
        ac_even+=i
    else:
        ac_odds+=i

print(f"The sum of all evens is {ac_even}.And the sum of all odds is {ac_odds}\n")


############################


land_countries=list()

for country in countries_list.countries:
    if "land" in country:
        land_countries.append(country)

print(land_countries)

#land_countries= [country for country in countries if "land" in country]


fruits= ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruits)-1,-1,-1):
    print(fruits[i])

'''
-What are the total number of languages in the data
-Find the ten most spoken languages from the data
-Find the 10 most populated countries in the world

'''

#Excercise 1
lenguajes = set()

for country in countries_data.countries_data:
   for language in country.get("languages"):
       lenguajes.add(language)

print(f"There is {len(lenguajes)} languages",'\n')

#Excercise 2
lenguajes_spoken= {}

for country in countries_data.countries_data:
    for language in country.get("languages"):
        if language in lenguajes_spoken:
            lenguajes_spoken[language]+=1
        else:
            lenguajes_spoken[language]=1

def valor_ordenar(tupla):
    return tupla[1]

lista_countries= list(lenguajes_spoken.items()) #Convertir a lista el dict

lista_countries = sorted(lista_countries,key= valor_ordenar,reverse=True)
top_ten_spoken= lista_countries[:10]

print(top_ten_spoken,'\n' )

#Exercise 3
population_countries= {}

for country in countries_data.countries_data:
    population_countries[country["name"]]= country["population"]

list_population= list(population_countries.items())
list_population= sorted(list_population,key=valor_ordenar,reverse=True)

ten_population= list_population[:10]
print(ten_population,'\n')