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

# Start a loop to allow the user to add new monster cards
while True:

    # Define a list of fields for the message box
    enterbox_fields = ["Card name", "Strength", "Speed", "Stealth", "Cunning"]
    enterbox_msg = "Enter your card information"
    enterbox_title = "Add Monster cards"

    # Display a message box and receive the user's input
    monster_info = easygui.multenterbox(title=enterbox_title, msg=enterbox_msg, fields=enterbox_fields)
    monster_info = easygui.multenterbox(title=enterbox_title,
                                        msg="Confirm the card info",
                                        fields=enterbox_fields,
                                        values=monster_info)


    #Add the new monster card to the dictionary
    creatures[monster_info[0]] = {"Strength": monster_info[1], "Speed": monster_info[2],
                                    "Stealth": monster_info[3], "Cunning": monster_info[4]}


    print(creatures)


