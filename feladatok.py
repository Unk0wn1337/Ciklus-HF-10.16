def elsoFela(szam):
    index: int = 0
    while index < szam:
        if index % 2 == 1:
            if index < szam - 1:
                print(index, end=",")
            else:
                print(index, end="")
        index += 1


def masodikFela(szam):
    index: int = 1
    if szam < 0:
        print("HIBA: Parameterben a szam nem lehet 0")
    else:
        while index < szam:
            if index < szam - 1:
                print(index, end=";")
            else:
                print(index, end="")
            index += 1


def harmadikFela():
    szam: int = int(input("Szeretnek kerni egy 5-el oszthato szamot: "))
    while not szam % 5 == 0:
        szam: int = int(input("Szeretnek kerni egy 5-el oszthato szamot"))

def negyedikFela(szam):
    index = 1
    while index <= szam:
        if index % 3 == 0:
            print("BUUM",end="" if index == szam else ';')
        elif index % 2 == 0:
            print("BAM",end="" if index == szam else ';')
        else:
            print(index,end=""if index == szam else ' ')
        index+=1