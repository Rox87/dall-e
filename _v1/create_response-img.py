# create.py

import json
import os
from pathlib import Path
from base64 import b64decode
import openai

'''gera um json com a resposta da api e depois grava a imagem e arquivo'''

PROMPT = "obra de Deus"
DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)

#DATA_DIR = Path.cwd() / "responses"
JSON_FILE = file_name
IMAGE_DIR = Path.cwd() / "images"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    response = json.load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)