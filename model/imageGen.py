import openai
import os
import requests
from typing import List, Optional, Union
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

class ImageGenerator:
    """A class for generating, editing, and downloading images using OpenAI's DALL-E API."""
    
    def __init__(self) -> None:
        """Initialize the ImageGenerator with OpenAI API key from environment variables."""
        self.image_urls: List[str] = []
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        openai.api_key = self.api_key
        self.names: Optional[List[str]] = None

    def generate_image(self, prompt: str, image_count: int = 1, image_size: str = "1024x1024") -> List[str]:
        """Generate images based on a text prompt.
        
        Args:
            prompt: The text description to generate images from
            image_count: Number of images to generate
            image_size: Size of the images (e.g., "1024x1024")
            
        Returns:
            List of URLs for the generated images
        """
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=image_count,
                size=image_size
            )
            self.image_urls = [image["url"] for image in response['data']]
            return self.image_urls
        except openai.error.OpenAIError as e:
            print(f"Error generating image: {e.http_status} - {e.error}")
            return []

    def variant_image(self, image_path: str) -> List[str]:
        """Create a variation of an existing image.
        
        Args:
            image_path: Path to the source image
            
        Returns:
            List containing the URL of the generated variant
        """
        try:
            image_path = Path(image_path)
            with open(image_path, 'rb') as image_file:
                response = openai.Image.create_variation(
                    image=image_file
                )
            self.image_urls = [response['data'][0]['url']]
            return self.image_urls
        except Exception as e:
            print(f"Error creating image variation: {str(e)}")
            return []

    def download_image(self, names: List[str]) -> Optional[List[str]]:
        """Download images from URLs stored in self.image_urls.
        
        Args:
            names: List of file paths (without extension) to save the images
            
        Returns:
            List of names if successful, None if an error occurred
        """
        try:
            self.names = names
            for i, url in enumerate(self.image_urls):
                if i >= len(names):
                    break
                    
                # Ensure directory exists
                output_path = Path(f"{names[i]}.png")
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Download and save image
                image_response = requests.get(url)
                image_response.raise_for_status()  # Raise exception for HTTP errors
                
                with open(output_path, "wb") as f:
                    f.write(image_response.content)
                    
            return self.names
        except Exception as e:
            print(f"Error downloading image: {str(e)}")
            return None

    def convert_image(self, mask_path: str) -> Optional[Image.Image]:
        """Convert an image to RGBA format for use as a mask.
        
        Args:
            mask_path: Path to the mask image (without extension)
            
        Returns:
            PIL Image object of the converted image
        """
        try:
            mask_file = Path(f"{mask_path}.png")
            image = Image.open(mask_file)
            rgba_image = image.convert('RGBA')
            rgba_image.save(mask_file)
            return rgba_image
        except Exception as e:
            print(f"Error converting image: {str(e)}")
            return None
    
    def edit_image(self, image_name: str, mask_name: str, image_count: int = 1, 
                  image_size: str = "1024x1024", prompt: str = "") -> List[str]:
        """Edit an image using a mask and a prompt.
        
        Args:
            image_name: Path to the source image (without extension)
            mask_name: Path to the mask image (without extension)
            image_count: Number of edited images to generate
            image_size: Size of the output images
            prompt: Text description for the edit
            
        Returns:
            List of URLs for the edited images
        """
        try:
            self.convert_image(mask_name)
            
            image_path = Path(f"{image_name}.png")
            mask_path = Path(f"{mask_name}.png")
            
            with open(image_path, "rb") as image_file, open(mask_path, "rb") as mask_file:
                response = openai.Image.create_edit(
                    image=image_file,
                    mask=mask_file,
                    prompt=prompt,
                    n=image_count,
                    size=image_size
                )
                
            self.image_urls = [image["url"] for image in response['data']]
            return self.image_urls
        except Exception as e:
            print(f"Error editing image: {str(e)}")
            return []

