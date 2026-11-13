import numpy as np

# Ціни товарів
prices = np.array([120, 250, 500, 750, 1000])

# Кількість проданих товарів
quantities = np.array([5, 3, 8, 2, 4])

# Відсотки знижок
discounts = np.array([10, 15, 0, 20, 5])

print("Ціни:", prices)
print("Кількість:", quantities)
print("Знижки:", discounts)


# Завдання 2. Інформація про масиви

def show_array_info(arr):
    print("Масив:", arr)
    print("Тип масиву:", type(arr))
    print("Тип елементів:", arr.dtype)
    print("Форма масиву:", arr.shape)
    print("Кількість через len:", len(arr))
    print("Кількість через size:", arr.size)
    print("____________________")

show_array_info(prices)
show_array_info(quantities)
show_array_info(discounts)


# Завдання 3. Арифметичні операції

# 1. Вартість проданих товарів
total_prices = prices * quantities
print("Вартість проданих товарів:", total_prices)

# 2. Збільшення знижок на 3%
discounts += 3
print("Нові знижки:", discounts)

# 3. Вартість товарів після знижки
final_prices = prices * (1 - discounts / 100)
print("Ціни після знижок:", final_prices)


# Завдання 4. Оператори порівняння

# 1. Ціни більше 500 грн
print("Ціни більше 500 грн:", prices[prices > 500])

# 2. Ціни від 200 до 800 грн
print("Ціни від 200 до 800 грн:",
      prices[(prices >= 200) & (prices <= 800)])

# 3. Ціни рівно 500 грн
print("Ціни рівно 500 грн:", prices[prices == 500])


# Завдання 5. Логічні оператори

# 1. Ціна менша 300 або більша 800 грн
print("Ціна менша 300 або більша 800:",
      prices[(prices < 300) | (prices > 800)])

# 2. Ціна не перевищує 500 грн
print("Ціна не перевищує 500:",
      prices[~(prices > 500)])

# 3. Ціна більша 200 і кількість продажів більша 3
print("Ціна > 200 і кількість > 3:",
      prices[(prices > 200) & (quantities > 3)])


# Завдання 6. Розрахунок знижок

# 1. Знижка 20% для кожного товару
discount_20 = prices * 0.20
print("Знижка 20%:", discount_20)

# 2. Індивідуальна сума знижки
individual_discount = prices * discounts / 100
print("Індивідуальна знижка:", individual_discount)

# 3. Кінцева вартість товарів
final_cost = prices - individual_discount
print("Кінцева вартість:", final_cost)


# Завдання 7. Індексація та зрізи

# 1. Перша та остання ціна
print("Перша ціна:", prices[0])
print("Остання ціна:", prices[-1])

# 2. Перші три ціни
print("Перші три ціни:", prices[:3])

# 3. Змінити другу ціну на 300 грн
prices[1] = 300
print("Ціни після зміни:", prices)

# 4. Ціни у зворотному порядку
print("Зворотний порядок:", prices[::-1])


# Завдання 8. Зміна та доповнення масивів

# 1. Додаємо нову ціну 1500 грн
prices = np.append(prices, 1500)
print("Після додавання:", prices)

# 2. Вставляємо 400 грн на третю позицію
prices = np.insert(prices, 2, 400)
print("Після вставки:", prices)

# 3. Видаляємо один товар (перший)
prices = np.delete(prices, 0)
print("Після видалення:", prices)


# Завдання 9. Додаткові оператори та методи NumPy

# 1. Збільшити всі ціни на 100 грн
prices += 100
print("Ціни +100:", prices)

# 2. Збільшити кількість товарів у 2 рази
quantities *= 2
print("Кількість x2:", quantities)

# 3. Скільки повних наборів по 100 грн
print("Повні сотні:", prices // 100)

# 4. Залишок після ділення на 100
print("Залишок:", prices % 100)

# 5. Замінити ціни менші 300 на 300
prices = np.where(prices < 300, 300, prices)
print("Після np.where:", prices)

# 6. Отримати унікальні ціни
print("Унікальні ціни:", np.unique(prices))

# 7. Відсортувати ціни
print("Відсортовані ціни:", np.sort(prices))

# 8. Обмежити ціни від 200 до 800
print("Ціни від 200 до 800:", np.clip(prices, 200, 800))