import json
from pyexpat import features
import joblib
import numpy as np
from pathlib import Path

from tensorflow.keras.models import load_model


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


class EdgeRuntime:

    def __init__(self):

        print("Loading HydroSense Runtime...")

        # Load Models
        self.autoencoder = load_model(MODEL_DIR / "autoencoder.keras",compile=False)
        self.scaler = joblib.load(MODEL_DIR / "scaler.pkl")

        self.feature_columns = joblib.load(
            MODEL_DIR / "feature_columns.pkl"
        )

        self.label_maps = joblib.load(
            MODEL_DIR / "label_maps.pkl"
        )

        with open(MODEL_DIR / "model_metadata.json", "r") as file:
            self.metadata = json.load(file)

        self.rf_models = {

            "Pump":
            joblib.load(MODEL_DIR / "rf_pump.pkl"),

            "Valve":
            joblib.load(MODEL_DIR / "rf_valve.pkl"),

            "Cooler":
            joblib.load(MODEL_DIR / "rf_cooler.pkl"),

            "Accumulator":
            joblib.load(MODEL_DIR / "rf_accumulator.pkl")
        }

        print("✅ Runtime Loaded Successfully")


    def preprocess(self, features):

        return self.scaler.transform(features)


    def anomaly_detection(self, scaled_features):

        reconstructed = self.autoencoder.predict(
            scaled_features,
            verbose=0
        )

        reconstruction_error = np.mean(
            np.square(
                scaled_features - reconstructed
            ),
            axis=1
        )[0]

        threshold = self.metadata["autoencoder_threshold"]

        health_score = max(
            0,
            100 * (1 - reconstruction_error / threshold)
        )

        return health_score, reconstruction_error


    def diagnose_fault(
    self,
    features,
    health_score,
    reconstruction_error
    ):

     rf_input = features.copy()

     # Remove old generated columns if present
     rf_input = rf_input.drop(
        columns=["Health_Score", "Reconstruction_Error"],
        errors="ignore"
     )

    # Add the runtime-generated values
     rf_input["Health_Score"] = health_score
     rf_input["Reconstruction_Error"] = reconstruction_error

     predictions = {}
     confidence = {}

     for target, model in self.rf_models.items():

        pred = model.predict(rf_input)[0]

        prob = np.max(
            model.predict_proba(rf_input)
        )

        predictions[target] = self.label_maps[target][pred]
        confidence[target] = round(prob * 100, 2)

     return predictions, confidence


    def predict(self, features):

        scaled = self.preprocess(features)

        health_score, reconstruction_error = self.anomaly_detection(
            scaled
        )

        # Edge AI Optimization
        if health_score > 95:

            return {

                "status": "Healthy",

                "health_score": round(
                    health_score,
                    2
                ),

                "reconstruction_error":
                round(reconstruction_error,6),

                "faults": None,

                "confidence": None
            }

        predictions, confidence = self.diagnose_fault(
    features,
    health_score,
    reconstruction_error
)

        return {

            "status": "Attention Required",

            "health_score":
            round(health_score,2),

            "reconstruction_error":
            round(reconstruction_error,6),

            "faults":
            predictions,

            "confidence":
            confidence
        }


if __name__ == "__main__":

    print("HydroSense Edge Runtime Ready")

    runtime = EdgeRuntime()