import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_login_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_signup_page(client):
    response = client.get("/signup")
    assert response.status_code == 200


def test_home_requires_login(client):
    response = client.get("/home")
    assert response.status_code == 302


def test_tips_requires_login(client):
    response = client.get("/tips")
    assert response.status_code == 302


def test_contact_requires_login(client):
    response = client.get("/contact")
    assert response.status_code == 302


def test_detection_requires_login(client):
    response = client.get("/detection")
    assert response.status_code == 302


def test_signup_and_login(client):
    signup_response = client.post(
        "/signup",
        data={
            "email": "test@example.com",
            "password": "test123"
        }
    )

    assert signup_response.status_code == 302

    login_response = client.post(
        "/",
        data={
            "email": "test@example.com",
            "password": "test123"
        }
    )

    assert login_response.status_code == 302
    assert login_response.location.endswith("/home")