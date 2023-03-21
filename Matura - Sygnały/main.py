f = open("sygnaly.txt","r")
s = 1
ha = []
li = []
lik = []
kod = []
w = 0
zad3 = []
z = 0
for line in f:
    if s%40 == 0:
        ha.append(line[9])
    s = s + 1
    li.append(line)

    for i in range(0,len(line)-1):
        kod.append(line[i])


    for i in range(65,91):
        x = kod.count(chr(i))
        if x > 0:
            z = z + 1
            x = 0
    lik.append(z)
    z = 0
    kod = []

    for i in range(0,len(line)-1):
        for b in range(0,len(line)-1):
            if(abs(ord(line[i])-ord(line[b])))>10:
                w = w + 1


    if w==0:
        zad3.append(line)
    w = 0


m = i - 1
for i in range(1,len(lik)-1):
    x = lik[m]
    if lik[i] > lik[m]:
        m = i
        z = i

li[z] = li[z].replace("\n","")
print("Odpowiedź 1:","".join(ha))
print("Odpowiedź 2:",li[z],lik[z])
print("Odpowiedź 3:"+" \n"+"".join(zad3))

f.close()