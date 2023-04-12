# Automatic Screenshot Taker

This Python script takes a screenshot of each connected monitor every 30 seconds and saves the images with a timestamp in separate folders for each day and monitor. The program also overlays the timestamp on each screenshot.

## Requirements

- Python 3.6 or later
- mss
- screeninfo
- pillow

## Installation

1. Clone the repository or download the `screenshottaker.py` script.
2. Install the required libraries:
pip install mss screeninfo pillow

## Usage

1. Navigate to the folder containing the `screenshottaker.py` script.
2. Run the script:
python screenshottaker.py

The script will start taking screenshots every 30 seconds and save them in the `screenshots` folder, organized by date and monitor. Screenshots will not be taken when the user is idle for more than 10 seconds.

## Running the script in the background
1. Make sure the screenshot.bat file is in the same folder as the `screenshottaker.py` script.
2. Run the .bat file.
3. To stop the script from running, use the task manager to end the python task.

## Customization

If you want to change the screenshot interval or the idle time threshold, you can modify the following lines in the `screenshottaker.py` script:

time.sleep(30)  # Change the number of seconds to wait between screenshots

return idle_time_seconds > 10  # Change the idle time threshold in seconds

## License

This project is licensed under the MIT License.

Copyright 2023 Victor Johansson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
