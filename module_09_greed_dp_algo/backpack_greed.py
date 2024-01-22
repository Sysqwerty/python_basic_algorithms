# Жадібний алгоритм. Треба сортувати предмети за їхнім співвідношенням вартість/вага та обирати найкращі предмети,
# поки не заповниться рюкзак. Непоганий метод, але може не завжди знаходити оптимальне рішення.

# У жадібному підході до задачі про рюкзак вибір предметів відбувається на основі певного критерію. Найпоширенішим
# критерієм є відношення вартість/вага (value-to-weight ratio) кожного предмета. Предмети з вищим відношенням
# вартість/вага вибираються першими, поки в рюкзаку залишається достатньо місця.

# Часова кількість обчислень: O(nlogn)

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapSack(items: list[Item], capacity: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
    return total_value


if __name__ == '__main__':
    # Дані предметів
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    # Місткість рюкзака
    capacity = 50
    # Виклик функції
    print(knapSack(items, capacity))  # 160
