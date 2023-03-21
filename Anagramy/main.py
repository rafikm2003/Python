tab = []
na = []
name = "R"
b = 0

f = open("dane.txt","r")
d = open("wynik.txt","w")



for line in f:
    line = line.replace("\n","")
    for i in range(0,256):
        name = name + str(line.count(chr(i))) + ":"
    tab.append(name)
    na.append(line)
    name = "R"


wyp = []
wypl = []
wypk = []
x = 0
y = 0
z = 0

for a in range(0,len(na)):
    for b in range(0,len(na)):
        for c in range(0,len(wypl)):
            if a == wypl[c]:
                x = x + 1
            if b == wypl[c]:
                y = y + 1
        if a!=b and x == 0 and tab[a] == tab[b]:
            wyp.append(a)
            wypl.append(a)
        if a!=b and y == 0 and tab[a] == tab[b]:
            wyp.append(b)
            wypl.append(b)
        x = 0
        y = 0
    for i in range(0,len(wyp)):
        wypk.append(na[wyp[i]])
    for i in range(0,len(wypl)):
        if a == wypl[i]:
            z = z + 1
    if z == 0:
        d.write(name[a]+"\n")
        z = 0
    if len(wyp)>1:
        d.write(" ".join(wypk)+"\n")
    wypk = []
    wyp = []

f.close()
d.close()