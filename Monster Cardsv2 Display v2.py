"""Store each monster cards information; display all the Monster cards"""


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

# Define the header of the table
header = "Monster:\t\tStrength:\tSpeed:\t\tStealth:\tCunning:"

# Create a list to store each row of data
rows = []

# Iterate through the dictionary and append each row to the list
for creature, stats in creatures.items():
    # Format each row with the creature name and its stats
    row = f"{creature}\t\t{stats['Strength']}\t\t{stats['Speed']}\t\t{stats['Stealth']}\t\t{stats['Cunning']}"
    rows.append(row)

# Join the header and rows together with a newline character '\n'
table = '\n'.join([header] + rows)

# Print the table to the console
print(table)

# Display the table in a message box using easygui
easygui.msgbox(table)
