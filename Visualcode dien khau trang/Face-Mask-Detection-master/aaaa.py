from tensorflow.keras.models import load_model

maskNet = load_model("mask_detector.model")

maskNet.summary()