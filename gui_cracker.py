# pip install pyautogui
# To get coordinates:
# import pyautogui
# print(pyautogui.position())

import pyautogui
import time
import os

def click_at_coordinates(x, y):
    """Move to (x, y) and perform a mouse click."""
    pyautogui.moveTo(x, y, duration=0.1)  # Smoothly move to (x, y)
    pyautogui.click()

def type_number(number):
    """Type a given number into the input field."""
    pyautogui.typewrite(str(number), interval=0.05)

def element_exists(image_path):
    """
    Check if a UI element is present on the screen.
    Uses an image of the UI element for detection.
    """
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        return location is not None
    except pyautogui.ImageNotFoundException:
        return False

def save_tried_number(number, file_path="numbers_tried.txt"):
    """Record the number tried so far into a file."""
    with open(file_path, "a") as file:
        file.write(f"{number}\n")

def main(input_coords, start_number=1, max_number=999999, log_file="numbers_tried.txt"):
    """
    Main function to automate entering sequential numbers and clicking confirm.
    
    - input_coords: (x, y) tuple for the input box.
    - confirm_coords: (x, y) tuple for the confirm button.
    - confirm_button_image: Path to the image of the confirm button for detection.
    - start_number: Starting number for the sequence.
    - max_number: Maximum number to try.
    - log_file: Path to the file to log numbers tried.
    """
    current_number = start_number

    # Ensure log file exists
    if not os.path.exists(log_file):
        with open(log_file, "w") as file:
            file.write("Numbers Tried:\n")
    
        #click_at_coordinates(*input_coords)
        #time.sleep(0.2)  # Wait for the input box to focus

    while current_number <= max_number:  # Loop while numbers remain and button exists
        # Click the input box
        click_at_coordinates(*input_coords)
        time.sleep(1)  # Wait for the input box to focus

        pyautogui.press('enter')
        time.sleep(2)

        # Type the current number
        type_number(current_number)
        print(f"Entered number: {current_number}")
        
        # Save the number to the log file
        save_tried_number(current_number, log_file)
        time.sleep(2)
        
        # Click the confirm button
        #click_at_coordinates(*confirm_coords)
        pyautogui.press('enter')
        print(f"Clicked confirm button for {current_number}")
        time.sleep(2)

        pyautogui.press('enter')
        time.sleep(1)

        # Increment the number for the next iteration
        current_number += 1
        time.sleep(1)  # Wait for the system to process the click
    
    print("Completed. Either maximum number reached or confirm button is no longer present.")

if __name__ == "__main__":
    # Example usage
    # Replace these with actual (x, y) coordinates for the input field and confirm button
    input_coords = (518, 81)  # Replace with the (x, y) of your input field

    #confirm_coords = (600, 400)  # Replace with the (x, y) of your confirm button
    #confirm_button_image = "confirm_button.png"  # Replace with a screenshot of the confirm button
    
    # Starting number for the sequence
    start_number = 1
    
    print("Starting automation...")
    #main(input_coords, confirm_coords, confirm_button_image, start_number=start_number)
    main(input_coords, start_number=start_number)
    print("Automation finished.")
