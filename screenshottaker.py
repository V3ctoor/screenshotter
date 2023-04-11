import os
import time
import ctypes
from mss import mss
from mss.tools import to_png
from screeninfo import get_monitors

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

            # Save the screenshot with the timestamp in the file name
            screenshot_path = os.path.join(monitor_folder, f"{timestamp}_screenshot.png")
            to_png(screenshot.rgb, screenshot.size, output=screenshot_path)
            print(f"Screenshot saved for monitor {i+1} to {screenshot_path}")

def main():
    while True:
        if not is_user_idle():
            take_screenshot()
        time.sleep(30)  # Wait for 30 seconds

if __name__ == "__main__":
    main()