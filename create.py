from model.imageGen import ImageGenerator

imageGen = ImageGenerator()

#gera duas imagens
imageGen.generateImage(
    Prompt="Giant lion",
    ImageCount=2,
    ImageSize = "1024x1024"
    )
#recebe os nomes das imagens e baixa - len(names) == ImageCount
imageGen.downloadImage(names=["images\output\leao1","images\output\leao2"])
