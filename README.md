
![shutdown](https://github.com/user-attachments/assets/a960ec4e-8edd-48d9-b518-d2fbe3eb68cf)

![Uploading icon.PNG…]()


1.Library Imports:
   - The necessary libraries for building the user interface and system control have been imported.

2.SystemControl Class:
   - This class inherits from QWidget and is responsible for creating the user interface.

3. __init__ Method:
   - This is the main constructor that calls the parent class constructor (super().__init__) and invokes the initUI() method.

4. initUI Method:
   - Here, the initial UI settings are configured:
     - The window title and size are set.
     - A QLabel is added to display a GIF animation in the background.
     - The GIF is loaded and displayed.
     - A QVBoxLayout for vertically arranging the widgets is created.
     - Titles and buttons are generated and added to the layout.

5.create_button Method:
   - This method creates buttons with a specific style and a callback function.
   - Additionally, events are defined to change the button style when the mouse enters or leaves.

6.change_button_style Method:
   - This method manages the appearance changes of the buttons during mouse movement.

7. Button Functions:
   - Shutdown:Clicking this button shows a message that the system will shut down in 7 seconds, then issues the shutdown command.
   - Restart: Functions similarly to the shutdown button but restarts the system.
   - Cancel: Clicking this button displays a message and closes the window.

8. Running the Program:
   - Finally, the program is executed using QApplication, and the SystemControl class is displayed.

Key Points:
- Events and Callbacks: Using connect to link events to specific functions.
- Interactive UI: Improved user experience through changes and animations.
- System Interaction: Commands can be executed using os.system.
