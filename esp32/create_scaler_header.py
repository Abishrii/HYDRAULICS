import numpy as np

mean = np.loadtxt("models/scaler_mean.csv", delimiter=",")
scale = np.loadtxt("models/scaler_scale.csv", delimiter=",")

with open("esp32/scaler.h", "w") as f:

    f.write("#ifndef SCALER_H\n")
    f.write("#define SCALER_H\n\n")

    f.write("const float feature_mean[96] = {\n")

    for i, value in enumerate(mean):
        f.write(f"    {value:.10f}f")
        if i != len(mean)-1:
            f.write(",")
        if (i+1)%4==0:
            f.write("\n")
        else:
            f.write(" ")

    f.write("\n};\n\n")

    f.write("const float feature_scale[96] = {\n")

    for i, value in enumerate(scale):
        f.write(f"    {value:.10f}f")
        if i != len(scale)-1:
            f.write(",")
        if (i+1)%4==0:
            f.write("\n")
        else:
            f.write(" ")

    f.write("\n};\n\n")

    f.write("#endif\n")

print("scaler.h created successfully")