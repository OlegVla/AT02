#Конечно! Вот пример функции на Python, которая считает количество гласных в строке, и
# тестов для этой функции с использованием PyTest.
### Функция для подсчета количества гласных:
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
### Тесты с использованием PyTest:

#Создайте файл, например, `test_count_vowels.py`, и добавьте туда следующие тесты:


