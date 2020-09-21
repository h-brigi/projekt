"""
# összeadás +
# kivonás -
# szorzás *
# osztás /
# maradékképzés %
# hatványozás ** (3**2 három a második hatványon)

Operátorok
> and és 
> or vagy
> not tagadás

Relációs operátorok
>, <, >=, <=, ==, !=
"""

print("maradványérték", 5 % 2)
print("hatványozás", 3**2) 
szam=5
print(szam>3 or szam>5)
print(szam>3 and szam<5)
print(not szam>3)

#sztring valósság konvertálása
a="123.12345"
float(a)

szamstr = "343.34521" 
szam=float(szamstr)
print("Szám: ", szam*2)          #686.69042

#sztring egésszé
a="123.12345"
int(float(a))

szamStr = "343.34521"
szam = int(float(szamStr))
print("Szám: ", szam*2)          #686

szamStr = "345"   
szam = int(szamStr)
print("Szám: ", szam*2)          # 690

szam = 345
szamStr = str(szam)
print("Szám: ", szamStr + " db")  # 345 db

szam = 345.12345
szamStr = str(szam)
print("Szám: ", szamStr + " kg")






