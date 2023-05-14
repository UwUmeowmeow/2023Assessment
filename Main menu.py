"""Display a menu of buttons box for user to select: 
Add monster cards, delete monster cards, Configure monster card, Display monster cards"""


import easygui


while True:
    title_output = "Hello"
    MSG = "Choose one of the following buttons"
    buttons = ["Display", "Add", "Delete", "Configure", "Search", "Exit"]
    select_button = easygui.buttonbox(msg=MSG, title=title_output, choices=buttons)

    if select_button == "Exit":
        easygui.msgbox("You Exit the program")
        break
    