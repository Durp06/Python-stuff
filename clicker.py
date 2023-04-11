import pyautogui
import time
#thx chatGPT :3
# Set the coordinates for the first position
pos1 = (279, 191)

# Set the coordinates for the second position
pos2 = (429, 191)

# Set the number of times to repeat the action
num_repeats = 35
#pyautogui.displayMousePosition() | find coordinates
# Loop through the number of repeats
for i in range(num_repeats):
    # Move the mouse to the first position
    pyautogui.moveTo(pos1[0], pos1[1])
    # Click the left mouse button
    pyautogui.click()
    # Move the mouse to the second position
    pyautogui.moveTo(pos2[0], pos2[1])
    # Click the left mouse button
    pyautogui.click()
    # Pause for a moment before repeating
    time.sleep(0.25)
