import cv2
import pyttsx3
from cvzone.FaceDetectionModule import FaceDetector    # Implementation of some libraries for the project.
from cvzone.SerialModule import SerialObject


cap = cv2.VideoCapture(0)          # To start webcam and livestreaming.

detector = FaceDetector(minDetectionCon=0.8)   # If system detects %80 human face codes will start running.

arduino = SerialObject("COM6")                 # For Arduino Uno Board's connected port.
port = "COM6"

engine = pyttsx3.init()                       # For voice assistant.


while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)       # Calling some functions from libraries.
    if bboxs:                                  # If system detects a human face a data can pass to the Arduino.

        arduino.sendData([90])                 # For rotating servo motor in 90 degrees when face is detected.
        print("You can pass")
        engine.say("Welcome, door will open in few seconds")     # Comments for voice assistant.

    else:
        arduino.sendData([0])                  # For rotating servo motor in initial position and turns on the LED when face is not detected.
        print("Please show your face")
        engine.say("Door will close in few seconds please show your face to pass")       # Comments for voice assistant.

    engine.runAndWait()                       # For voice assistant It appears and wait until to concluding the program.
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):       # To stop the running program with some functions from libraries.
        break