import pyautogui
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
import time

# Define the path to save the screenshots
screenshot_path = "/Users/rraman/Documents/automator_screenshots/"

# Function to take a screenshot of a selected portion
def take_screenshot(x1, y1, x2, y2, count):
    timestamp = f"{count:03d}"
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screenshot.save(f"{screenshot_path}{timestamp}.png")

# Create a flag to track if 'q' is pressed
exit_flag = False

# Function to handle keypress
def on_key_release(key):
    global exit_flag
    if key == Key.esc:
        exit_flag = True

#initial sleep of 10 seconds
time.sleep(5)

# Start the key listener
with Listener(on_release=on_key_release) as listener:
    # Number of iterations
    for i in range(1, 370):
        # Define the coordinates for the selected portion (change as needed)
        #x1, y1, x2, y2 = 290, 1437, 1437, 1015  # Example coordinates
        x1=290
        x2=1437
        y1=219
        y2=1015
        take_screenshot(x1, y1, x2, y2, i)
        pyautogui.press('right')  # Send a right arrow key press

        if exit_flag:
            break

        time.sleep(3)  # Wait for 3 seconds before the next screenshot

# Release any held keys (important for the script not to interfere with regular keyboard use)
pyautogui.press('right', presses=369, interval=0.01)
