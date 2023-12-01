import cv2
import pytesseract

def ocr_on_upper_half(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Get the height and width of the image
    height, width, _ = img.shape

    # Extract the upper half of the image
    upper_half = img[0:height//2, 0:width]

    # Convert the upper half to grayscale
    gray_upper_half = cv2.cvtColor(upper_half, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the upper half
    text = pytesseract.image_to_string(gray_upper_half)

    return text

# Example usage
image_path = 'data/canopy4.jpg'

# Perform OCR on the upper half of the image
extracted_text = ocr_on_upper_half(image_path)

# Specify the statement to check
statement_to_check = 'SECONDARY'

# Check if the statement is present in the extracted text
if statement_to_check in extracted_text:
    print("Statement found: Valid document.")
else:
    print("Statement not found: Invalid document or incorrect region.")
