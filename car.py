class Samochod:
    def __init__(self, marka, kolor="Kolorowy"):
        self.marka = marka
        self._kolor = kolor
        self.predkosc = 0
        print(f"Samochód {self.marka} koloru {self._kolor} wita")
    def przedstaw_sie(self):
        print(f"Jestem samochodem {self.marka}")
    def przyspiesz(self):
        self.predkosc += 10
        print(f"Samochód {self.marka} przyspiesza i jedzie z prędkością {self.predkosc}km/h")
    def hamuj(self):
        if self.predkosc >= 10:
            self.predkosc -= 10
            print(f"Samochód {self.marka} hamuje i jedzie z prędkością {self.predkosc}km/h")
        else:
            print(f"Samochód {self.marka} już stoi!")
    def klakson(self):
        print(f"Samochód {self.marka} trąbi!")

    def getter_kolor(self):
        return self._kolor
    def setter_kolor(self, nowy_kolor):
        self._kolor = nowy_kolor


bmw = Samochod("BMW")
bmw.przedstaw_sie()
bmw.przyspiesz()
bmw.przyspiesz()

mini = Samochod("MINI")
mini.przyspiesz()
bmw.przyspiesz()
mini.hamuj()
mini.hamuj()
mini.klakson()

print(mini.getter_kolor())
mini.setter_kolor("czerwony")
print(mini.getter_kolor())

print("="*30)
print(mini._kolor)
mini._kolor = "Niebieski"
print(mini._kolor)
