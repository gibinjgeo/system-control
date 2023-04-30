import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector
from keras.models import load_model  # TensorFlow is required for Keras to work
import numpy as np
import math
import time
import sys

cap = cv2.VideoCapture(0)

detector = HandDetector(maxHands=1)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()


def again():
    offset = 20
    imgSize = 224
    # Set the minimum time (in seconds) to wait before recognizing another hand gesture
    gesture_delay = 1
    last_gesture_time = time.time() - gesture_delay
    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            # cv2.imshow("ImageCrop", imgCrop)
            cv2.imshow("ImageWhite", imgWhite)

            # Make the image a numpy array and reshape it to the models input shape.
            image = np.asarray(imgWhite, dtype=np.float32).reshape(1, 224, 224, 3)

            # Normalize the image array
            image = (image / 127.5) - 1

            # Predicts the model
            prediction = model.predict(image)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
            conf = round(confidence_score, 2) * 100
            newio = int(class_name[0:2])
            print(newio, conf)
            current_time = time.time()
            if current_time - last_gesture_time > gesture_delay:
                # Recognize the hand gesture
                if conf > 95:
                    if newio == 0:
                        pyautogui.press('a')
                    if newio == 1:
                        pyautogui.press('b')
                    if newio == 2:
                        pyautogui.press('c')
                    if newio == 3:
                        pyautogui.press('d')
                    if newio == 4:
                        pyautogui.press('e')
                    if newio == 5:
                        pyautogui.press('f')
                    if newio == 6:
                        pyautogui.press('g')
                    if newio == 7:
                        pyautogui.press('h')
                    if newio == 8:
                        pyautogui.press('i')
                    if newio == 9:
                        pyautogui.press('j')
                    if newio == 10:
                        pyautogui.press('k')
                    if newio == 11:
                        pyautogui.press('l')
                    if newio == 12:
                        pyautogui.press('m')
                    if newio == 13:
                        pyautogui.press('n')
                    if newio == 14:
                        pyautogui.press('o')
                    if newio == 15:
                        pyautogui.press('p')
                    if newio == 16:
                        pyautogui.press('q')
                    if newio == 17:
                        pyautogui.press('r')
                    if newio == 18:
                        pyautogui.press('s')
                    if newio == 19:
                        pyautogui.press('t')
                    if newio == 20:
                        pyautogui.press('u')
                    if newio == 21:
                        pyautogui.press('v')
                    if newio == 22:
                        pyautogui.press('w')
                    if newio == 23:
                        pyautogui.press('x')
                    if newio == 24:
                        pyautogui.press('y')
                    if newio == 25:
                        pyautogui.press('z')
                    if newio == 26:
                        pyautogui.press('backspace')
                    if newio == 26:
                        pyautogui.press('backspace')
                    if newio == 27:
                        pyautogui.press('capslock')
                    if newio == 28:
                        print("closing entire program")
                        sys.exit()
                    if newio == 29:
                        cv2.destroyAllWindows()
                        return "shift"
                    if newio == 30:
                        pyautogui.press('space')
                    if newio == 31:
                        print("fe1")
                    if newio == 32:
                        print("fe2")
                    last_gesture_time = current_time

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord("x"):
            # cap.release()
            cv2.destroyAllWindows()


def new():
    try:
        sh = again()
        if sh == "shift":
            return "mouse"
    except:
        print("hand went out of camera")
        print("you   seriously have to stop doing that :):):)")
        # time.sleep(0.30)
        new()


new()
