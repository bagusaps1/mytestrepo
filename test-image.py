import pytesseract
from PIL import Image

# Load an image from file
image = Image.open('image/placeholder.png')

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
print("test1")
