print("   $$$$$$$$$$$$$$$$$$$$$$    ")
print(" ite to banknotow i monet ")
print("policzmy ile to banknotow i monet")
print("banknoty to, banknoty")
print("$$$$$$$$$$$$$$$$$4")


banknoty = [
    500,
    200,
    100,
    50,
    20,
    10,
    5,
    2,
    1,
]

a = int(input("podaj kwote "))
waluta = a
kasa = []
i = 0

while sum(kasa) < a:
    ilosc_bankonotow = waluta // banknoty[i]
    (waluta) %= banknoty[i]
    for j in range(ilosc_bankonotow):
        kasa.append(banknoty[i])
    i += 1

print(" suma : ", sum(kasa))
print("banknoty i monety : ", kasa)
