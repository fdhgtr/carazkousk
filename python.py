import random
pole = [1,22,13,45,9,61,37,89,4,]
print(pole)


prvni = pole[0]
prostedni = pole[len(pole) // 2]
posledni = pole[-1]

print("první hodnota:", prvni)
print("prostřední hodnota:", prostedni)
print("poslední hodnota:", posledni)

pole[5]=34
print(pole)

pole7 = pole[7]
print( pole7)


print(len(pole))
#minimální a maximální hodnota obou pole A
print(min(pole))
print(max(pole))
pole1 = [6,2,10,15,7,9,11,4,3,1]
print(pole1)


pole1 = [6,2,10,15,7,9,11,4,3,1]
print(pole1)

pole1[3]=4
print(pole1)
#sečtení obou polí a délka obou polí
print(sum(pole+pole1))
print(len(pole+pole1))


#minimální a maximální hodnota obou dvou polí
print(min(pole + pole1))
print(max(pole + pole1))

pole_auto=list(range(1,51))
random.shuffle(pole_auto)
print(pole_auto)
print(sum(pole))