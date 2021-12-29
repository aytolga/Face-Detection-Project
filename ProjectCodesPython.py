import cv2
from cvzone.FaceDetectionModule import FaceDetector    # Implementation of some libraries for the project.
from cvzone.SerialModule import SerialObject


cap = cv2.VideoCapture(0)          # To start webcam and livestreaming.

detector = FaceDetector(minDetectionCon=0.8)   # If system detects %80 human face codes will start running.

arduino = SerialObject("COM6")                 # For Arduino Uno Board's connected port.
port = "COM6"



while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)       # Calling some functions from libraries.
    if bboxs:                                  # If system detects a human face a data can pass to the Arduino.

        arduino.sendData([90])                 # For rotating servo motor in 90 degrees when face is detected.

        print("You have passed")


    else:
        arduino.sendData([0])                  # For rotating servo motor in initial position and turns off the LED when face is not detected.

        print("Please show your face")



    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):       # To stop the running program with some functions from libraries.
        break