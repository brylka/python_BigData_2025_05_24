zmienna1            = 3            # int - liczba całkowita
zmienna2 = 3.14         # float - liczba zmiennoprzecinkowa
zmienna3 = 'Witaj'       # string - łańcuch znaków
zmienna4 = True         # bool - prawda/fałsz True False

# print("ALA " + zmienna3 + ' ' + str(zmienna2))
# print("ALA", zmienna3, zmienna2)
# print(f"ALA {zmienna3} {zmienna2}")

# #print("Ala", "ma", "kota", sep="-!-")
# print("Ala", end="\t")
# #coś jeszcze
# print("ma", end="\n")
# #....
# print("kota")

# name = input("Podaj swoje imie: ")
# print(f"Witaj {name}")

# a = float(input("Podaj liczbę a: "))
# b = float(input("Podaj liczbę b: "))
# c = a + b
# print(f"Wynik dodawania: {c:.2f}")

# if a > 10:
#     print("Zmienna jest większa od dziesięciu")
# elif a < 10:
#     print("Zmienna jest mniejsza od dziesięciu")
# else:
#     print("Zmienna jest równa dziesięć")
#
# print("Kolejna linijka")
#
# a = -10
# b = -11
#
# if a > 0 and b > 0:
#     print("Oblie liczby są dodatnie")
# elif a > 0 > b:
#     print("Liczba a + i b -")
# elif a < 0 and b > 0:
#     print("Liczba a - i b +")
# elif a < 0 and b < 0:
#     print("Liczby są ujemne")
#lista = range(10)
# #        0  1    2  3   4 5 6 7 8 9
# lista = [0,"ala",2,3.14,4,5,6,7,8,9]
# string = "Ala ma kota"
# #print(lista[1:7:2])
#
# for i in string[::-1]:
#     print(i, end=", ")

# slowa = ['oko', 'python', 'civic', 'Kamil Ślimak', 'witaj']
#
# for slowo in slowa:
#     przygotowane_slowo = slowo.lower().replace(" ", "")
#     if przygotowane_slowo == przygotowane_slowo[::-1]:
#         print(f"Słowo {slowo} jest palindromem")
#     else:
#         print(f"Słowo {slowo} NIE jest palindromem")

# kamil = "    Kamil Ślimak"
# print(":" + kamil.upper().replace(" ", ""))

# lista1 = []
# lista2 = [1,2,3,4,5]
# lista3 = list(range(1,6,1))
# lista4 = [1, 2] * 10
# #print(lista4)
#
# #print("Witaj świecie!\n" * 10)
#
# lista = [2,3,4,5,3]
# lista2 = ['kamil', 'ślimak']
# print(lista)
# lista.append(6)             #dodaje element na konec lista
# print(lista)
# lista.insert(2, "ala")  #dodaje element pod wskazany index
# print(lista)
# lista.extend(lista2)        #dodaje inną listę do list
# print(lista)
# lista.remove(3)             #kasuje pierwsze wystąpienie elementu
# print(lista)
# lista.pop()                 #kasuje ostatni element
# print(lista)
# lista.pop(1)                #kasuje element o indexie
# print(lista)
# lista.clear()               #czyści listę
# print(lista)
#
# lista = [5,2,-5,4,99,0]
# print(lista)
# lista.sort(reverse=True)    # sortuje listę zgodnie z "matematyką"
# print(lista)
# print(len(lista))           # ilośc elementów list

# print(lista[-2])

# lista3 = [5,2,-5,4,99,0]
# slownik3 = {0:5, 1:2, 2:-5, 3:4, 4:99, 5:0}
# print(lista3[4])
# print(slownik3[4])

# slownik = {"imie": "Bartosz", "nazwisko": "Bryniarski", "adres": "Wrocław"}
# slownik["wiek"] = 45
# print(slownik)

# cos = {"a": 3, "PI": 3.14, "lista": [4,3,[4,5,{"t":4,"s":"mmm"},6],3.14,"ala"], 7:"Bartosz"}
#
# print(cos["lista"][2][2]["s"])

# for a in range(0,11):
#     for b in range(0,11):
#         if a == 0 and b == 0:
#             print("\033[31m*\033[0m", end="\t")
#         elif a == 0:
#             print("\033[31m", b, "\033[0m", sep="", end="\t")
#         elif b == 0:
#             print("\033[31m", a, "\033[0m", sep="", end="\t")
#         elif a == b:
#             print("\033[32m", a*b, "\033[0m", sep="", end="\t")
#         else:
#             print(a*b, end="\t")
#     print()

# lista = []
# for _ in range(5):
#     a = int(input("Podaj liczbę: "))
#     lista.append(a)
# lista = []
# podawaj = True
# while podawaj:
#     a = input("Podaj liczbę (1,2,3,4,5,6 lub x aby zakończyć): ")
#     if a == 'x':
#         podawaj = False
#     else:
#         lista.append(int(a))
#
#
# print(lista)
#
# suma = 0
# for liczba in lista:
#     suma += liczba
#
# srednia = suma / len(lista)
# print(f"Średnia: {srednia}")

def witaj(imie, ok=True):
    print(f"Witaj {imie}!")
    if ok:
        print("Miło mi Cię widzieć!!!!!")
    else:
        print("Do zobaczenia!!!!!!")

if __name__ == "__main__":
    witaj("Paweł")