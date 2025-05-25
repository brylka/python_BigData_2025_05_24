import requests

url = "https://api.frankfurter.dev/v1/latest?base=PLN"

response = requests.get(url)
data = response.json()
#print(data)

pln = float(input("Podaj kwotę w PLN: "))
print(f"Przelicznik euro: {data['rates']['EUR']}")
print(f"Kwota {pln}PLN to {data['rates']['EUR']*pln}EUR")