import tensorflow as tf

interpreter = tf.lite.Interpreter(
    model_path="models/model_int8.tflite"
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("\n========== INPUT ==========")
print("Shape      :", input_details[0]["shape"])
print("DType      :", input_details[0]["dtype"])
print("Scale      :", input_details[0]["quantization"][0])
print("Zero Point :", input_details[0]["quantization"][1])

print("\n========== OUTPUT ==========")
print("Shape      :", output_details[0]["shape"])
print("DType      :", output_details[0]["dtype"])
print("Scale      :", output_details[0]["quantization"][0])
print("Zero Point :", output_details[0]["quantization"][1])