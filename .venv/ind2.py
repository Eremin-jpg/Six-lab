a = input("Введите предложение: ")

zpt = a.find(',')
b = a[:zpt]
count_n = b.lower().count('н')

print("Количество букв 'н' до первой запятой:", count_n)
