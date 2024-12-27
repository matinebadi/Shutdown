

# System Control - PyQt5

A desktop application built using PyQt5 to control system shutdown and restart with a user-friendly GUI. The app also plays an animated GIF in the background to enhance the visual experience.

## Features

- **Shutdown and Restart:** Allows the user to shut down or restart the system with a 7-second delay.
- **Cancel Option:** Provides an option to cancel any pending actions.
- **Customizable Buttons:** Stylish buttons with hover and click effects.
- **Animated Background:** Displays a GIF as the background for a visually dynamic interface.
- **Responsive Layout:** The app is designed to be responsive, adjusting to different screen sizes.

## Requirements

- Python 3.x
- PyQt5

To install the required dependencies, run the following command:

```bash
pip install PyQt5

How to Run

1. Clone or download the project.


2. Open a terminal and navigate to the project directory.


3. Run the script:



python system_control.py

Code Explanation

Window and Layout Setup

The main window is set with a fixed size of 300x300 and a background GIF. The layout includes a title label and three buttons: Shutdown, Restart, and Cancel.

Animated GIF Background

The QMovie class is used to load and play an animated GIF in the background. The setMovie method sets the GIF, and it starts automatically.

Buttons and Interactions

Each button is created using a custom create_button method. The buttons change their style on hover and click, providing a dynamic user experience. The shutdown, restart, and cancel methods perform the respective actions.

Shutdown and Restart

The shutdown and restart functions use the os.system() command to initiate system actions with a 7-second delay.

Cancel

The cancel button stops any ongoing operation and closes the window.

