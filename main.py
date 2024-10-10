print("*********************************************")
print("*********************************************")
print("1.1 uzduotis")
print(8 * 4 + 2)
print(8 * (4 + 2))
print(48 / 4)
print(3 + 6 * 2)

a = 5
b = 6
c = a + b
print(a, b, c)

print("1.2 uzduotis")
a = 4
b = 3
c = 2

d = a + b + c
e = a - b - c
f = a * b * c
g = a / b / c
print(f"Skaičių suma: {a} + {b} + {c} = {d}")
print(f"Skaičių atimtis: {a} - {b} - {c} = {e}")
print(f"Skaičių sandauga: {a} * {b} * {c} = {f}")
print(f"Skaičių dalmuo: {a} / {b} / {c} = {g}")

a = 4
b = 2
print (a, b)
a += 5
b *= 2
print (a, b)

print("*********************************************")
print("*********************************************")
print("2.1 uzduotis")
skaicius1 = 2
skaicius2 = 3
skaicius3 = 4
if skaicius1 == skaicius2:
    print("pirmas ir antras yra lygus")
if skaicius2 == skaicius3:
    print("antras ir trecias yra lygus")
if skaicius1 > skaicius2:
    print("pirmas didesnis uz antra")
if skaicius2 > skaicius3 * 2:
    print("antras skaicius didesnis uz trecia skaiciu, padauginta is 2")
if skaicius1 % 2 == 0:
    print("pirmas skaicius lyginis")
if skaicius2 % 2 != 0:
    print("antras skaicius nelyginis")
if skaicius3 > 0:
    print("trecias skaicius teigiamas")
if skaicius1 < 0:
    print("pirmas skaicius neigiamas")
if skaicius2 % 4 == 0:
    print("antras skaicius dalinasi is 4")
if skaicius3 % 8 == 0:
    print("trecias skaicius dalinasi is 8")

print("2.2 uzduotis")
amzius = 17
if amzius == 18:
    print("Jus galite balsuoti")

paz1 = 5
paz2 = 7
paz3 = 8
if (paz1 + paz2 + paz3) / 3 >= 5:
    print("Vidurkis teigiamas")

print("2.3 uzduotis")
skaicius = 10
if skaicius % 5 == 0:
    print(f"skaicius x 1 = {skaicius * 1}")
if skaicius % 2 == 0:
    print(f"skaicius = {skaicius}, sk. kvadratas = {skaicius ** 2}, sk./2 = {skaicius/2}")
if skaicius % 7 != 0:
    skaicius2 = 8
    print({skaicius + skaicius2}, {skaicius - skaicius2}, {skaicius * skaicius2}, {skaicius / skaicius2})

print("*********************************************")
print("*********************************************")
print("3.1 uzduotis")
a = 1
b = 2
c = 3
if a > b:
    print("pirmas didesnis uz antra")
elif b > c:
    print("antras didesnis uz trecia")
elif c > a:
    print("trecias didesnis uz pirma")

print("3.2 uzduotis")
a = 1
b = 2
c = 3
if a == b:
    print("pirmi du skaiciai yra lygus nuliui")
elif b == c:
    print("paskutiniai du skaiciai yra lygus nuliui")
elif a == 0:
    print("pirmas skaicius yra lygus nuliui")
elif a < 0:
    print("pirmas skaicius yra neigiamas")
elif c > 0:
    print("trecias skaicius yra teigiamas")

print("3.3 uzduotis")
pazymys = 2
if pazymys == 10:
    print("puiku")
elif pazymys >= 9:
    print("labai gerai")
elif pazymys >= 7:
    print("gerai")
elif pazymys >= 5:
    print("patenkinamai")
elif pazymys < 5:
    print("egzaminas neislaikytas")


print("*********************************************")
print("*********************************************")
print("4.1 uzduotis")

skaicius = 10
if skaicius % 2 == 0:
    print("skaicius lyginis")
else:
    print("nelyginis")

skaicius = 14
if skaicius % 7 == 0:
    print("skaicius dalinas is 7")
else:
    print("nesidalina is 7")

kelias = "\path\hey.txt"
if kelias.endswith("py"):
    print("Python failas")
else:
    print("Kitas failas")

print("*********************************************")
print("*********************************************")
print("5.1 uzduotis")
skaicius = 8
if skaicius % 2 == 0:
    print("skaicius lyginis")
elif skaicius % 5 == 0:
    print("skaicius dalinasi is 5")
elif skaicius == 3:
    print("skaicius lygus 3")
else:
    print("Klaida!")


sk1 = 1
sk2 = 2
sk3 = 3

print("5.2 uzduotis")
if sk1 == sk2:
    print("Pirmi du skaičiai lygūs")
elif sk1 == sk3:
    print("Pirmas ir trečias skaičiai lygūs")
elif sk3 > sk1:
    print("Trečias skaičius didesnis už pirmą")
elif sk2 == (sk3 * 2):
    print("Trečias skaičius didesnis už pirmą")
elif sk1 % 3 == 0:
    print("Pirmas skaičius dalinasi iš 3")
else:
    print("Klaida!")


print("*********************************************")
print("*********************************************")
print("6.1 uzduotis")

sk1 = 1
sk2 = 2
sk3 = 3

if sk1 > sk2 and sk1 > sk3:
    print(f"Didziausias pirmas skaicius")
elif sk2 > sk1 and sk2 > sk3:
    print(f"Didziausias antras skaicius")
elif sk3 > sk1 and sk3 > sk2:
    print(f"Didziausias trecias skaicius")

if sk1 < sk2 and sk1 < sk3:
    print(f"Maziausias pirmas skaicius")
elif sk2 < sk1 and sk2 < sk3:
    print(f"Maziausias antras skaicius")
elif sk3 < sk1 and sk3 < sk2:
    print(f"Maziausias trecias skaicius")

sk1 = 1
sk2 = 2
sk3 = 3
vidurkis = (sk1 + sk2 + sk3) / 3;

if vidurkis <= 10 and vidurkis >= 8:
    print("Gautas vidurkis yra [8-10]")
elif vidurkis <= 8 and vidurkis >= 5:
    print("Gautas vidurkis yra [5-8]")
elif vidurkis < 5:
    print("Gautas vidurkis < 5")

sk1 = 2
sk2 = 5
if sk1 > sk2 or sk1 == 0:
    print()
if sk2 > sk1 or sk2 == 5:
    print()
if sk1 > sk2 and sk1 == 20:
    print()
if sk2 > sk1 and sk2 < 100:
    print()

print("*********************************************")
print("*********************************************")
print("ĮVESTIS")
print("1 uzduotis")
vardas = input('Iveskite varda: ')
amzius = input('Iveskite amziu: ')
priezastis = input('Kodel pasirinkai programavima: ')
print(f"Mano vardas yra {vardas}, man yra {amzius} metu. Programuoti pasirinkau, nes {priezastis}")

skaicius = input("Ivesk skaiciu: ")
print(f"Skaiciaus kvadratas yra {int(skaicius) ** 2}")

simbolis = input("Ivesk simboli: ")
print(simbolis)
print(f"{simbolis} {simbolis}")
print(f"{simbolis} {simbolis} {simbolis}")


print("2 uzduotis")
vardas = str(input('Iveskite varda: '))
amzius = int(input('Iveskite amziu: '))
ugis = float(input('Iveskite ugi: '))
print(f"Vardas: {vardas}, amzius: {amzius}, ugis: {ugis}")
print(f"Tipai: {type(vardas)}, {type(amzius)}, {type(ugis)}")

sk1 = int(input('Iveskite 1-a skaiciu: '))
sk2 = int(input('Iveskite 2-a skaiciu: '))
sk3 = int(input('Iveskite 3-a skaiciu: '))
sk4 = int(input('Iveskite 4-a skaiciu: '))
sk5 = int(input('Iveskite 5-a skaiciu: '))
print(f"Vidurkis = {(sk1 + sk2 + sk3 + sk4 + sk5) / 5}")

atstumas = int(input('Iveskite metrus: '))
print(f"Atstumas centimetrais: {atstumas * 100}, atstumas milimetraus: {atstumas * 1000}, atstumas kilometrais: {atstumas / 1000}" )
sk1 = int(input('Iveskite 1-a skaiciu: '))
sk2 = int(input('Iveskite 2-a skaiciu: '))
print(f"Suma: {sk1 + sk2}, skirtumas: {sk1 - sk2}, sandauga: {sk1 * sk2}, dalmuo: {sk1 / sk2}")

print("3 uzduotis")
sk1 = int(input('Iveskite 1-a skaiciu: '))
sk2 = int(input('Iveskite 2-a skaiciu: '))

print(f"Liekana: {sk1 % sk2}")

sk1 = int(input('Iveskite 1-a skaiciu: '))
sk2 = int(input('Iveskite 2-a skaiciu: '))

print(f"Pakelus laipsniu: {sk1 ** sk2}")
print()
# git config --global user.email "rasaliukste@yahoo.com"
# git config --global user.name "rasa84"


print("hi2")
