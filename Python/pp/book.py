# print("*" * 15, " Калькулятор ", "*" * 10)
# print("Для выхода введите q в качестве знака операции")
# while True:
#     sequence = input("Знак (+,-,*,/): ")
#     if sequence == 'q': break
#     if sequence in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if sequence == '+':
#             print("%.2f" % (x + y))
#         elif sequence == '-':
#             print("%.2f" % (x - y))
#         elif sequence == '*':
#             print("%.2f" % (x * y))
#         elif sequence == '/':  
#             if y != 0:
#                 print("%.2f" % (x / y))
#             else: print("Деление на ноль!")
#         else:
#             print("Неверный знак операции!")


dict = {"apple" : "яблоко",
        "bold" : "жирный",
        "bus" : "автобус",
        "cat" : "кошка",
        "саг" : "автомобиль"}

print("=" * 15, "Словарь v 0.1", "=" * 15)

#Справка. Будет выведена по команде h
helpMessage = """
search - поиск слова в словаре
add - добавить новое слово
remove - удалить слово
k - вывод всех слов
d - вывод всего словаря
h - отображение этой подсказки
quite - выход
"""

choice = ''
while choice != 'q':
    choice = input("(h - справка)>> ")
    if choice == 's':
        word = input("Введите слово: ")
        res = dict.get(word, "Нет такого слова!")
        print(res)
    elif choice == 'a':
        word = input("Введите слово: ")
        value = input("Введите новое слово: ")
        dict[word] = value
        print("Слово добавлено!")
    elif choice == 'r':
        word = input("Введите слово: ")
        del dict[word]
        print("Слово ", word , " удалено")
    elif choice == 'k':
        print(dict.keys())
    elif choice == 'd':
        for word in dict:
            print(word, ": ", dict[word])
    elif choice == 'h':
        print(helpMessage)
    elif choice == 'q':
        continue
    else:
        print("Нераспознанная команда. Введите h для справки")