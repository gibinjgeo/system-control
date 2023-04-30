import hand
import mouse
import asl
import time


def start():
    try:
        capt = mouse.mouse_control()
        print(capt)
        if capt == "hand":
            capt = hand.hand_gesture()
            print(capt)
            if capt == "asl":
                time.sleep(4)
                capt = asl.new()
                print(capt)
                if capt == "mouse":
                    return start()
    except:
        print("either some error occured or system restarted")
        start()


start()
