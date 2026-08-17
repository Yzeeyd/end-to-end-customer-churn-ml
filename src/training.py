from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import joblib
import os

# Local lib
from src.data import CleanData

from src.config import (
    FILE_PATH,
    ARTIFACT_PATH,
    THRESHOLD,
    COL_DROP,
    CATEGORICAL,
    NUMERICAL,
    TARGET
)



def Train():

    # Load and clean data
    X, y = CleanData(
        FILE_PATH,
        COL_DROP,
        NUMERICAL,
        TARGET
    )

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Data preprocessing
    Preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                StandardScaler(),
                NUMERICAL
            ),
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL
            )
        ]
    )

    # Final model
    Model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        min_samples_leaf=2,
        min_samples_split=5,
        class_weight="balanced_subsample",
        random_state=42
    )

    # Full ML pipeline
    ModelPipeline = Pipeline([
        ("Preprocessor", Preprocessor),
        ("Model", Model)
    ])

    # Train
    ModelPipeline.fit(
        X_train,
        y_train
    )

    # Predict probabilities
    y_prob = ModelPipeline.predict_proba(
        X_test
    )[:, 1]

    # Apply custom threshold
    y_pred = (
        y_prob >= THRESHOLD
    ).astype(int)

    # Evaluation
    print("Accuracy :", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall   :", recall_score(y_test, y_pred))
    print("F1       :", f1_score(y_test, y_pred))

    # Create model directory
    os.makedirs(
        os.path.dirname(ARTIFACT_PATH),
        exist_ok=True
    )

    # Package model artifact
    model_artifact = {
        "model": ModelPipeline,
        "threshold": THRESHOLD
    }

    # Save model
    joblib.dump(
        model_artifact,
        ARTIFACT_PATH
    )

    print(f"Model saved to: {ARTIFACT_PATH}")


if __name__ == "__main__":
    Train()