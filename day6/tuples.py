'''
-Create an empty tuple
-Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
-Join brothers and sisters tuples and assign it to siblings
-How many siblings do you have?
-Modify the siblings tuple and add the name of your father and mother and assign it to family_members
'''


emptyTuple = ()
sisters=("Maria Luz","Ambar","Sofia")
brothers= ("Juan","Federico")

siblings= brothers + sisters
print("I have: " +str(len(siblings))+" siblings")

siblings= list(siblings)
siblings.append("Lorena")
siblings.append("Gustavo")

family_members= tuple(siblings)

print(family_members)

siblings,parents = family_members[0:5],family_members[5:]

print(siblings)
print(parents)

fruits=("Banana","Manzana","Naranja")
vegetables=("Lechuga","Tomate","Papa")
animal_products=("Queso","Leche","Yogurth")

food_stuff_tp= fruits +vegetables + animal_products
food_stuff_lt=list(food_stuff_tp)


middleItem = int(len(food_stuff_tp)/2)
if len(food_stuff_tp)%2 !=0:
   middleStuff= food_stuff_tp[middleItem]
else:
   middleStuff= food_stuff_tp[middleItem-1:middleItem+1]

print(middleStuff,'\n')

firstThree=food_stuff_lt[0:3]
lastThree=food_stuff_lt[len(food_stuff_lt)-3:len(food_stuff_lt)+1]

print(firstThree, '\n')
print(lastThree, '\n')

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

EstoniaExist = ("Estonia" in nordic_countries)
IcelandExist =("Iceland" in nordic_countries)

print(EstoniaExist,'\n')
print(IcelandExist,'\n')