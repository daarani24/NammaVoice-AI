import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

df = pd.read_csv("ML/data/complaints_dataset.csv")

os.makedirs("ML/models", exist_ok=True)

def train_and_save(label_column, output_prefix):
    X = df["text"]
    y = df[label_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    predictions = model.predict(X_test_vec)
    print(f"\n--- {output_prefix} ---")
    print(classification_report(y_test, predictions))

    joblib.dump(vectorizer, f"ML/models/{output_prefix}_vectorizer.pkl")
    joblib.dump(model, f"ML/models/{output_prefix}_model.pkl")

train_and_save("category", "category")
train_and_save("priority", "priority")