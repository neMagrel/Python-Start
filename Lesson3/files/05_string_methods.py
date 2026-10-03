word = " Питон "

print(len(word))       # 7 — пробелы тоже символы
print(word.strip())    # "Питон"
print(len(word))       # снова 7 — исходная строка не изменилась

word = word.strip()    # теперь сохраняем новую строку без пробелов
print(len(word))       # 5
