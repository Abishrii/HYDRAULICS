import tensorflow as tf

interpreter = tf.lite.Interpreter(
    model_path="models/model_int8.tflite"
)

interpreter.allocate_tensors()

print(interpreter.get_input_details()[0])

print(interpreter.get_output_details()[0])