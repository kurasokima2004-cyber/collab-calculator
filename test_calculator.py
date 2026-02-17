# test_calculator.py
from calculator import divide

def test_divide_normal():
    """Тест обычного деления"""
    result = divide(6, 2)
    print(f"Тест 6/2: {result} (ожидается 3.0)")
    assert result == 3.0

    result = divide(5, 2)
    print(f"Тест 5/2: {result} (ожидается 2.5)")
    assert result == 2.5

    print("✓ Тест обычного деления пройден")

def test_divide_by_zero():
    """Тест деления на ноль"""
    result = divide(10, 0)
    print(f"Тест 10/0: {result} (ожидается None)")
    assert result is None  # Функция должна вернуть None при ошибке
    print("✓ Тест деления на ноль пройден")

if __name__ == "__main__":
    print("Запуск тестов для функции divide...")
    test_divide_normal()
    test_divide_by_zero()
    print("Все тесты пройдены!")