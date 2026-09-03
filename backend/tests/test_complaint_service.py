from unittest.mock import MagicMock
from app.services import complaint_service
from fastapi import HTTPException
import pytest

def test_submit(mocker):
    fake_db=MagicMock()
    fake_user=MagicMock(id=1)
    fake_data=MagicMock()
    mocker.patch(
        "app.services.complaint_service.complaint_repository.create_complaint",
        return_value=MagicMock(id=10)
    )
    result=complaint_service.submit_complaint(fake_db, fake_user, fake_data)
    assert result.id==10

def test_accept(mocker):
    fake_db=MagicMock()
    fake_officer=MagicMock(id=5)
    fake_complaint=MagicMock(id=1, officer_id=None)
    mocker.patch(
        "app.services.complaint_service.complaint_repository.get_by_id",
        return_value=fake_complaint
    )
    mocker.patch(
        "app.services.complaint_service.complaint_repository.assign_officer",
        return_value=fake_complaint
    )
    mocker.patch(
        "app.services.complaint_service.status_history_repository.add_status_entry"
    )
    result=complaint_service.accept_complaint(fake_db, fake_officer, 1)
    assert result.id==1

def test_accept_already_taken(mocker):
    fake_db=MagicMock()
    fake_officer=MagicMock(id=5)
    fake_complaint=MagicMock(officer_id=99)
    mocker.patch(
        "app.services.complaint_service.complaint_repository.get_by_id",
        return_value=fake_complaint
    )
    with pytest.raises(HTTPException) as exc:
        complaint_service.accept_complaint(fake_db, fake_officer, 1)
    assert exc.value.status_code==409

def test_status_wrong_officer(mocker):
    fake_db=MagicMock()
    fake_officer=MagicMock(id=5)
    fake_complaint=MagicMock(officer_id=1)
    mocker.patch(
        "app.services.complaint_service.complaint_repository.get_by_id",
        return_value=fake_complaint
    )
    with pytest.raises(HTTPException) as exc:
        complaint_service.change_status(fake_db, fake_officer, 1, "completed")
    assert exc.value.status_code==403