"""Display a menu of buttons box for user to select: 
Add monster cards, delete monster cards, Configure monster card, Display monster cards"""


import easygui

title_output = "Hello"
MSG = "Choose one of the following buttons"
buttons = ["Display", "Add", "Delete", "Configure", "Search"]
easygui.buttonbox(msg=MSG, title=title_output, choices=buttons)