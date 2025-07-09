'''
Write a function called is_prime, which checks if a number is prime.

Write a functions which checks if all items are unique in the list.

Write a function which checks if all the items of the list are of the same data type.

Write a function which check if provided variable is a valid python variable

Go to the data folder and access the countries-data.py file.

Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order

Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
'''

def is_prime(number):
    if number<2:
        return False
    for i in range(2, int(number**0.5 +1)):
        if (number) %i==0:
            return False
    return True

print(is_prime(1301))

print('\n')

def unique_items(lista):
    return len(lista) == len(set(lista))

lista_test= [1,2,3,4,5,2]
print(unique_items(lista_test))
