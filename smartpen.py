import cv2
import pytesseract
from PIL import Image
from PyDictionary import PyDictionary
import requests as req

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

# Step 3: Get meaning from dictionary
url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response=req.get(url)
print(response.json())

meaning=response.json()[0]['meanings'][0]['definitions'][0]['definition']
print("\n word :", word)
print("meaning :", meaning)

if response.status_code !=200:
  print("word not found")
