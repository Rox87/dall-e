from imageGen import ImageGenerator

imageGen = ImageGenerator()

imageGen.editImage(
    imageName= "images\input\original",
    maskName = "images\input\mask",
    ImageCount = 1,
    ImageSize = "1024x1024",
    Prompt = "leoa filhote e leão"
)

imageGen.downloadImage(names=['images\edit\leao_gen5'])