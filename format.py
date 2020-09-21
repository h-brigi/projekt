#formázott értékek formátum sztringgel
#formátumkód mindig %-karakterrel vezetjük be, ezt követi a formátumkarakter
#formátumkarekter: d - , f- , c- , s- stb.
szam=3
print("Szám: %10d" % szam) #10.helyen\spacecel\ iratjuk ki
print("Szám: %3.2f" % szam) #valós szám két tizedesjegy pontosággal, 3. helyen ábrázolva
print("Szám: %4c" % szam) #karakter?
print("Szám: %10s " % szam) #


print('{} {}'.format(48,840000)) #format függvény
print('{} kg {} Ft'.format(48,840000))


print('{:>20}'.format(8400000)) #20.helyen végződő  balra igazítottkiírás
print('{:20}'.format(8400000)) 


print('{:_>10}'.format('8400000'), "balra")
print('{:_<10}'.format('8400000'), "jobbra")
print('{:^10}'.format('8400000'), "középre igazított")

#Mennyiség: 16 kg
gyumolcs="Mennyiség:{} kg"
print(gyumolcs.format(16))

#Mennyiség: 16 kg Ár: 840  Ft
gyumolcs = "Mennyiség: {} kg Ár: {} Ft"
print(gyumolcs.format(16,840))

#Tizedesjegyig való kerekítés
gyumolcs = "Mennyiség: {} kg Ár: {:.2f} Ft"
print(gyumolcs.format(16, 840.12345))

#Szélesség megadása
gyumolcs = "Mennyiség: {:10d} kg Ár: {:10d} Ft"
print(gyumolcs.format(16, 840))

#vezető nulla a 10. helyre való kiírás mellett
gyumolcs = "Ár: {:010d} Ft"
print(gyumolcs.format(840))

#ezredes tagolás
gyumolcs = "Ár: {:,d} Ft"
print(gyumolcs.format(8400000))

#előjel
gyumolcs = "Ár: {:+10d} Ft"
print(gyumolcs.format(8400000))

#sorrend megadása 
szoveg = "Az ő neve {1}. {1} életkora: {0}"
print(szoveg.format(34, "Mari")) #Az ő neve Mari. Mari életkora: 34







