import cv2
import os
import random

RAW_DATA_PATH = os.path.join(os.getcwd(), 'research/data/raw_data')

def load_random_image(): 
    images = os.listdir(RAW_DATA_PATH)
    img_index = random.randint(0, len(images))
    img = cv2.imread(os.path.join(RAW_DATA_PATH, images[img_index]))
    return img 


if __name__ == '__main__':
    pass