import joblib
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "ML", "models")

category_vectorizer = joblib.load(os.path.join(MODEL_DIR, "category_vectorizer.pkl"))
category_model = joblib.load(os.path.join(MODEL_DIR, "category_model.pkl"))

priority_vectorizer = joblib.load(os.path.join(MODEL_DIR, "priority_vectorizer.pkl"))
priority_model = joblib.load(os.path.join(MODEL_DIR, "priority_model.pkl"))

def predict(text: str):
    cat_vec = category_vectorizer.transform([text])
    predicted_category = category_model.predict(cat_vec)[0]
    category_confidence = category_model.predict_proba(cat_vec).max()

    pri_vec = priority_vectorizer.transform([text])
    predicted_priority = priority_model.predict(pri_vec)[0]

    return {
        "predicted_category": predicted_category,
        "priority": predicted_priority,
        "confidence_score": round(float(category_confidence), 2),
    }