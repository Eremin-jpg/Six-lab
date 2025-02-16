a= input("Введите слово: ")

pvt = ""
for i in a:
    if i not in pvt:
        pvt += i

print("Слово без повторяющихся букв:", pvt)
