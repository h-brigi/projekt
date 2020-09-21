import math
print(math.sqrt(9)) #sqrt gyökvonás

from math import sqrt #statikus importálása a gyökvonás függvénynek
print(sqrt(9))

#gyökvonás és sin függvény importálása
from math import sqrt, sin, pi
print(sqrt(9))
print(sin(1*pi/180))

#összes függvény importálása
from math import *

#hatványozás
import math
print(math.pow(2,8))
print(math.pow(2,3))

#véletlen szám generálás --> randrange függvénnyel
#importáljuk a random modult
import random
# szintaxis:  random.randrange([start,] stop[, step])
print(random.randrange(6)) #0-5ig generál véletlen számokat - 6 mint felső korlát
print(random.randrange(10, 15)) #megadható also és felso korlat is

import random
for szam in range(20): #megadjuk hányszor hajtsa végre a feladatot
	print(random.randrange(3))

#a randrange elfogad egy harmadik paramétert (3\also hatar\, 13\felső határ\, 3\hárommal osztható"
for szam in range(10):
	print(random.randrange(3,13,3))

#random randint/a,b/ N számmal, 
print(random.randint(1,6)) #1-6ig szám előállítása

for szam in range(1, 6):
	print(random.randrange(3))
	
seq="abcd"
print(random.choice("abcd")) #választ egy elemet a sorozabol és azt írja ki

