import pyautogui
import keyboard
import time

# Function to perform mouse click and drag based on arrow key presses
def simulate_mouse_drag():
    # Monitor arrow key presses to control mouse movement
    while True:
        if keyboard.is_pressed('up'):
            pyautogui.mouseDown(button='left')
            pyautogui.move(0, -50)  # Adjust the value based on the distance you want to move
            pyautogui.mouseUp(button='left')
            #time.sleep(0.1)  # Adjust the sleep time based on your preference
            pyautogui.move(0, 50)
        elif keyboard.is_pressed('down'):
            pyautogui.mouseDown(button='left')
            pyautogui.move(0, 50)  # Adjust the value based on the distance you want to move
            pyautogui.mouseUp(button='left')
            #time.sleep(0.1)  # Adjust the sleep time based on your preference
            pyautogui.move(0, -50)
        elif keyboard.is_pressed('left'):
            pyautogui.mouseDown(button='left')
            pyautogui.move(-50, 0)  # Adjust the value based on the distance you want to move
            pyautogui.mouseUp(button='left')
            #time.sleep(0.1)  # Adjust the sleep time based on your preference
            pyautogui.move(50, 0)
        elif keyboard.is_pressed('right'):
            pyautogui.mouseDown(button='left')
            pyautogui.move(50, 0)  # Adjust the value based on the distance you want to move
            pyautogui.mouseUp(button='left')
            pyautogui.move(-50, 0)
            #time.sleep(0.1)  # Adjust the sleep time based on your preference
        elif keyboard.is_pressed('space'):
            pyautogui.mouseDown(button='left')
            time.sleep(0.05)
            pyautogui.mouseUp(button='left')
            time.sleep(0.05)
            pyautogui.mouseDown(button='left')
            time.sleep(0.05)
            pyautogui.mouseUp(button='left')

# Main function
def main():
    print("Press 'Q' to quit.")
    simulate_mouse_drag()

# Execute main function
if __name__ == "__main__":
    main()
