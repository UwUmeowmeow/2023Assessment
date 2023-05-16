"""Display a enterbox and allow user to type in Monster name, and display the monster name and status"""

# Import the easygui module for displaying a message box
import easygui

# Define a dictionary of creatures and their stats
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

# Prompt the user to enter a creature name to search for
searched_monster = easygui.enterbox("Type in creature that you want to search: ")

# Check if the entered creature name exists in the dictionary
if searched_monster in creatures:
    # Prepare the title and message to display the creature's stats
    search_title = f"Searched Monster: {searched_monster}"
    search_msg = (f"Strength: {creatures[searched_monster]['Strength']}\n"
                  f"Speed: {creatures[searched_monster]['Speed']}\n"
                  f"Stealth: {creatures[searched_monster]['Stealth']}\n"
                  f"Cunning: {creatures[searched_monster]['Cunning']}")
    # Display a message box with the creature's stats
    easygui.msgbox(title=search_title, msg=search_msg)
else:
    # Display an error message if the creature is not found
    easygui.msgbox("Creature not found.")
