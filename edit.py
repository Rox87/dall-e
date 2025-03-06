from model.imageGen import ImageGenerator
from pathlib import Path

# Initialize the image generator
imageGen = ImageGenerator()

# Define input paths
input_dir = Path("images") / "input"
output_dir = Path("images") / "output"

# Edit the image based on the prompt
imageGen.edit_image(
    image_name=str(input_dir / "original"),
    mask_name=str(input_dir / "mask"),
    image_count=1,
    image_size="1024x1024",
    prompt="leoa filhote e leão"
)

# Download the generated image
imageGen.download_image(names=[str(output_dir / "leao_edit1")])