import pytest
from mainht import count_vowels  # Импортируйте функцию из вашего модуля

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_count_vowels_only_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_count_vowels_mixed_case():
    assert count_vowels("Hello World") == 3

def test_count_vowels_with_numbers_and_punctuation():
    assert count_vowels("This 1s @ t3st.") == 1

def test_count_vowels_mixed_vowels_and_consonants():
    assert count_vowels("The quick brown fox jumps over the lazy dog") == 11

if __name__ == "__main__":
    pytest.main()

### Как запустить тесты:

# 1. Убедитесь, что у вас установлен PyTest. Если нет, установите его с помощью команды:


# 2. Сохраните вашу функцию в модуле (например, `your_module.py`), а тесты в файле `test_count_vowels.py`.

# 3. Запустите testht, выполнив команду:

# Ptestht  автоматически обнаружит ваши тесты и выполнит их, предоставив отчет о результатах.