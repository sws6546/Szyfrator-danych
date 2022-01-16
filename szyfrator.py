pplik = input("Podaj ścieżkę do pliku: ")

def pobieranie(plik):
    plik = open(plik, 'r')
    try:
        tekst = plik.read()
    finally:
        plik.close()
    return tekst

def zapisywanieDoPliku(plik, tresc):
    plik = open(plik, 'w')
    plik.write(tresc)
    plik.close()

def szyfrowanie(tresc):
    napis = tresc

    asciii = []
    for i in napis:
        asciii.append(ord(i))

    klucz = input("Podaj klucz wariacie: ")
    klucz_liczba = 0
    for i in klucz:
        klucz_liczba += ord(i)
    
    zaszyfrowanyNapis = []
    for i in asciii:
        zaszyfrowanyNapis.append(chr(i + klucz_liczba))
    
    napis = ""
    for i in zaszyfrowanyNapis:
        napis += i
    return napis

def deszyfracja(szyfr):
    napis = szyfr

    asciii = []
    for i in napis:
        asciii.append(ord(i))

    klucz = input("Podaj klucz wariacie: ")
    klucz_liczba = 0
    for i in klucz:
        klucz_liczba += ord(i)
    
    odszyfrowanyNapis = []
    for i in asciii:
        odszyfrowanyNapis.append(chr(i - klucz_liczba))

    napis = ""
    for i in odszyfrowanyNapis:
        napis += i
    return napis

wybor = input("Co chcesz zrobić [s] = szyfruj, [o] = odszyfruj: ")
if wybor == "s":
    tresc = pobieranie(pplik)
    szyfr = szyfrowanie(tresc)
    zapisywanieDoPliku(pplik, szyfr)
if wybor == "o":
    tresc = pobieranie(pplik)
    szyfr = deszyfracja(tresc)
    zapisywanieDoPliku(pplik, szyfr)
