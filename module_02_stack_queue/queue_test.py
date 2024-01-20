from queue import Queue

# Створюємо чергу
q = Queue(maxsize=3)

# Перевіряємо, чи черга порожня
print(q.empty())  # Output: True

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

# Перевіряємо, чи черга повна
print(q.full())  # Output: True

# Перевіряємо розмір черги
print(q.qsize())  # Output: 3

# Видаляємо елементи
print(q.get())  # Output: 'a'
print(q.get())  # Output: 'b'
