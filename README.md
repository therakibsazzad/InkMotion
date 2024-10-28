
# InkMotion - A Virtual Whiteboard with Hand Gesture Recognition

InkMotion is an intuitive virtual whiteboard that uses OpenCV and cvzone’s hand detection to turn hand gestures into drawing tools! Select colors, switch between drawing and erasing, and more—all with the flick of a finger.

## Visuals
![Screenshot 2024-10-28 at 9 24 35 PM](https://github.com/user-attachments/assets/88048397-493b-4be1-8b4d-c76f6c769eb9)
![1730045105260711](https://github.com/user-attachments/assets/f7aee652-803f-432f-86bd-caf5816324fd)
![1730042275475931](https://github.com/user-attachments/assets/929f9532-28b2-4f50-abbd-0a19e3925f49)
![1730045382584283](https://github.com/user-attachments/assets/14ebdac0-679d-45f0-b662-2751a370f57e)


## Features
- Draw with Gestures: Use your index finger for drawing, and two fingers for selecting tools.
- Dynamic Color Selection: Choose colors by tapping on different parts of the header.
- Erase with Ease: Switch to eraser mode by selecting the eraser option.
- Smooth & Responsive: Real-time hand tracking ensures fluid drawing.


## Installation

### Requirements
- **Python 3.x**
- **Libraries**:
  - `opencv-python-headless` (for image processing)
  - `cvzone` (for hand tracking and gesture recognition)
  - `numpy` (for array handling)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/therakibsazzad/InkMotion.git
   cd InkMotion
   ```

2. Install the required libraries:
   ```bash
   pip install opencv-python-headless cvzone numpy
   ```

3. Ensure that you have a folder named `Header` in the project directory, which should contain images for color and tool selection overlay. You can add any images you'd like to use for color selection in this folder.

## Usage

1. **Run the Application**:
   ```bash
   python ink_motion.py
   ```

2. **Drawing and Erasing**:
   - **Drawing Mode**: Raise your index finger to start drawing.
   - **Selection Mode**: Raise both your index and middle fingers to select colors or switch to eraser mode.
     - **Red, Green, Purple, Eraser, and [InkBoard]** color options are available by tapping on different areas in the header.
   - **Erase**: Select the eraser color from the header and move your index finger over areas to erase.

3. **Controls**:
   - **Esc**: Close the application.


## Contributing
Want to help improve InkMotion? Contributions are welcome! If you encounter bugs or have feature suggestions, feel free to open an issue or submit a pull request. Let’s enhance this project together!
