event = input("Что за событие? ").strip()
place = input("Где пройдёт? ").strip()

title = event.upper()
message = f"{event} состоится в месте: {place}."

print(title)
print(message)
print(f"Длина сообщения: {len(message)} символов")
