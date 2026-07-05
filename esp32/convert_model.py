from pathlib import Path

model_path = Path("models/model_int8.tflite")
data = model_path.read_bytes()

with open("esp32/model.h", "w") as f:

    f.write("#ifndef MODEL_H\n")
    f.write("#define MODEL_H\n\n")

    f.write("const unsigned char model[] = {\n")

    for i, b in enumerate(data):
        f.write(f"0x{b:02x},")

        if i % 12 == 11:
            f.write("\n")

    f.write("\n};\n\n")
    f.write(f"const unsigned int model_len = {len(data)};\n\n")
    f.write("#endif\n")

print("model.h created successfully")
print("Size:", len(data), "bytes")