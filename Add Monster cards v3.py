"""Allow user to add in new cards in to the program, by displaying the enterbox
 and let the user enter each values for each of the status fields"""


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

enterbox_fields = ["Card name", "Strength", "Speed", "Stealth", "Cunning"]
enterbox_msg = "Enter your card information"
enterbox_title = "Add Monster cards"

# Display a message box and receive the user's input
monster_info = easygui.multenterbox(title=enterbox_title, msg=enterbox_msg, fields=enterbox_fields)

if monster_info is None:
    easygui.msgbox("Cancelled")
    exit()

# Start a loop to allow the user to add new monster cards
while True:

    # Define a list of fields for the message box
    monster_info = easygui.multenterbox(title=enterbox_title,
                                    msg="Confirm the card info",
                                    fields=enterbox_fields,
                                    values=monster_info)


    check = False

    if monster_info is None:
        easygui.msgbox("Cancelled")
        break
    # Check if the user has cancelled

    for enterbox_info in monster_info[1:]:
        try:
            creasture_values = int(enterbox_info)
        except ValueError:
            easygui.msgbox("Please enter a valid number for the status fields")
            break
        else:
            if creasture_values > 25 or creasture_values < 1:
                easygui.msgbox("Please enter number between 1 to 25")
                break

    else:
        for item in monster_info:
                if item == "":
                    check = True
        if check is True:
            continue
        else:
            # If the user has entered valid input, add the new monster card to the dictionary
            creatures[monster_info[0]] = {"Strength": int(monster_info[1]), "Speed": int(monster_info[2]),
                                        "Stealth": int(monster_info[3]), "Cunning": int(monster_info[4])}
            break
    

# Print the updated dictionary
title_add = "Updated dictionary:"
header = "Monster:\t\tStrength:\tSpeed:\t\tStealth:\tCunning:"

# Create a list to store each row of data
rows = []

# Iterate through the dictionary and append each row to the list
for creature_display, stats_display in creatures.items():
    # Format each row with the creature name and its stats
    row = f"{creature_display}\t\t{stats_display['Strength']}\t\t{stats_display['Speed']}\t\t{stats_display['Stealth']}\t\t{stats_display['Cunning']}"
    rows.append(row)

# Join the header and rows together with a newline character '\n'
table = '\n'.join([header] + rows)

# Print the table to the console
print(table)

# Display the table in a message box using easygui
easygui.msgbox(title=title_add, msg=table)


