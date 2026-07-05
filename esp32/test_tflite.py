import joblib
import numpy as np
import pandas as pd
import tensorflow as tf

# -----------------------
# Load scaler
# -----------------------

scaler = joblib.load("models/scaler.pkl")

# -----------------------
# Load raw sample
# -----------------------

sample_raw = pd.read_csv("models/test_sample_96.csv").iloc[[0]]

print("\nRAW")
print(sample_raw.values[0][:10])

# -----------------------
# Scale sample
# -----------------------

sample = scaler.transform(sample_raw).astype(np.float32)

print("\nSCALED")
print(sample[0][:10])

# -----------------------
# Load model
# -----------------------

interpreter = tf.lite.Interpreter(
    model_path="models/model_int8.tflite"
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("\nINPUT DETAILS")
print(input_details)

print("\nOUTPUT DETAILS")
print(output_details)

# -----------------------
# Quantize
# -----------------------

scale, zero = input_details[0]["quantization"]

sample_q = np.round(sample / scale + zero)

sample_q = np.clip(sample_q, -128, 127).astype(np.int8)

print("\nINT8 INPUT")
print(sample_q[0][:10])

# -----------------------
# Run
# -----------------------

interpreter.set_tensor(
    input_details[0]["index"],
    sample_q
)

interpreter.invoke()

output_q = interpreter.get_tensor(
    output_details[0]["index"]
)

print("\nINT8 OUTPUT")
print(output_q[0][:10])

# -----------------------
# Dequantize
# -----------------------

out_scale, out_zero = output_details[0]["quantization"]

output = (output_q.astype(np.float32) - out_zero) * out_scale

print("\nFLOAT OUTPUT")
print(output[0][:10])

# -----------------------
# Reconstruction Error
# -----------------------

mse = np.mean((sample[0] - output[0]) ** 2)

print("\nMSE =", mse)