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
kasa500 = []
i = 0

while sum(kasa) < a:
    ilosc_bankonotow = waluta // banknoty[i]
    (waluta) %= banknoty[i]
    for j in range(ilosc_bankonotow):
        kasa.append(banknoty[i])

    i += 1
number_of_banknoty = len(kasa)


def banknoty_500(kasa, kasa500):
    number_of_banknoty = len(kasa)
    for k in range(number_of_banknoty):
        banknoty500 = "500"
        kasa500.append(banknoty500)


banknoty_500(kasa, kasa500)

print(" suma : ", sum(kasa))
print("banknoty i monety : ", kasa)
print("ilosc sztuk ", number_of_banknoty)
print("banknoty 500", kasa500)
