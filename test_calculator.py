# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide, sqrt

def test_add():
    """Тест сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 1.5) == 4.0

def test_subtract():
    """Тест вычитания"""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0
    assert subtract(5.5, 1.5) == 4.0

def test_multiply():
    """Тест умножения"""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(2.5, 2) == 5.0

def test_divide():
    """Тест деления"""
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    assert divide(10, 3) == pytest.approx(3.333, 0.001)

def test_divide_by_zero():
    """Тест деления на ноль"""
    result = divide(10, 0)
    assert result is None  # Функция должна вернуть None при ошибке

def test_sqrt():
    """Тест квадратного корня"""
    assert sqrt(9) == 3.0
    assert sqrt(0) == 0.0
    assert sqrt(2) == pytest.approx(1.414, 0.001)

def test_sqrt_negative():
    """Тест корня из отрицательного числа"""
    result = sqrt(-4)
    assert result is None  # или проверка на возврат ошибки