import pytest

class User:
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        """Метод для створення користувача з іменем та прізвищем."""
        self.name = "Ім'я"  
        self.second_name = "Прізвище"  

    def remove(self):
        """Метод для видалення користувача."""
        self.name = ""
        self.second_name = ""

@pytest.fixture
def user():
    """Фікстура для створення та видалення об'єкта User."""
    user = User()
    user.create()
    yield user  # Повертаємо об'єкт у тест
    user.remove()  # Викликаємо метод remove після завершення тесту


