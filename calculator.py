# calculator.py
def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def sqrt(x):
    """Извлечение квадратного корня"""
    if x < 0:
        return "Ошибка: корень из отрицательного числа"
    return x ** 0.5

def main():
    print("=== Калькулятор ===")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Квадратный корень")
    
    choice = input("Выберите операцию (1-5): ")
    
    if choice == '5':
        x = float(input("Введите число: "))
        print(f"Результат: {sqrt(x)}")
    else:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        if choice == '1':
            print(f"Результат: {add(a, b)}")
        elif choice == '2':
            print(f"Результат: {subtract(a, b)}")
        elif choice == '3':
            print(f"Результат: {multiply(a, b)}")
        elif choice == '4':
            print(f"Результат: {divide(a, b)}")
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()