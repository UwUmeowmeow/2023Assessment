"""Display a menu of buttons box for user to select: 
Add monster cards, delete monster cards, Configure monster card, Display monster cards"""

# Import the easygui module for displaying a message box
import easygui

# Looping
while True:
    # Title for the message box
    title_output = "Hello"

    # Message to display in the message box
    MSG = "Choose one of the following buttons"

    # List of buttons for the user to select
    buttons = ["Display", "Add", "Delete", "Configure", "Search", "Exit"]

    # Display the message box with the button choices and store the selected button
    select_button = easygui.buttonbox(msg=MSG, title=title_output, choices=buttons)

    # If the user selects "Exit", display a message and break out of the loop
    if select_button == "Exit":
        easygui.msgbox("You Exit the program")
        break
