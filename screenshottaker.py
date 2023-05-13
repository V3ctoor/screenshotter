import os
import time
import ctypes
from mss import mss
from mss.tools import to_png
from screeninfo import get_monitors
from PIL import Image, ImageDraw, ImageFont

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

def get_idle_time():
    last_input_info = LASTINPUTINFO()
    last_input_info.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(last_input_info))
    return (ctypes.windll.kernel32.GetTickCount() - last_input_info.dwTime) / 1000

def is_user_idle():
    idle_time_seconds = get_idle_time()
    return idle_time_seconds > 10

def add_timestamp(image, text):
    font_size = 20
    font = ImageFont.truetype("arial.ttf", font_size)
    draw = ImageDraw.Draw(image)
    text_bbox = draw.textbbox((0, 0), text, font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    x, y = 5, image.height - text_height - 5

    # Draw the text with a black outline
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        draw.text((x + dx, y + dy), text, font=font, fill=(0, 0, 0))

    # Draw the text in white
    draw.text((x, y), text, font=font, fill=(255, 255, 255))

def take_screenshot():
    # Get the current timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    date = time.strftime("%Y-%m-%d")

    # Create a folder named 'screenshots' if it doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Create a folder for the current day if it doesn't exist
    daily_folder = os.path.join("screenshots", date)
    if not os.path.exists(daily_folder):
        os.makedirs(daily_folder)

    # Iterate over all connected monitors
    with mss() as sct:
        for i, monitor in enumerate(get_monitors()):
            # Create a folder for the current monitor if it doesn't exist
            monitor_folder = os.path.join(daily_folder, f"monitor_{i+1}")
            if not os.path.exists(monitor_folder):
                os.makedirs(monitor_folder)

            # Capture a screenshot of the current monitor
            screenshot = sct.grab({
                "top": monitor.y,
                "left": monitor.x,
                "width": monitor.width,
                "height": monitor.height
            })

            # Convert the screenshot to a PIL image and add the timestamp
            pil_image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
            add_timestamp(pil_image, timestamp)

            # Save the screenshot with the timestamp in the file name
            screenshot_path = os.path.join(monitor_folder, f"{timestamp}_screenshot.png")
            pil_image.save(screenshot_path, "PNG")
            print(f"Screenshot saved for monitor {i+1} to {screenshot_path}")
            pil_image.close()  # Close the PIL image object to free memory

def log_error(error_message):
    log_file = "error_log.txt"
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    with open(log_file, "a") as f:
        f.write(f"{timestamp}: {error_message}\n")

def main():
    while True:
        try:
            if not is_user_idle():
                take_screenshot()
        except Exception as e:
            error_message = f"Error occurred: {e}"
            log_error(error_message)
        time.sleep(30)  # Wait for 30 seconds

if __name__ == "__main__":
    main()