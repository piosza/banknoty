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
kasa200 = []
kasa100 = []
kasa50 = []
kasa20 = []
kasa10 = []
kasa5 = []
kasa2 = []
kasa1 = []
i = 0

while sum(kasa) < a:
    ilosc_bankonotow = waluta // banknoty[i]
    (waluta) %= banknoty[i]
    for j in range(ilosc_bankonotow):
        kasa.append(banknoty[i])

    i += 1
number_of_banknoty = len(kasa)


def banknoty_500(
    kasa,
    kasa500,
):
    for banknot in kasa:
        if banknot == 500:
            kasa500.append(500)


def banknoty_200(
    kasa,
    kasa200,
):
    for banknot in kasa:
        if banknot == 200:
            kasa200.append(200)


def banknoty_100(
    kasa,
    kasa100,
):
    for banknot in kasa:
        if banknot == 100:
            kasa100.append(100)


def banknoty_50(
    kasa,
    kasa50,
):
    for banknot in kasa:
        if banknot == 50:
            kasa50.append(50)


def banknoty_20(
    kasa,
    kasa20,
):
    for banknot in kasa:
        if banknot == 20:
            kasa20.append(20)


def banknoty_10(
    kasa,
    kasa10,
):
    for banknot in kasa:
        if banknot == 10:
            kasa10.append(10)


def banknoty_5(
    kasa,
    kasa5,
):
    for banknot in kasa:
        if banknot == 5:
            kasa5.append(5)


def banknoty_2(
    kasa,
    kasa2,
):
    for banknot in kasa:
        if banknot == 2:
            kasa2.append(2)


def banknoty_1(
    kasa,
    kasa1,
):
    for banknot in kasa:
        if banknot == 1:
            kasa1.append(1)


banknoty_500(kasa, kasa500)
banknoty_200(kasa, kasa200)
banknoty_100(kasa, kasa100)
banknoty_50(kasa, kasa50)
banknoty_20(kasa, kasa20)
banknoty_10(kasa, kasa10)
banknoty_5(kasa, kasa5)
banknoty_2(kasa, kasa2)
banknoty_1(kasa, kasa1)

print(" suma : ", sum(kasa))
print("banknoty i monety : ", kasa)
print("ilosc sztuk ", number_of_banknoty)
print("banknoty 500", len(kasa500))
print("banknoty 200", len(kasa200))
print("banknoty 100", len(kasa100))
print("banknoty 50", len(kasa50))
print("banknoty 20", len(kasa20))
print("banknoty 10", len(kasa10))
print("moneta 5", len(kasa50))
print("moneta 2", len(kasa20))
print("moneta 1", len(kasa10))
