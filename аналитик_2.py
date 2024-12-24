from math import comb

# Количество всех возможных рук
total_hands = comb(36, 5)

# Роял Флеш
royal_flush = 4  # По одному для каждой масти
p_royal_flush = royal_flush / total_hands

# Стрит Флеш (кроме Роял Флеша)
straight_flush = 4 * 7  # 7 стритов на масть, 4 масти
p_straight_flush = straight_flush / total_hands

# Каре (четыре карты одного достоинства)
four_of_a_kind = 9 * 32  # 9 достоинств, 32 варианта пятой карты
p_four_of_a_kind = four_of_a_kind / total_hands

# Фулл Хаус (три карты одного достоинства и две другого)
full_house = comb(9, 2) * comb(4, 3) * comb(4, 2)  # 36 достоинств, 24 способа распределить масти
p_full_house = full_house / total_hands

# Флеш (5 одномастных карт, не стрит)
flush = 4 * (comb(9, 5) - 8)  # 4 масти, вычитаем стриты
p_flush = flush / total_hands

# Стрит (5 последовательных карт, не одной масти)
straight = 7 * (4**5 - 4)  # 7 последовательностей, исключаем одномастные
p_straight = straight / total_hands

# Сет (три карты одного достоинства и две произвольных разных)
three_of_a_kind = 9 * comb(4, 3) * comb(8, 2) * (4**2)  # 9 достоинств, 16 способов для двух других карт
p_three_of_a_kind = three_of_a_kind / total_hands

# Две пары
two_pair = comb(9, 2) * (comb(4, 2)**2) * comb(7, 1) * comb(4, 1)  # 36 достоинств, 7 вариантов для пятой карты
p_two_pair = two_pair / total_hands

# Одна пара
one_pair = 9 * comb(4, 2) * comb(8, 3) * (4**3)  # 9 достоинств, 56 способов для трех других карт
p_one_pair = one_pair / total_hands

# Старшая карта
high_card = total_hands - (royal_flush + straight_flush + four_of_a_kind +
                           full_house + flush + straight +
                           three_of_a_kind + two_pair + one_pair)
p_high_card = high_card / total_hands

# Вывод вероятностей
print(f"Роял Флеш: {p_royal_flush:.6%}")
print(f"Стрит Флеш: {p_straight_flush:.6%}")
print(f"Каре: {p_four_of_a_kind:.6%}")
print(f"Фулл Хаус: {p_full_house:.6%}")
print(f"Флеш: {p_flush:.6%}")
print(f"Стрит: {p_straight:.6%}")
print(f"Сет: {p_three_of_a_kind:.6%}")
print(f"Две пары: {p_two_pair:.6%}")
print(f"Одна пара: {p_one_pair:.6%}")
print(f"Старшая карта: {p_high_card:.6%}")
