#Cerinta: Scrieți un program care va determina valoarea ipotenuzei unui triunghi dreptunghic, valorile catetelor citindu-se de la tastatură.

#Rezolvare:
import math
cateta1 = input("Valoarea catetei 1 este:")
a=int(cateta1)
cateta2 = input("Valoarea catetei 2 este:")
b=int(cateta2)
z = math.sqrt(a ** 2 + b ** 2)
print(z)
