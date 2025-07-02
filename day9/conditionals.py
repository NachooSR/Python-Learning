'''
age= int(input("Enter your age: ").strip())
if age >= 18:
    print("You are old enough to learn to drive")
else:
    print("You need " + str(18-age) +" years to learn to drive")

grade= float(input("Enter your grade: ").strip())

if grade >=0 and grade<= 49:
    print("F")
elif grade >=50 and grade <=59:
    print("D")
elif grade>=60 and grade <=69:
    print("C")
elif grade>=70 and grade <=79:
    print("B")
elif grade>=80 and grade <=100:
    print("A")
else:
    print("Invalid grade")


Summer= ["Diciembre","Enero","Febrero"]
Autumn= ["Marzo","Abril","Mayo"]
Winter= ["Junio","Julio","Agosto"]
Spring= ["Septiembre","Octubre","Noviembre"]

month= str(input("Enter month: ").strip())

if month in Summer:
    print("Summer season")
elif month in Autumn:
    print("Autum season")
elif month in Winter:
    print("Winter season")
elif month in Spring:
    print("Spring season")
else:
    print("Invalid month")


fruits = ['banana', 'orange', 'mango', 'lemon']
fruit= str(input("Enter fruit: ").strip())
if fruit in fruits:
    print("Fruit already exist")
else:
    fruits.append(fruit)
    print(fruits)
'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person.keys():
    middle = int( len(person['skills']) / 2)
    print(person["skills"][middle])
    if "Python" in person["skills"]:
        print("OMG, sabes python")


if set(person['skills']) == {'React','JavaScript'}:
   print("He is a front developer")
if {'Node', 'MongoDB', 'Python'}.issubset(person['skills']):
    print("He is a backend developer")

if person["is_marred"] and person["country"]== "Finland":
    print(f"{person["first_name"]} {person['last_name']} lives in {person["country"]}. He is married")