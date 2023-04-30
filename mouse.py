import mediapipe as mp
import cv2
import pyautogui
import time
import sys

def mouse_control():
    def count_fingers(lst):
        c = 0
        if lst.landmark[6].y > lst.landmark[8].y:
            image_width, image_height = pyautogui.size()
            image_height = image_height + 250
            image_width = image_width + 250
            relative_x, relative_y = lst.landmark[8].x, lst.landmark[8].y
            # Multiply by the image dimensions to obtain the denormalized coordinates
            x = int(relative_x * image_width)
            y = int(relative_y * image_height)
            print(x, y)
            pyautogui.moveTo(x, y)
        if lst.landmark[8].x > lst.landmark[4].x and lst.landmark[18].y > lst.landmark[20].y:
            c = 2
        if lst.landmark[8].x > lst.landmark[4].x and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[14].y > \
                lst.landmark[16].y:
            c = 3
        if lst.landmark[8].x < lst.landmark[4].x:
            c = 4
        if lst.landmark[8].x < lst.landmark[4].x and lst.landmark[18].y > lst.landmark[20].y:
            c = 5
        if lst.landmark[8].x < lst.landmark[4].x and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[14].y > \
                lst.landmark[16].y:
            c = 6
        if lst.landmark[8].x < lst.landmark[4].x and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[14].y > \
                lst.landmark[16].y and lst.landmark[10].y > lst.landmark[12].y:
            c = 7
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[2].y > \
                lst.landmark[4].y and lst.landmark[8].x < lst.landmark[4].x:
            c = 9
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[14].y > \
                lst.landmark[16].y and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[2].y > lst.landmark[
            4].y and lst.landmark[8].x < lst.landmark[4].x:
            c = 8
        return c

    def keybord(ctt):
        # Code to be executed in another thread
        if ctt == 2:
            pyautogui.click(button='left')
            print("m-left")
        elif ctt == 3:
            pyautogui.click(button='right')
            print("m-right")
        elif ctt == 4:
            pyautogui.press("up")
            print("k-up")
        elif ctt == 5:
            pyautogui.press("down")
            print("k-down")
        elif ctt == 6:
            pyautogui.press("left")
            print("k-left")
        elif ctt == 7:
            pyautogui.press("right")
            print("k-right")
        elif ctt == 8:
            print("closing entire program")
            sys.exit()
        elif ctt == 9:
            cv2.destroyAllWindows()
            return "hand"

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    # Set the minimum time (in seconds) to wait before recognizing another hand gesture
    gesture_delay = 1
    last_gesture_time = time.time() - gesture_delay

    # For webcam input:
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            # Wait for the thread to finish)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
                    # Check if enough time has passed since the last gesture
                    current_time = time.time()
                    ctt = count_fingers(results.multi_hand_landmarks[0])
                    if current_time - last_gesture_time > gesture_delay:
                        print(ctt)
                        shift = keybord(ctt)
                        if shift == "hand":
                            return "hand"
                        last_gesture_time = current_time
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Hands', image)
            # cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()


mouse_control()