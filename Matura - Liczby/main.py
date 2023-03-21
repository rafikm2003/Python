f = open("liczby.txt","r")
d = open("wyniki4.txt","w")
t = []
zad1 = 0
zad2 = []

pierw = []
dl = []
nwd = []

dzg = []
dzd = []

dlp = 0
for i in range(0,100):
    if (3**i) > 100000:
       break
    else:
        t.append(3**i)

for line in f:
    line = line.replace("\n","")
    pierw.append(int(line))
    for i in range(0,len(t)):
        if int(line) == t[i]:
            zad1 = zad1 + 1
    w = []
    wd = []
    for i in range(0,len(line)):
        w.append(int(line[i]))

    for b in range(0,len(w)):
        sum = 1
        for i in range(1,w[b]+1):
            sum = sum * i
        wd.append(sum)
    z = 0
    for i in range(0,len(wd)):
        z = z + wd[i]
    if z == int(line):
        zad2.append(line)


dlp = 1
for i in range(0,len(pierw)):

    dzio = []
    dzd = []

    if dlp > 1 and pierw[i] != 1:
        for b in range(pierw[i], 1, -1):
            if int(pierw[i]) % b == 0:
                dzd.append(b)
        for c in range(0, len(dzg)):
            for b in range(0, len(dzd)):
                if dzg[c] == dzd[b]:
                    dzio.append(dzg[c])

    if len(dzio) == 0 and dlp >1:
        dl.append(dlp)
        dlp = 1
        nwd.append(max(dzg))
    if len(dzio) > 0 and dlp > 1:
        dlp = dlp + 1
        dzg = dzio

    if dlp == 1 and pierw[i] != 1:
        dzg = []
        for b in range(pierw[i], 1, -1):
            if pierw[i] % b == 0:
                dzg.append(b)
        dlp = dlp + 1



    if pierw[i]==1 or i == 499:
        dl.append(dlp)
        dlp = 1
        nwd.append(max(dzg))

ma = 0
for i in range(1,len(dl)):
    if dl[i]>dl[ma]:
        ma = i


d.write(str(zad1))
d.write("\n")
d.write(" ".join(zad2))
d.write("\n")

zad3 = []
zad3.append(str(pierw[ma]))
zad3.append(str(dl[ma]))
zad3.append(str(nwd[ma]))
d.write(" ".join(zad3))
f.close()
d.close()



