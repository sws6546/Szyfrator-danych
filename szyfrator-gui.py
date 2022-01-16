import tkinter
from tkinter import filedialog as fd
from traceback import print_tb

def szyfrowanie():


    def szyfru():
        klucz = kluczPole.get()
        print(klucz)
        
        def pobieranie():
            plik = open(filename, 'r')
            try:
                tekst = plik.read()
            finally:
                plik.close()
            return tekst

        tresc = pobieranie()

        napis = tresc

        asciii = []
        for i in napis:
            asciii.append(ord(i))

        klucz_liczba = 0
        for i in klucz:
            klucz_liczba += ord(i)
            
        zaszyfrowanyNapis = []
        for i in asciii:
            zaszyfrowanyNapis.append(chr(i + klucz_liczba))
        
        napis = ""
        for i in zaszyfrowanyNapis:
            napis += i
        print(napis)

        def zapisywanieDoPliku(filename, napis):
            plik = open(filename, 'w')
            plik.write(napis)
            plik.close()

        zapisywanieDoPliku(filename, napis)


    szyfr_gui = tkinter.Tk()

    etykietkaSzyfru = tkinter.Label(szyfr_gui, text="Wybierz plik do zaszyfrowania, i podaj klucz szyfru")
    etykietkaSzyfru.pack()

    filename = fd.askopenfilename()

    file_path_etykietka = tkinter.Label(szyfr_gui, text=f"{filename}")
    file_path_etykietka.pack()

    kluczPole = tkinter.Entry(szyfr_gui)
    kluczPole.pack()

    btn = tkinter.Button(szyfr_gui, text="zatwierdź", command=szyfru).pack()

    szyfr_gui.mainloop()

def deszyfrowanie():



    def deszyfru():
        def pobieranie(plik):
            plik = open(plik, 'r')
            try:
                tekst = plik.read()
            finally:
                plik.close()
            return tekst
        tresc = pobieranie(filename)
        napis = tresc

        asciii = []
        for i in napis:
            asciii.append(ord(i))

        klucz = kluczPole.get()
        klucz_liczba = 0
        for i in klucz:
            klucz_liczba += ord(i)

        odszyfrowanyNapis = []
        for i in asciii:
            odszyfrowanyNapis.append(chr(i - klucz_liczba))
        napis = ""
        for i in odszyfrowanyNapis:
            napis += i
        
        def zapisywanieDoPliku(filename, napis):
            plik = open(filename, 'w')
            plik.write(napis)
            plik.close()

        zapisywanieDoPliku(filename, napis)



    deszyfr_gui = tkinter.Tk()

    etykietkaSzyfru = tkinter.Label(deszyfr_gui, text="Wybierz plik do zaszyfrowania, i podaj klucz szyfru")
    etykietkaSzyfru.pack()

    filename = fd.askopenfilename()

    file_path_etykietka = tkinter.Label(deszyfr_gui, text=f"{filename}")
    file_path_etykietka.pack()

    kluczPole = tkinter.Entry(deszyfr_gui)
    kluczPole.pack()

    btn = tkinter.Button(deszyfr_gui, text="zatwierdź", command=deszyfru).pack()



root = tkinter.Tk()

etykietka = tkinter.Label(root, text=" Szyfrator danych by Szymon z Wrocławia. \nWeź chłopie zaznacz co chcesz zrobić ok?")
etykietka.pack()

szyfrowanie = tkinter.Button(root, text="Szyfrowanie", command=szyfrowanie)
szyfrowanie.pack()

rozszyfrowanie = tkinter.Button(root, text="Rozszyfrowanie", command=deszyfrowanie)
rozszyfrowanie.pack()

root.mainloop()