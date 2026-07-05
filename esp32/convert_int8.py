import numpy as np
import tensorflow as tf
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = ROOT / "models" / "autoencoder.keras"
NPY_PATH = ROOT / "models" / "X_train_scaled.npy"
OUTPUT_PATH = ROOT / "models" / "model_int8.tflite"

print("Loading model...")
model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)

print("Loading representative dataset...")
X_train = np.load(NPY_PATH).astype(np.float32)

print("Dataset Shape :", X_train.shape)

# ----------------------------------------------------
# Representative Dataset
# ----------------------------------------------------
def representative_dataset():

    sample_count = min(500, len(X_train))

    for i in range(sample_count):
        yield [X_train[i:i+1]]

# ----------------------------------------------------
# Converter
# ----------------------------------------------------
converter = tf.lite.TFLiteConverter.from_keras_model(model)

converter.optimizations = [tf.lite.Optimize.DEFAULT]

converter.representative_dataset = representative_dataset

converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS_INT8
]

converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

print("Converting...")

tflite_model = converter.convert()

OUTPUT_PATH.write_bytes(tflite_model)

print()
print("==============================")
print("Conversion Successful")
print("==============================")
print("Saved :", OUTPUT_PATH)
print("Model Size :", round(len(tflite_model)/1024,2),"KB")