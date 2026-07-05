from pathlib import Path
import re

# ---------- Paths ----------
tflite_path = Path("models/autoencoder_int8.tflite")
model_h_path = Path("esp32/model/model.h")

# ---------- Read original model ----------
original = tflite_path.read_bytes()

# ---------- Read model.h ----------
text = model_h_path.read_text()

# Extract every hexadecimal byte (0x??)
hex_values = re.findall(r'0x([0-9a-fA-F]{2})', text)

# Convert to bytes
header_bytes = bytes(int(x, 16) for x in hex_values)

print("Original size :", len(original))
print("Header size   :", len(header_bytes))

print()

print("First 16 bytes of TFLite")
print(list(original[:16]))

print()

print("First 16 bytes of model.h")
print(list(header_bytes[:16]))

print()

if original == header_bytes:
    print("✅ SUCCESS: model.h is IDENTICAL to autoencoder_int8.tflite")
else:
    print("❌ ERROR: model.h is DIFFERENT!")

    # Find first mismatch
    for i, (a, b) in enumerate(zip(original, header_bytes)):
        if a != b:
            print(f"\nFirst difference at byte {i}")
            print("TFLite :", a)
            print("model.h:", b)
            break