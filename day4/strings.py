'''
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

full_name= "Ignacio"
print(full_name[::3])
'''

#string [inicio:fin:paso] --> como una especie de for

fullSequence= "Thirty" +" "+ "Days"+" "+"Of"+" "+"Python"
print(fullSequence)

company= "Coding For All"
print(company)

print("String length: ",len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.swapcase())


first=str( company.split()[1] )
print(first)


indice = company.index("Coding")

if indice != -1:
    print("Existe")
else:
    print("No existe")

newPhrase= company.replace("Coding","Python")
print(newPhrase)

string= "Python for Everyone"
newString= string.replace("Everyone","All")

print(company.split())

techCompanies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(techCompanies.split(','))

print(company[0])
print(company[len(company)-1])
print(company[9])
AcronymComplete= "Python For Everyone"

#List comprehension
acronym= '_'.join([word[0] for word in AcronymComplete.split()])
print(acronym)


cuadradosPares=[number**2 for number in range(1,21) if (number**2) %2 ==0]
print(cuadradosPares)

palabras = ['Nacho', 'código', 'Python', 'terminal', 'Argentina']

firstLetter= ','.join([palabra[0].upper() for palabra in palabras])

print(firstLetter)

print(company.index("F"))

sentence ='You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because",0))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start = sentence.find('because')
end = sentence.rfind('because') + len('because')
sliced = sentence[start:end]

sentence_without = sentence[:start] + sentence[end+1:]
print(sentence_without)

print(company.startswith("Coding"))
print(company.endswith("All"))

company2= '   Coding For All      '  
print(company2.strip())