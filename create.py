from model.imageGen import ImageGenerator
from pathlib import Path

# Initialize the image generator
imageGen = ImageGenerator()

# Generate two lion images
imageGen.generate_image(
    prompt="Giant lion",
    image_count=2,
    image_size="1024x1024"
)

# Define output paths and download the generated images
output_dir = Path("images") / "output"
output_dir.mkdir(parents=True, exist_ok=True)

imageGen.download_image(names=[
    str(output_dir / "leao1"),
    str(output_dir / "leao2")
])
