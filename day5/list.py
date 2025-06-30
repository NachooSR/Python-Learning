
emptyList = ()
listBiggerThanFive=(2,3,4,5,6,7)
print(emptyList)

print(len(listBiggerThanFive))

firstItem= listBiggerThanFive[0]
lastItem= listBiggerThanFive[len(listBiggerThanFive)-1]

middle = int( len(listBiggerThanFive)/2)
middleItem = listBiggerThanFive[middle]

print("Primer Item: ",firstItem)
print("Item del Medio: ",middleItem)
print("Ultimo item: ",lastItem)

mixed_data_types= ("Ignacio",22,1.80,"Soltero","Isla Pajaros 127")

it_companies= ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

print(it_companies)
print("There is:",len(it_companies),"companies" )
print("First company: ",it_companies[0])
print("Last company: ",it_companies[len(it_companies)-1])
middleCompany=int(len(it_companies) /2) 
print("Middle company: ",it_companies[middleCompany])

it_companies.append("Globant")
print(it_companies,'\n')

middleCompany=int(len(it_companies) /2)
it_companies.insert(middleCompany,"Accenture")
print(it_companies,'\n')

print(it_companies[0].upper(),'\n')

newList = '#;'.join(company for company in it_companies)
print(newList,'\n')

print("Facebook" in it_companies,'\n')

it_companies.sort()
print(it_companies,'\n')

it_companies.reverse()
print(it_companies,'\n')

ThreeCompanies= it_companies[0:3]
print(ThreeCompanies,'\n')

ThreeLastCompanies= it_companies[len(it_companies)-3:len(it_companies)]

print(ThreeLastCompanies,'\n')

#Slice out the middle IT company or companies from the list

it_companies.append("EAsports")

print(it_companies,'\n')

#Si la cantidad de items es impar, remueve solo uno
if len(it_companies) %2 !=0:
   middle= int(len(it_companies)/2)
   middlesCompanies = it_companies.pop(middle)
else:
   middle= int(len(it_companies)/2)
   middlesCompanies = it_companies[middle-1: middle+1]

   

print(middlesCompanies,'\n')

del it_companies[0]
print(it_companies,'\n')

del it_companies[::]
print(it_companies)

'''
remove --> remueve datos de la lista
clear --> Vacia la lista
del --> la puede borrar por completo, asi como la referencia a su espacio de memoria asignado
'''

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

print(full_stack)

positionInsert= full_stack.index("Redux")

itemsInsert=['Python','SQL']

full_stack[positionInsert+1:positionInsert+1]=itemsInsert

print(full_stack,'\n')

#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

maxAge= max(ages)
minAge=min(ages)

ages.append(maxAge)
ages.append(minAge)

ages.sort()

print(ages)

middle= int(len(ages) /2)
if(len(ages)%2==0):
   media = (ages[middle-1] + ages[middle]) /2
else:
   media = ages[middle]

print(media)

promedio= sum(ages) / len(ages)

print(promedio)

countries= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1,country2,country3, *scandicCountries=countries
print(country1)
print(country2)
print(country3)
print(scandicCountries)



