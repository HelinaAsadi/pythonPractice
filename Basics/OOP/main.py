# classes work as a blueprint for our objects

from guitar import Guitar

guitar1 = Guitar("mc-128s", "Martinez" , "classical")
print(guitar1.model)
print(guitar1.brand)
print(guitar1.type)
guitar1.sound()