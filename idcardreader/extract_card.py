import pytesseract
from PIL import Image

def extract_name_address(image_path):
    """Extracts name and address from an image."""

    # Open the image
    image = Image.open(image_path)

    # Extract the text from the image
    text = pytesseract.image_to_string(image)

    # Process the text to extract name and address
    # This part is highly dependent on the image format and layout
    # You'll likely need to use regular expressions or other text processing techniques
    # to extract the relevant information

    return text

# Example usage
image_path = "lic_id.jpg"
text = extract_name_address(image_path)

print("Text:", text)
