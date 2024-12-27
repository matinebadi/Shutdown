
# System Control - PyQt5 Application

A desktop application built using **PyQt5** for controlling system actions such as shutdown, restart, and cancel. The application features a modern, interactive UI with a **background GIF** and **custom-styled buttons**.

## ✨ Features

- **Background GIF:** A GIF that plays as the background for the application, creating a dynamic effect.
- **Shutdown & Restart:** Allows the user to shut down or restart the system with a 7-second delay.
- **Cancel:** Cancels the current operation and closes the application.
- **Hover Effects on Buttons:** Buttons change style when hovered to provide a dynamic user experience.

## ⚙️ Requirements

To run the application, you need the following dependencies:

- **Python 3.x**
- **PyQt5**: To install the required library, use:

```bash
pip install pyqt5

🚀 How to Run

1. Clone or download the project to your local machine.


2. Open a terminal and navigate to the project directory.


3. Run the script by executing the following command:



python system_control.py

🧑‍💻 Code Explanation

User Interface

The UI is built using PyQt5 and consists of:

Title Label: A centered label displaying the text "Choose an action".

Action Buttons: Includes buttons for Shutdown, Restart, and Cancel. Each button has a hover effect.

Background GIF: A dynamic background GIF is displayed using QMovie.


Button Styles and Effects

The buttons are customized using CSS and feature hover effects to change the background color when the mouse hovers over them. Here’s the breakdown:

Shutdown: Triggers the system shutdown with a 7-second delay.

Restart: Triggers a system restart with a 7-second delay.

Cancel: Closes the application and cancels any operation.


System Actions

The shutdown and restart functions use the os.system() command to invoke system shutdown or restart.


Window Setup

The window size is set to 300x300 pixels, and it is not resizable.

Transparency and Background Color: The window has a semi-transparent background with a customized color using CSS.


