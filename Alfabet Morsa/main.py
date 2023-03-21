kod ={ 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '7':'--...',
                    '6':'-....', '8':'---..', '9':'----.',
                    '0':'-----'}
sl = []
for i in range(65,91):
    sl.append(chr(i))
for i in range(0,10):
    sl.append(i)

f = open("dane.txt","r")
d = open("dane1.txt","w")

def dekoduj():
    for line in f:
        line = line.replace("\n","")
        line = line.replace("   ",";")
        z = 0
        w = []
        wa = []
        for i in range(0,len(line)):
            if line[i] == ";" or line[i] == " ":
                w.append(line[z:i])
                z = i + 1
            if line[i] == ";":
                w.append(" ")
            if i == len(line)-1:
                w.append(line[z:i+1])
        for i in range(0,len(w)):
            if w[i] == " ":
                wa.append(" ")
            for b in range(0,len(kod)):
                if w[i] == kod[str(sl[b])]:
                    wa.append(sl[b])
        d.write("".join(wa))
        d.write("\n")
    f.close()
    d.close()

def koduj():
    for line in f:
        line = line.replace("\n", "")
        w = []
        wa = []
        for i in range(0, len(line)):
            if line[i] == " ":
                w.append(" ")
            else:
                w.append(str(line[i].upper()))
        for i in range(0, len(w)):
            if w[i] == " ":
                wa.append(" ")
            for b in range(0, len(kod)):
                if w[i] == sl[b]:
                    wa.append(kod[str(sl[b])])
        d.write(" ".join(wa))
        d.write("\n")
    f.close()
    d.close()

x = int(input("1 - Odszyfruj wiadomość\n2 - Zaszyfruj wiadomość\n"))
if x == 1:
    dekoduj()
else:
    koduj()

