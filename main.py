import cv2
import pygame
from sent_email import execute

# Initialize Pygame for sound playback
pygame.mixer.init()

# Load the sound file you want to play when a face is detected
sound_file = "ahh.mp3"  # Replace with the path to your sound file
pygame.mixer.music.load(sound_file)

# Open the webcam
cap = cv2.VideoCapture(0)

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img_counter = 0
while True:
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Play the sound when a face is detected
    if len(faces) > 0 and not pygame.mixer.music.get_busy():
        #Store an image after 3 detections
        if img_counter == 3:
            img_name = "opencv_frame.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("Screenshot take")
            execute()
        img_counter += 1
        pygame.mixer.music.play()

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with face detection
    cv2.imshow('Face Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
