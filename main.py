import unittest

# Пример функции, которую мы хотим протестировать
def multiply(a, b):
    return a * b

# Создаем класс для тестирования
class TestMultiply(unittest.TestCase):

    # Методы тестирования должны начинаться с префикса "test_"
    def test_multiply_positive_numbers(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)  # Проверяем, что результат равен ожидаемому значению

    def test_multiply_negative_numbers(self):
        result = multiply(-2, -3)
        self.assertEqual(result, 6)  # Проверяем, что результат равен ожидаемому значению

    def test_multiply_zero(self):
        result = multiply(2, 0)
        self.assertEqual(result, 0)  # Проверяем, что результат равен ожидаемому значению

# Запускаем тесты
if __name__ == '__main__':
    unittest.main()

