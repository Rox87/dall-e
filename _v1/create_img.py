import openai
import os
'''gera uma imagem baseada em prompt e depois baixa da url'''
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="obra de Deus",
  n=1,
  size="1024x1024"
)

#print(response)

import urllib.request

url = response['data'][0]['url']
with urllib.request.urlopen(url) as url:
    with open('images\example.png','wb') as f:
       f.write(url.read())