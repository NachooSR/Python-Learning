#Dictionaries --> Like maps {"llava":"valor"}
empty_dictionary= {}
empty_dictionary= dict()

persona = {
    "Nombre":"Ignacio",
    "Apellido": "Reyna",
    "Telefono": 212332412,
    "Mail": "Nachito@gmail.com"
}

#print(persona["Nonvre"]) Error por llave inexistente
print(persona.get("Nonvre"),'\n')
print(persona.get("Nombre"),'\n')

persona["Nombre"] = "Juan" #Misma llave pisa el valor
persona["Dni"]="1234567"

print(persona,'\n' )

persona.pop("Dni")
print(persona,'\n' )

lista = persona.items() 
print(lista, '\n') #Lista de tuplas

llaves= persona.keys()
print(llaves,'\n')

#Exercises 
dog = dict()

dog["name"]="Mushu"
dog["color"]="Black"
dog["breed"]="Pug"
dog["legs"]=4
dog["age"]=4

student= {
    "first_name":"Pedro",
    "last_name":"Sanchez",
    "gender":"male",
    "age":19,
    "marital_status":"single",
    "skills": ["Go","Python","Sql"],
    "country":"Argentina",
    "city":"Mar del Plata",
    "address":"Isla pajaros 127"
}

print(len(student),'\n')

print(student.get("skills"),'\n')
print(type(student["skills"]),'\n')

skills_student= student.get("skills")

skills= skills_student + ["Java","Dart"]

student["skills"]= skills

#student["skills"]+= ["Java","Dart"]

print(student["skills"])

list_keys = list(student.keys())
print(list_keys, '\n')

list_values= list(student.values())
print(list_values,'\n' ) 

list_items=student.items()
print(list_items, '\n')

student.pop("marital_status")
print(student,'\n')

del student