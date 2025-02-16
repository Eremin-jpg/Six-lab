a = input("Введите предложение: ")

zpt = a.find(',')

if zpt != -1:
    b = a[:zpt]
else:
    b = a

count_n = b.lower().count('н')

print("Количество букв 'н' до первой запятой:", count_n)
