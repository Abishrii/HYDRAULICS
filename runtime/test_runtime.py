from pathlib import Path
import joblib

from edge_runtime import EdgeRuntime

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

runtime = EdgeRuntime()

# Load feature list
feature_columns = joblib.load(MODEL_DIR / "feature_columns.pkl")

# Read sample
import pandas as pd

sample = pd.read_csv(MODEL_DIR / "test_sample.csv")

# Keep only training features
sample = sample[feature_columns]

result = runtime.predict(sample)

print(result)