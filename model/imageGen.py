import openai
import os
import requests
from dotenv import load_dotenv
from PIL import Image
load_dotenv()
class ImageGenerator:
    def __init__(self) -> str:
        self.image_url : str
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.name = None

    def generateImage(self,Prompt,ImageCount,ImageSize):
        try:
            response = openai.Image.create(
            prompt = Prompt,
            n = ImageCount,
            size = ImageSize 
            )
            self.image_url = response['data']
            self.image_url = [image["url"] for image in self.image_url]
            print(self.image_url)
            return self.image_url
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)

    def variantImage(self,image):
        response = openai.Image.create_variation(
            image=open(image,'rb')
            )
        self.image_url = [response['data'][0]['url']]
        return self.image_url

    def downloadImage(self,names)-> None:
        try:
            self.name = names
            i = 0
            for url in self.image_url:
                image = requests.get(url)
                with open(f"{names[i]}.png","wb") as f:
                    f.write(image.content)
                i+=1
        except:
            print("An error ocured")
            return self.name

    def convertImage(self,maskname):
        image = Image.open(f"{maskname}.png")
        rgba_image = image.convert('RGBA')
        rgba_image.save(f"{maskname}.png")
        return rgba_image
    
    def editImage(self,imageName, maskName,ImageCount,ImageSize,Prompt):
        self.convertImage(maskName)
        response = openai.Image.create_edit(
            image = open(f"{imageName}.png","rb"),
            mask = open(f"{maskName}.png","rb"),
            prompt = Prompt,
            n = ImageCount,
            size = ImageSize
            )
        self.image_url = response['data']
        self.image_url = [image["url"] for image in self.image_url]

        print(self.image_url)
        return self.image_url

