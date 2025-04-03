# Hand Gesture Controlled Browser Launcher

This project uses **OpenCV** and **MediaPipe** to detect hand gestures via a webcam. A specific hand gesture (middle finger down) is used to open a browser and navigate to ChatGPT. The project consists of three Python files:

`CV.py`: The main script handling webcam input and gesture detection.

`hand_detection.py`: Defines the hand detection class using MediaPipe.

`port_forwarding.py`: Contains a function to open a browser window.


## Usage

### 1. Running the Application

Start the program by executing:

`python CV.py`

This will activate the webcam and begin tracking hands.

### 2. Triggering the Browser Open Function

If you lower your middle finger (landmark `12`) below your index finger (landmark `8`), the script will open a browser window to ChatGPT.

A boolean (`open_browser`) prevents multiple instances from opening.

(TODO): Implement a gesture to reset `open_browser` to `False`.

## File Structure & Explanation

### 1. CV.py

Initializes the webcam and hand detector.

Continuously detects hands and their positions.

Calls `pf.open_browser()` when the trigger gesture is detected.

### 2. hand_detection.py

Implements `handDetector` class using MediaPipe.

Extracts hand landmarks and returns them as a list.

### 3. port_forwarding.py

Defines `open_browser()` to open ChatGPT using Python’s webbrowser module.

## Future Improvements

Add saving custom handgestures and link them to preferred websites.

Add default gestures to toggle reading on / off.

Add support for additional commands using different hand gestures.

Add UI (focus on MacBook dynamic island).
