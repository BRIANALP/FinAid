import cv2
import pytesseract
import re

def extract_details(ocr_result):
    # Define regular expressions for extracting name and mean grade
    name_pattern = re.compile(r'NAME:\s*([\w\s]+)\s*')
    grade_pattern = re.compile(r'MEAN GRADE\s*([\w\s\+\-]+)\s*')

    # Search for the patterns in the OCR result
    name_match = re.search(name_pattern, ocr_result)
    grade_match = re.search(grade_pattern, ocr_result)

    # Extract name and mean grade if found
    name = name_match.group(1) if name_match else "Name not found"
    mean_grade = grade_match.group(1) if grade_match else "Mean grade not found"

    return name, mean_grade

# Replace 'your_image.jpg' with the actual file path
image_path = 'data/certificate.jpg'

# Read the original image
original_image = cv2.imread(image_path)

# Check if the image was successfully loaded
if original_image is None:
    print(f"Error: Unable to load image from '{image_path}'")
    exit(1)

# Get image dimensions
height, width, _ = original_image.shape

# Split the image into upper and lower halves
upper_half = original_image[0:height//2, :, :]
lower_half = original_image[height//2:height, :, :]

# Define a function to zoom in on a given image
def zoom_image(image, factor):
    return cv2.resize(image, None, fx=factor, fy=factor)

# Zoom in on the upper and lower halves
zoomed_upper_half = zoom_image(upper_half, factor=1.5)
zoomed_lower_half = zoom_image(lower_half, factor=1.5)

# Perform OCR on the zoomed-in images
text_upper_half = pytesseract.image_to_string(zoomed_upper_half)
text_lower_half = pytesseract.image_to_string(zoomed_lower_half)

# Combine OCR results for upper and lower halves
combined_ocr_result = text_upper_half + '\n' + text_lower_half

# Extract details from the combined OCR result
name, mean_grade = extract_details(combined_ocr_result)

# Display the extracted details
print("Extracted Details:")
print(f"Name: {name}")
print(f"Mean Grade: {mean_grade}")

# Optionally, you can display the original and zoomed images
cv2.waitKey(0)
cv2.destroyAllWindows()

