import pandas as pd

sample = pd.read_csv("models/test_sample_96.csv")

sample = sample.iloc[0].values

with open("esp32/sample.h", "w") as f:

    f.write("#ifndef SAMPLE_H\n")
    f.write("#define SAMPLE_H\n\n")

    f.write("const float sample_input[96] = {\n")

    for i, value in enumerate(sample):

        f.write(f"    {value:.10f}f")

        if i != 95:
            f.write(",")

        if (i + 1) % 4 == 0:
            f.write("\n")
        else:
            f.write(" ")

    f.write("\n};\n\n")

    f.write("#endif")