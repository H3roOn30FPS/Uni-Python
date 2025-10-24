#Програма за намиране на Лице на Окръжност
import math

r = float(input("Въведете радиус на Окръжността: "))
from math import pi

Area = pi * math.pow(r, r)
#Alternativly:: Area = pi * (r * r)
#Alternativly:: Area = pi * r**2

print(f"Лицето на кръга е: {Area:.2f} м.ед.^2")