def przyznaj(l,w):
    for user in range(0,len(l)):
       w.append(input("Podaj wiek "+l[user]+":"))
    return(w)

def doko(l,w):
    s = "brać udział w wyborach"
    s1 = "brać udziału w wyborach"
    d1 = []
    d2 = []

    m1 = "może"
    m2 = m1

    for i in range(0,len(l)):
        if int(w[i]) > 17:
            d1.append(m[i])
        else:
            d2.append(m[i])
    if len(d1)>1:
        m1 = "mogą"
    if len(d2) > 1:
        m2 = "mogą"

    se = ", "
    if len(d1)>0:
        print(se.join(d1),m1,s)

    if len(d2) > 0:
        print(se.join(d2),"nie",m2,s1)


m = ["Karolina","Alicja","Jakub","Kacper"]
l = ["Karoliny","Alicji","Jakuba","Kacpra"]
w = []

przyznaj(l,w)
doko(l,w)
