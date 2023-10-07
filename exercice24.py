nombre=int(input("Donner un nombre SVP : "))

somme=0

while nombre<0 :
    nombre=int(input("Donner un nombre SVP (positif ou null): "))

for i in range(0,nombre+1):
    somme=somme+(10**i)

print("la somme est ",somme)