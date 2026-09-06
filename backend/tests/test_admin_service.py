from unittest.mock import MagicMock
from app.services import admin_service

def test_list_users(mocker):
    fake_db=MagicMock()

    mocker.patch(
        "app.services.admin_service.user_repository.get_all_users",
        return_value=[MagicMock(), MagicMock()]
    )

    result=admin_service.list_all_users(fake_db)
    assert len(result)==2