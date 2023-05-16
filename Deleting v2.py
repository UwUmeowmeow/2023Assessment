"""Allow user to select Monster cards and delete the cards from the dictionary"""

# Import the easygui module for displaying a message box
import easygui

# Dictionary of monster cards with their stats
creatures = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

while True:
    # Create a list of available monster card names
    choices = []
    for name, stats in creatures.items():
        choices.append(name)

    # Display a dialog box for the user to select monster cards to delete
    selected = easygui.multchoicebox(choices=choices)
    print(selected)

    if selected is None: # If the user pressed cancel it should exit the loop 
        easygui.msgbox("Canceled")
        break

    # If the user didn't select print the message and run the loop again
    elif selected == []:
        easygui.msgbox("Please select at least one option")

    else:
        # Delete the selected monster cards from the dictionary
        for item in selected:
            del creatures[item]

        # Print the updated dictionary after deleting the cards
        print(creatures)
        break  # Exit the loop

