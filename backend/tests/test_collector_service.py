from unittest.mock import MagicMock
from app.services import collector_service

def test_dashboard(mocker):
    fake_db=MagicMock()
    fake_user=MagicMock(district_id=1)

    mocker.patch(
        "app.services.collector_service.complaint_repository.get_district_stats",
        return_value={"total": 5,"pending": 2,"completed": 3}
    )
    mocker.patch(
        "app.services.collector_service.complaint_repository.get_all_by_district",
        return_value=[]
    )

    result=collector_service.get_dashboard(fake_db, fake_user)
    assert result['stats']['total']==5