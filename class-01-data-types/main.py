# Primitive Types

milk = "Leite Desnatado"
volume = 2.5

print(type(milk))
print(type(volume))

preparation1 = volume + 1
preparation2 = milk + "10"

print(preparation1)
print(preparation2)

life_cat = str(volume + 5)

print("O gato bebe " + milk)
print("E tem " + life_cat + " vidas")

print("O gato bebe " + milk + " e tem " + life_cat + " vidas")
print(f"O gato bebe {milk} e tem {life_cat} vidas")

name = "Odilon"
age = 31
is_admin = False # Boolean True or False 

print(is_admin)
print(type(is_admin))

# Structures Types (Collections)

animes = ["Dragon Ball", "Naruto", "Jojo", "Death Note"]
#      =>       0              1        2         3
#      <=      -4             -3       -2        -1

print(animes)
print(type(animes))
print(animes[0])
print(animes[3])
print(animes[-1])

list = ["A", 123, True, ["B", "C"]]

print(list[0])
print(list[3])
print(list[3][1])
print(list[3][0])
print(list[-1])
print(list[-1][-1])
print(list[-1][-2])

list[2] = False
list[-1][0] = "D"
print(list)
print(len(list)) # length

# tuple 

tuple = ("A", 123, True)
print(tuple[1])
print(type(tuple))

#tuple[1] = 798 # tuple is immutable

#print(tuple) # Retorna um erro

# dict 

dict = {
    "name": "Odilon",
    "age": 18,
    "is_admin": True
}

print(dict)
print(type(dict))

print(dict["name"])
print(dict["age"])
print(dict["is_admin"])