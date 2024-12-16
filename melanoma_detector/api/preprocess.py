import cv2

def preprocess_image(image):
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("La imagen no puede ser procesada, por favor ingresa una imagen correcta")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0

    return image
