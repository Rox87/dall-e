import openai
import os
'''cria'''
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create_variation(image=open('images\praia.png','rb'))
#print(response)

import urllib.request

url = response['data'][0]['url']
with urllib.request.urlopen(url) as url:
    with open('images\example2.png','wb') as f:
       f.write(url.read())