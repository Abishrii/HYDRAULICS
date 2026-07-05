from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Models folder
MODEL_PATH = BASE_DIR / "models" / "autoencoder_int8.tflite"

# Output header
HEADER_PATH = BASE_DIR / "esp32" / "model" / "model.h"

# Create folder if it doesn't exist
HEADER_PATH.parent.mkdir(parents=True, exist_ok=True)

print("Reading:", MODEL_PATH)
print("Writing:", HEADER_PATH)

data = MODEL_PATH.read_bytes()

with open(HEADER_PATH, "w") as f:
    f.write("#ifndef MODEL_H\n")
    f.write("#define MODEL_H\n\n")

    f.write("const unsigned char model[] = {\n")

    for i, byte in enumerate(data):
        if i % 12 == 0:
            f.write("    ")
        f.write(f"0x{byte:02x}, ")

        if i % 12 == 11:
            f.write("\n")

    f.write("\n};\n\n")
    f.write(f"const unsigned int model_len = {len(data)};\n\n")
    f.write("#endif\n")

print("✅ model.h created successfully!")
print("Model Size:", len(data), "bytes")