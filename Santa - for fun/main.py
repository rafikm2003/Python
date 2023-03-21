import sys
import random
h = int(input("Proszę podać wysokość pierwszej gałęzi:"))
p = int(input("Proszę podać ilość gałęzi:"))

if h==1 and p==1:
    print("\nWidziałeś ty kiedyś taką małą choinkę?\nMikołaj nigdy do nas nie dotrze.\nPostaraj się następnym razem co?")
    sys.exit(0)

o=0
x=int(p-1)




filepath = "santa.txt"
f = open(filepath, "r")
print(f.read())

print((h-1+x)*" "+"*")

while o!=p:

    if (p*h)<30:
        f.readline()=="0"
    for i in range(h-2,0,-1):

        random.seed()
        maximum = ((2 * h - 3) - (2 * i) + (2 * o)-1)
        m = int(random.random() * maximum)

        if m==0:
            print((i + x) * " " + "/" + ((2 * h - 3) - (2 * i) + (2 * o)) * " " + "\\")
        else:
            print((i + x) * " " + "/" + ((2 * h - 3) - (2 * i) + (2 * o) - m) * " " + "°" + (m - 1) * " " + "\\")

    print(x*" "+(h+o)* "* ")
    o=o+1
    x=x-1

c=len((h+o)* "* ")
c=(c-5)/2

for i in range(0,p,1):
    if p<4:
        x= ""
    else:
        if i==1 or i==3:
            x = "  ==============="
        elif i==2:
            x = "  WESOŁYCH ŚWIĄT!"
        else:
            x = ""
    print(int(c)*" " + "|" + " " + "|",x)
    i=i+1
