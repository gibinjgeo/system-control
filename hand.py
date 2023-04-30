import mediapipe as mp
import cv2
import pyautogui
import time

def hand_gesture():
    def count_fingers(lst):
        c = 0
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[8].x > lst.landmark[4].x:
            c = 1
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[8].x > \
                lst.landmark[4].x:
            c = 2
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[14].y > \
                lst.landmark[16].y and lst.landmark[8].x > lst.landmark[4].x:
            c = 3
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[14].y > \
                lst.landmark[16].y and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[8].x > lst.landmark[
            4].x:
            c = 4
        if lst.landmark[8].x < lst.landmark[4].x:
            c = 6
        if lst.landmark[8].x < lst.landmark[4].x and lst.landmark[6].y > lst.landmark[8].y:
            c = 7
        if lst.landmark[8].x < lst.landmark[4].x and lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > \
                lst.landmark[12].y:
            c = 8
        if lst.landmark[8].x < lst.landmark[4].x and lst.landmark[6].y > lst.landmark[8].y and lst.landmark[18].y > \
                lst.landmark[20].y:
            c = 10
        if lst.landmark[8].x < lst.landmark[4].x and lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > \
                lst.landmark[12].y and lst.landmark[18].y > lst.landmark[20].y:
            c = 9
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[14].y > \
                lst.landmark[16].y and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[2].y > lst.landmark[
            4].y and lst.landmark[8].x < lst.landmark[4].x:
            c = 5
        return c

    def left_rec(lst):
        c = 0
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[8].x < lst.landmark[4].x:
            c = 1
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[8].x < \
                lst.landmark[4].x:
            c = 2
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[14].y > \
                lst.landmark[16].y and lst.landmark[8].x < lst.landmark[4].x:
            c = 3
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[14].y > \
                lst.landmark[16].y and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[8].x < lst.landmark[
            4].x:
            c = 4
        if lst.landmark[2].y > lst.landmark[4].y and lst.landmark[8].x > lst.landmark[4].x:
            c = 6
        if lst.landmark[2].y > lst.landmark[4].y and lst.landmark[8].x > lst.landmark[4].x and lst.landmark[6].y > \
                lst.landmark[8].y:
            c = 7
        if lst.landmark[2].y > lst.landmark[4].y and lst.landmark[8].x > lst.landmark[4].x and lst.landmark[6].y > \
                lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y:
            c = 8
        if lst.landmark[2].y > lst.landmark[4].y and lst.landmark[8].x > lst.landmark[4].x and lst.landmark[6].y > \
                lst.landmark[8].y and lst.landmark[18].y > lst.landmark[20].y:
            c = 10
        if lst.landmark[2].y > lst.landmark[4].y and lst.landmark[8].x > lst.landmark[4].x and lst.landmark[6].y > \
                lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[18].y > lst.landmark[
            20].y:
            c = 9
        if lst.landmark[6].y > lst.landmark[8].y and lst.landmark[10].y > lst.landmark[12].y and lst.landmark[14].y > \
                lst.landmark[16].y and lst.landmark[18].y > lst.landmark[20].y and lst.landmark[2].y > lst.landmark[
            4].y and lst.landmark[8].x > lst.landmark[4].x:
            c = 5
        return c

    def keybord(ctt):
        if ctt == 1:
            pyautogui.hotkey('ctrl', 'c')
            print("index finger only-one")
        elif ctt == 2:
            pyautogui.hotkey('ctrl', 'v')
            print("middle finger-two")
        elif ctt == 3:
            pyautogui.press('f11')
            print("3 rd finger raised")
        elif ctt == 4:
            pyautogui.hotkey('win', 'tab')
            print("pingy finger-four")
        elif ctt == 5:
            pyautogui.hotkey('alt', 'tab')
            print("index finger-five")
        elif ctt == 6:
            pyautogui.hotkey('win', 'q')
            print("right thumb-six")
        elif ctt == 7:
            pyautogui.hotkey('ctrl', 'tab')
            print("thum+index-seven")
        elif ctt == 8:
            pyautogui.hotkey('ctrl', 'a')
            print("thumb+index+middle-eight")
        elif ctt == 9:
            pyautogui.hotkey('win', 'e')
            print("open palm with ring finger closed-ten")
        elif ctt == 10:
            cv2.destroyAllWindows()
            print("ilu-nine")
            return "asl"

    def keybordl(ctt):
        if ctt == 1:
            pyautogui.press('1')
            print("index finger only-one")
        elif ctt == 2:
            pyautogui.press('2')
            print("middle finger-two")
        elif ctt == 3:
            pyautogui.press('3')
            print("3 rd finger raised")
        elif ctt == 4:
            pyautogui.press('4')
            print("pingy finger-four")
        elif ctt == 5:
            pyautogui.press('5')
            print("index finger-five")
        elif ctt == 6:
            pyautogui.press('6')
            print("right thumb-six")
        elif ctt == 7:
            pyautogui.press('7')
            print("thum+index-seven")
        elif ctt == 8:
            pyautogui.press('8')
            print("thumb+index+middle-eight")
        elif ctt == 9:
            pyautogui.press('9')
            print("ilu-nine")
        elif ctt == 10:
            pyautogui.press('0')
            print("open palm with ring finger closed-ten")

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    # Set the minimum time (in seconds) to wait before recognizing another hand gesture
    gesture_delay = 1
    last_gesture_time = time.time() - gesture_delay

    # For webcam input:
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
            model_complexity=0,
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
                    if current_time - last_gesture_time > gesture_delay:
                        landmarks = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
                        # Check if the hand is left or right
                        if landmarks[mp_hands.HandLandmark.WRIST] < landmarks[mp_hands.HandLandmark.THUMB_CMC]:
                            print("Right")
                            ctt = count_fingers(results.multi_hand_landmarks[0])
                            print(ctt)
                            shift = keybord(ctt)
                            if shift == "asl":
                                return "asl"
                            last_gesture_time = current_time
                        else:
                            print("Left")
                            ctt = left_rec(results.multi_hand_landmarks[0])
                            print(ctt)
                            keybordl(ctt)
                            last_gesture_time = current_time
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()


hand_gesture()