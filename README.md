
# System Control - PyQt5 Application

A desktop application built using PyQt5 for controlling system actions like shutdown, restart, and cancel. The application features an interactive UI with a background GIF and custom-styled buttons.

## Features

- **Background GIF:** A GIF that plays as the background for the application.
- **Shutdown & Restart:** Allows the user to shut down or restart the system with a 7-second delay.
- **Cancel:** Cancels the current operation and closes the application.
- **Hover Effects:** Buttons change style when hovered to provide a dynamic user experience.

## Requirements

- Python 3.x
- PyQt5

You can install the required library using pip:

```bash
pip install pyqt5

How to Run

1. Clone or download the project.


2. Open a terminal and navigate to the project directory.


3. Run the script:



python system_control.py

Code Explanation

User Interface

The UI is built using PyQt5 and contains the following:

Title Label: Displays "Choose an action" centered at the top of the window.

Action Buttons: Includes buttons for shutdown, restart, and cancel. These buttons change style when hovered.

Background GIF: A GIF is displayed in the background using QMovie.


Buttons and Styling

The buttons are styled using CSS and feature hover effects that change the background color. The buttons are connected to their respective functions:

Shutdown: Initiates system shutdown with a 7-second delay.

Restart: Initiates system restart with a 7-second delay.

Cancel: Cancels any operation and closes the application.


System Actions

The shutdown and restart actions are handled using the os.system() command to execute system shutdown or restart commands.


Window Setup

The window is set to a fixed size of 300x300 pixels.

The background color and transparency are customized with CSS.

