import cv2
import pytesseract
from PIL import Image
from PyDictionary import PyDictionary
import cohere 


# Step 1: Open webcam and capture image on pressing SPACE
cam = cv2.VideoCapture(0)
print("Press SPACE to capture the word, ESC to quit...")

while True:
    ret, frame = cam.read()
    cv2.imshow("Camera - Press SPACE to capture", frame)

    key = cv2.waitKey(1)
    if key == 32:  # SPACE pressed → capture
        cv2.imwrite("captured.png", frame)
        print("Image captured!")
        break
    elif key == 27:  # ESC → quit
        cam.release()
        cv2.destroyAllWindows()
        exit()

cam.release()
cv2.destroyAllWindows()

# Step 2: OCR - extract word from captured image
image = Image.open("captured.png")
word = pytesseract.image_to_string(image, config="--psm 8").strip().lower()
print(f"Detected Word: {word}")

#step 03: get meaning using cohere api
co = cohere.Client("YOUR_COHERE_API_KEY")

prompt = f"Explain the word '{word}' in simple language with an example."

response = co.chat(
    model="command-a-03-2025",
    message=prompt
)

print(response.text)
 
