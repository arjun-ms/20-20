import gradio as gr
import numpy as np
import cv2
import keras

# Load model
model = keras.models.load_model('Server/3-class-improved.h5')

def predict_actor(image):
    """Predict which actor is in the image"""
    # Preprocess image
    img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, (224, 224))
    img = np.array(img) / 255.0
    img = img.reshape(-1, 224, 224, 1)

    # Get prediction
    result = model.predict(img)

    # Interpret results
    if result[0][0] > result[0][1] and result[0][0] > result[0][2]:
        prediction = 'Mammootty'
        confidence = result[0][0]
    elif result[0][1] > result[0][0] and result[0][1] > result[0][2]:
        prediction = 'Mohanlal'
        confidence = result[0][1]
    else:
        prediction = 'Unknown person'
        confidence = result[0][2]

    return f"{prediction} (Confidence: {confidence:.2%})"

# Create Gradio interface
demo = gr.Interface(
    fn=predict_actor,
    inputs=gr.Image(),
    outputs=gr.Text(label="Prediction"),
    title="Mammootty vs Mohanlal Classifier",
    description="Upload an image to classify whether it's Mammootty or Mohanlal",
    examples=[
        # You can add example image paths here if you want
    ]
)

if __name__ == "__main__":
    demo.launch()
