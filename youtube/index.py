import cv2
import pytesseract

# Set the path to the Tesseract executable (change the path accordingly)
# Download Tesseract: https://github.com/tesseract-ocr/tesseract
# Make sure to add the Tesseract installation path to your system's PATH variable
# For example, pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to convert image to table
def image_to_table(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(gray)

    # Split the text into lines
    lines = text.split('\n')

    # Create a list to store rows of the table


    return lines

# Example usage
image_path = 'test2.png'
result_table = image_to_table(image_path)

# Print the resulting table
for row in result_table:
    print(row)
