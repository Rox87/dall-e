from model.imageGen import ImageGenerator
from pathlib import Path

# Initialize the image generator
imageGen = ImageGenerator()

# Define input and output paths
input_dir = Path("images") / "input"
output_dir = Path("images") / "output"

# Create a variation of the original image
imageGen.variant_image(str(input_dir / "original.png"))

# Download the generated variant
imageGen.download_image(names=[str(output_dir / "leao_var1")])