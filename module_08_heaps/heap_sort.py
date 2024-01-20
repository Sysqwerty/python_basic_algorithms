import heapq


def heap_sort(iterable, descending=False):
    # Визначаємо, який знак використовувати залежно від порядку сортування
    sign = -1 if descending else 1

    # Створюємо купу, використовуючи заданий порядок сортування
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    # Витягуємо елементи, відновлюємо їхні оригінальні значення (якщо потрібно) і формуємо відсортований масив
    return [sign * heapq.heappop(h) for _ in range(len(h))]


# Приклади використання функції
arr = [12, 11, 13, 5, 6, 7]
# Сортування за зростанням (за замовчуванням)
sorted_arr_asc = heap_sort(arr)
print("Відсортований масив (за зростанням):", sorted_arr_asc)
# Сортування за спаданням
sorted_arr_desc = heap_sort(arr, descending=True)
print("Відсортований масив (за спаданням):", sorted_arr_desc)

# Часова складність пірамідального сортування (heap sort) складається з двох основних етапів — це побудова купи і сам
# процес сортування. Часова складність побудови купи становить O(n), де n — кількість елементів. Після того як купа
# побудована, найбільший або найменший елемент знаходиться на вершині. Цей елемент міняється місцем з останнім
# елементом масиву і вилучається з купи. Як ми вже знаємо, часова складність вилучення одного елемента — O(logn).
# Оскільки цей процес виконується n разів для всіх елементів, загальна часова складність сортування становить
# O(n⋅logn).
#
# Обидва етапи разом дають часову складність для алгоритму пірамідального сортування O(n+nlogn),
# що спрощується до O(nlogn), оскільки O(nlogn) домінує над O(n).
#
# Таким чином, загальна часова складність пірамідального сортування становить O(n⋅logn) в найгіршому, середньому та
# найкращому випадках, що робить його дуже ефективним для сортування великих наборів даних.

[1, 3, 5, 6, 8, 9, 11, 14]
13