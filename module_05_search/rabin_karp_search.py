def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(
        main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash -
                                  ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


main_string = "Being a developer is not easy"
substring = "developer"

position = rabin_karp_search(main_string, substring)
if position != -1:
    print(f"Substring found at index {position}")
else:
    print("Substring not found")


# У найгіршому випадку часова складність O(n*m), де n — довжина основного рядка, а m — довжина підрядка
# У середньому випадку та в найкращому випадку часова складність O(n+m)

# Алгоритм Рабіна-Карпа — це алгоритм для пошуку підрядка (або патерну) в рядку тексту за допомогою хешування. Він використовує віконний підхід, де розмір вікна відповідає розміру патерну. Алгоритм особливо ефективний для наборів даних, де є багато можливих входжень патерну.

# Алгоритм має такі кроки:

# 1. Хеш-функція: Обираємо (або визначаємо) хеш-функцію для підрахунку значення хешу для патерну та для підрядка тексту довжиною у патерн. Зазвичай використовують поліноміальне хешування.

# 2. Підрахунок хешу для патерну: Обчислюємо хеш для патерну.

# 3. Підрахунок хешу для підрядків: Починаючи від першого символу тексту, розраховуємо хеш для підрядка довжиною у патерн.

# 4. Порівняння хешу:

# Якщо хеш підрядка збігається з хешем патерну, ми виконуємо додаткове порівняння символ за символом для підтвердження, що ми дійсно знайшли входження патерну.
# Якщо підрядок не збігається з патерном, ми просто зсуваємо вікно на один символ і розраховуємо хеш для нового підрядка.
