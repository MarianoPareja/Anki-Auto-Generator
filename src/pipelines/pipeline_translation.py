from openai import OpenAI
from dotenv import load_dotenv
import re
import pandas as pd

load_dotenv()

def get_prompt(src_lang: str, dst_lang: str, input: list):

    input_str = ',\n'.join(f"{item}" for item in input)

    print(type(input_str))
    print(input)

    prompt = """
    Using the following list of words in {src_lang}, extract the corresponding words and translate it to {dst_lang},
    returning a json file object containing the original words as key and the translation as value.

    START EXAMPLE
    Input: {{
    [Vocabulaire,
    i ampoule n.f.,
    appareil n.m.,
    aspirateur n.m.,
    baignoire n.f.,
    optimiste adj.,
    augmenter,
    ]
    }}
    Output: 
    {{
        Le Vocabulaire: El Vocabulario,
        L'ampoule: La Bombilla,
        Le aspirateur: La aspiradora,
        La baignoire: La bañera,
        optimiste: optimista,
        augmenter: aumentar,
    }}
    END EXAMPLE
    Input:
    {input_str}

    Output: 
    """

    return prompt.format(src_lang=src_lang, dst_lang=dst_lang, input_str=input_str)


def get_response(prompt: str):  
    
    client = OpenAI()

    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt, 
        max_tokens=1024,
        temperature=0
    )

    return response.choices[0].text


def output_to_csv(text: str):

    text = re.sub(r'[{},]','', text)

    output = text.split("\n")

    src = []
    dst = []

    for item in output: 
        if item.isspace() or not item:
            continue

        item = re.sub(r'\s+', ' ', item).strip()
        words = item.split(': ')

        src.append(words[0])
        dst.append(words[1])

    df = pd.DataFrame({
        'src': src,
        'dst': dst,
    })

    # Avoid the last '\n'
    return df.to_csv(index=False)


def translation_pipeline(data):
    prompt = get_prompt('french', 'spanish', data)
    response = get_response(prompt)
    csv_file = output_to_csv(response)

    return csv_file

if __name__ == "__main__":
    pass