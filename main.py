print("   $$$$$$$$$$$$$$$$$$$$$$    ")
print(" ite to banknotow i monet ")
print("policzmy ile to banknotow i monet")
print("banknoty to, banknoty")
print("podaj kwote")


banknoty = [
    500,
    200,
    100,
    50,
    20,
    10,
    5,
    2,
    500,
    200,
    100,
    50,
    20,
    10,
    5,
    2,
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
banknoty.sort()
banknoty.reverse()

a = int(input("podaj kwote "))
waluta = a
kasa = []
i = 0

while i < len(banknoty) and (waluta - sum(kasa) >= min(banknoty)):
    if (waluta - sum(kasa)) >= banknoty[i]:
        kasa.append(banknoty[i])
    i += 1

print(" suma : ", sum(kasa))
print("banknoty : ", kasa)
