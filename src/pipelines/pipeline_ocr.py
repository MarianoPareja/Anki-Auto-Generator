import cv2
import numpy as np
import pytesseract


def apply_ocr(image: np.ndarray):

    words_data = pytesseract.image_to_string(image, output_type=pytesseract.Output.STRING)

    return words_data


def format_data(data: str): 

    words_list = data.strip().split("\n")
    # Remove empty lines 
    words_list = list(filter(lambda x: len(x) != 0, words_list))

    return words_list


def pipeline_ocr(image: np.ndarray):
    
    data = apply_ocr(image)
    data = format_data(data)

    return data


if __name__ == "__main__":
    None