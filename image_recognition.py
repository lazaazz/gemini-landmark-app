import torch
from torchvision import transforms
from PIL import Image
import os

# List of supported monuments
MONUMENTS = ["taj_mahal", "eiffel_tower", "statue_of_liberty"]

def identify_monument(image_file):
    """Identify the monument in the uploaded image."""
    image = Image.open(image_file).convert("RGB")

    # Preprocess image
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image = transform(image).unsqueeze(0)

    # Placeholder: Assign a random monument (Replace this with a trained AI model)
    return MONUMENTS[0]  # Default to Taj Mahal for now
