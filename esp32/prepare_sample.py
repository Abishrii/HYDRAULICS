from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

sample_path = ROOT / "models" / "test_sample.csv"

sample = pd.read_csv(sample_path)

print("Original Shape :", sample.shape)

sample = sample.iloc[:, :96]

print("New Shape :", sample.shape)

output_path = ROOT / "models" / "test_sample_96.csv"

sample.to_csv(output_path, index=False)

print("Saved:", output_path)