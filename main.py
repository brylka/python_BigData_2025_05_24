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

slowa = ['oko', 'python', 'civic', 'Kamil Ślimak', 'witaj']

for slowo in slowa:
    przygotowane_slowo = slowo.lower().replace(" ", "")
    if przygotowane_slowo == przygotowane_slowo[::-1]:
        print(f"Słowo {slowo} jest palindromem")
    else:
        print(f"Słowo {slowo} NIE jest palindromem")

# kamil = "    Kamil Ślimak"
# print(":" + kamil.upper().replace(" ", ""))
