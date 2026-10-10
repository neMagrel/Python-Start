# Урок 04. Слайды 15–16. ГОТОВЫЙ ОБРАЗЕЦ ДЛЯ РАЗБОРА.
# Внимание: во время восстановления по памяти этот файл нужно закрыть.

total = int(input("Сколько всего минут? "))

hours = total // 60
minutes = total % 60

print(f"{total} минут — это {hours} ч {minutes} мин")
print(f"В записи ответа {len(str(hours)) + len(str(minutes))} цифр")
