from model.imageGen import ImageGenerator

imageGen = ImageGenerator()

#edita as imagem com base no prompt 
imageGen.editImage(
    imageName= "images\input\original",
    maskName = "images\input\mask",
    ImageCount = 1,
    ImageSize = "1024x1024",
    Prompt = "leoa filhote e leão"
)
#baixa a imagem gerada
imageGen.downloadImage(names=['images\output\leao_edit1'])