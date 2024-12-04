import requests
import pytest

@pytest.mark.http
def test_first_request():
    # Відправляємо HTTP запит з методом GET
    response = requests.get("https://api.github.com/zen")
    # Виводимо текст відповіді
    print(f"Response text: {response.text}")
"""
@pytest.mark.http
def test_second_request():
    # Відправляємо HTTP запит з методом GET
    response = requests.get("https://api.github.com/users/defunkt")
    # Перевіряємо, що атрибут name відповідає 'Chris Wanstrath'
    assert response.json()['name'] == 'Chris Wanstrath'
    # Перевіряємо, що статус код відповіді 200
    assert response.status_code == 200
    # Перевіряємо, що заголовок Server відповідає 'GitHub.com'
    assert response.headers['Server'] == 'GitHub.com'
"""
@pytest.mark.http
def test_second_request():
    """Тест виконує GET-запит до https://api.github.com/users/defunkt"""
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath', f"Expected name 'Chris Wanstrath', got {body['name']}"
    assert r.status_code == 200, f"Expected status code 200, got {r.status_code}"
    assert headers['Server'].lower() == 'github.com', f"Expected Server header 'GitHub.com', got {headers['Server']}"


@pytest.mark.http
def test_status_code_request():
    # Відправляємо HTTP запит з методом GET
    response = requests.get("https://api.github.com/users/sergii_butenko")
    # Перевіряємо, що статус код відповіді 404
    assert response.status_code == 404

