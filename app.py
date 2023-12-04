from src.pipelines.pipeline_preprocessing import preprocess_pipeline
from src.pipelines.pipeline_ocr import pipeline_ocr
from src.pipelines.pipeline_translation import translation_pipeline

from src.utils import load_random_image


if __name__ == '__main__':
    image = load_random_image()
    preprocess_image = preprocess_pipeline(image)
    data = pipeline_ocr(preprocess_image)
    output = translation_pipeline(data)

    print(output)
