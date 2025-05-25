import requests

url = "https://api.frankfurter.dev/v1/latest?base=PLN"

response = requests.get(url)
data = response.json()
#print(data)

# pln = float(input("Podaj kwotę w PLN: "))
# print(f"Przelicznik euro: {data['rates']['EUR']}")
# print(f"Kwota {pln}PLN to {data['rates']['EUR']*pln}EUR")

# Dodaj pętlę, która wyświetli wszystkie przyliczniki

for klucz, wartosc in data['rates'].items():
    print(f"Waluta {klucz} przelicznik {wartosc}")

# for key, value in data['rates'].items():
#     print(key, value)