import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from preprocessing import preprocess_data   # our preprocessor
from utils import save_model
from evaluate import evaluate_model
from xgboost import XGBClassifier


DATA_PATH = "../data/processed/processed_heart.csv"
MODEL_PATH = "../models/heart_disease_model.pkl"


def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

def build_pipeline():
    preprocessor = preprocess_data()
    model = XGBClassifier( eval_metric='logloss',random_state=42)
    pipeline = Pipeline([('preprocessor', preprocessor),
                               ('classifier', model)])
    return pipeline

def main():
    df = load_data()
    X = df.drop('HeartDisease', axis=1)
    y = df['HeartDisease']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]

    metrics = evaluate_model(y_test, y_pred, y_prob)
    for metric_name, metric_value in metrics.items():
        print(f"{metric_name}: {metric_value:.4f}")

    save_model(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()