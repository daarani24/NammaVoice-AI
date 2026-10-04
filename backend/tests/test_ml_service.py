from app.services import ml_service

def test_predict_returns_expected_keys():
    result = ml_service.predict("Large pothole on main road causing accidents")

    assert "predicted_category" in result
    assert "priority" in result
    assert "confidence_score" in result
    assert 0 <= result["confidence_score"] <= 1