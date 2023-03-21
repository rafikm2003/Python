p = input("Podaj pesel: ")
while len(p)!=11:
    p = input("Podano pesel złej długości\nUpewnij się że nie występują w nim spacje ani inne znaki\nPodaj pesel:")

z = int(p[7])
w = str(1379137913)
suma = 0
i = 0

if z%2==0:
    print("Pesel należy do kobiety")
else:
    print("Pesel należy do mężczyzny")
while i!= 10:
    u = str(int(p[i]) * int(w[i]))
    u = u[-1]
    u = int(u)
    suma = suma + u
    i=i+1

print("Liczba kontrolna tego peselu to:",p[-1])
suma = str(suma)
d = int(suma[-1])
c = int(p[-1])

if 10-d == c:
    print("Podany pesel jest zgodny z liczbą kontrolną\n(Podana liczba kontrolna jest prawidłowa)")
else:
    print("Podany pesel nie jest zgodny z liczbą kontrolną\n(Podana liczba kontrolna jest nieprawidłowa)")

