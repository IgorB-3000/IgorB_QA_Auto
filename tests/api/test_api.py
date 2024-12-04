import pytest

@pytest.mark.change
def test_remove_name(user):
    """Тест змінює поле name на пустий рядок і перевіряє зміни."""
    # Змінюємо поле name на пустий рядок
    user.name = ""
    # Перевіряємо, що поле name стало пустим рядком

@pytest.mark.check
def test_name(user):
    """Перевіряє, що поле name об'єкта user відповідає очікуваному."""
    assert user.name == "Ім'я"  # Замініть на ваше ім'я

@pytest.mark.check
def test_second_name(user):
    """Перевіряє, що поле second_name об'єкта user відповідає очікуваному."""
    assert user.second_name == "Прізвище"  # Замініть на ваше прізвище

