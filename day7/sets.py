# sets no son ordenados
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#  ,'\n'

print(len(it_companies),'\n')

it_companies.add("Twitter")
it_companies.update(["Globant","Accenture","Kick"])

print(it_companies,'\n')

it_companies.remove("Google")

print(it_companies,'\n' )

'''
Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
'''

C= A.union(B)

print(C,'\n')

print(A.intersection(B), '\n' )
print(A.issubset(B),'\n')
print(A.isdisjoint(B), '\n')

print(A.symmetric_difference(B))

del A
del B

print(len(age),'\n' )
age_to_set= set(age)

print(len(age_to_set),'\n')

frase ="I am a teacher and I love to inspire and teach people"
palabras = frase.split()
palabras = set(palabras)

print(len(palabras),'\n' )
print(palabras,'\n')

