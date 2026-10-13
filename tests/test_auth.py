from src.auth.auth_service import AuthService

def test_register():
    auth = AuthService()
    assert auth.register("ivan", "12345") is True
    assert auth.register("ivan", "12345") is False

def test_login():
    auth = AuthService()
    auth.register("ivan", "12345")
    assert auth.login("ivan", "12345") is True
    assert auth.login("ivan", "wrong") is False