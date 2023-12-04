import numpy as np
import cv2

def preprocess_image(image: np.ndarray):
    image_gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image_gray_scale

def threshold_image(image: np.ndarray):
    _, image_threshold = cv2.threshold(src=image,
                                thresh=0,
                                maxval=255,
                                type=cv2.THRESH_BINARY + cv2.THRESH_OTSU
                                )
    
    return image_threshold

def normalize_image(image: np.ndarray):
    min_value = np.min(image)
    max_value = np.max(image)

    # Min-Max Normalization
    normalized_image = ((image - min_value) / (max_value - min_value))
    normalized_image = (normalized_image*255).astype(np.uint8)

    # Normalize image size
    normalized_image = cv2.resize(
        src=normalized_image,
        dsize=(1920,1080),
        interpolation=cv2.INTER_AREA,
    )

    return normalized_image


def preprocess_pipeline(image: np.ndarray):
    img = preprocess_image(image)
    img = threshold_image(img)
    img = normalize_image(img)
    return img


if __name__ == '__main__':
    pass