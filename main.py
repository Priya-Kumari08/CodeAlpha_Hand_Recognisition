from predict import predict_digit

file = "digit.png"   # apni image ka naam

result = predict_digit(file)

print("Predicted Digit:", result)