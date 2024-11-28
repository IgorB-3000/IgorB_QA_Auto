import pytest

@pytest.mark.check
def test_change_name(user):
    """Перевіряє, що поле name об'єкта user відповідає очікуваному."""
    assert user.name == "Ім'я"  

@pytest.mark.check
def test_change_second_name(user):
    """Перевіряє, що поле second_name об'єкта user відповідає очікуваному."""
    assert user.second_name == "Прізвище"  
