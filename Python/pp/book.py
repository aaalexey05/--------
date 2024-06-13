print("*" * 15, " Калькулятор ", + "*" * 10)
print("Для выхода введите q в качестве знака операции")
while True:
    s = input("Знак (+.-,*,/): ")
    if s == "q": break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+': print(x + y)
        elif s == '-': print(x - y)
        elif s == '*': print(x * y)
        elif s == '/':  
            if y != 0: print(x / y)
            else: print("Деление на ноль!")
        else:
            print("Неверный знак операции!")
            