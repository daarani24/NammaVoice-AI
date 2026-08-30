from unittest.mock import MagicMock
from fastapi import HTTPException
import pytest
from app.services import auth_service

def test_register(mocker):
    fake_db=MagicMock()
    mocker.patch(
        "app.services.auth_service.user_repository.get_user_by_email",
        return_value=MagicMock() 
    )
    fake_data=MagicMock(email="test@test.com")

    with pytest.raises(HTTPException) as exc:
        auth_service.register_user(fake_db, fake_data)

    assert exc.value.status_code==409

def test_login(mocker):
    fake_db=MagicMock()
    fake_user=MagicMock(id=1, role="citizen", password_hash="hashed")
    mocker.patch(
        "app.services.auth_service.user_repository.get_user_by_email",
        return_value=fake_user
    )
    mocker.patch(
        "app.services.auth_service.verify_password",
        return_value=True
    )
    fake_data=MagicMock(email="a@a.com", password="pass123")
    result=auth_service.login_user(fake_db, fake_data)

    assert "access_token" in result

def test_login_wrong_password(mocker):
    fake_db=MagicMock()
    fake_user=MagicMock(password_hash="hashed")

    mocker.patch(
        "app.services.auth_service.user_repository.get_user_by_email",
        return_value=fake_user
    )
    mocker.patch(
        "app.services.auth_service.verify_password",
        return_value=False
    )
    fake_data=MagicMock(email="a@a.com", password="wrong")

    with pytest.raises(HTTPException) as exc:
        auth_service.login_user(fake_db, fake_data)

    assert exc.value.status_code==401