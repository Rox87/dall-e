from model.imageGen import ImageGenerator

imageGen = ImageGenerator()

imageGen.generateImage(
    Prompt="Giant lion",
    ImageCount=2,
    ImageSize = "1024x1024"
    )
imageGen.downloadImage(names=["images/create/leao_new77","images/create/leao_new4"])
