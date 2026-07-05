import tensorflow as tf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

keras_model = BASE_DIR / "models" / "autoencoder.keras"

tflite_model = BASE_DIR / "models" / "autoencoder.tflite"

print("Loading model...")

model = tf.keras.models.load_model(
    keras_model,
    compile=False
)

print("Converting...")

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite = converter.convert()

with open(tflite_model, "wb") as f:
    f.write(tflite)

print("Saved:", tflite_model)