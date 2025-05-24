class Samochod:
    def __init__(self, marka):
        self.marka = marka
        self.predkosc = 0
        print(f"Samochód {self.marka} wita")
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

bmw = Samochod("BMW")
bmw.przedstaw_sie()
bmw.przyspiesz()
bmw.przyspiesz()

mini = Samochod("MINI")
mini.przyspiesz()
bmw.przyspiesz()
mini.hamuj()
mini.hamuj()