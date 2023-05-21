"""Display a enterbox and allow user to type in Monster name, and display the monster name and status"""

# Import the easygui module for displaying a message box
import easygui

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


def f_display_creature():
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


def f_add_creature():
    #list each datailes for the enterbox
    enterbox_fields = ["Card name", "Strength", "Speed", "Stealth", "Cunning"]
    enterbox_msg = "Enter your card information"
    enterbox_title = "Add Monster cards"

    # Display a message box and receive the user's input
    monster_info = easygui.multenterbox(title=enterbox_title, msg=enterbox_msg, fields=enterbox_fields)

    if monster_info is None:
        
        return False
    # Start a loop to allow the user to add new monster cards
    while True:

        # Define a list of fields for the message box
        monster_info = easygui.multenterbox(title=enterbox_title,
                                        msg="Confirm the card info",
                                        fields=enterbox_fields,
                                        values=monster_info)


        check = False

        if monster_info is None:
            return False
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


def f_configure_creature():
    # Allow user to type in the search box
    searched_monster = easygui.enterbox("Enter the name of the creature you want to edit: ")

    # Check if the entered creature name exists in the dictionary
    if searched_monster in creatures:
        # If the creature exists, allow the user to edit its stats
        creature_stats = creatures[searched_monster]
        updated_stats = {}
        for stat in creature_stats:
            new_value = easygui.enterbox(f"Enter new value for {stat} (current value: {creature_stats[stat]}): ")
            if new_value is not None:
                updated_stats[stat] = int(new_value)
            else:
                updated_stats[stat] = creature_stats[stat]
        creatures[searched_monster] = updated_stats
        # Display the updated stats of the creature
        new_msg = ""
        title = f"{searched_monster}\n"
        for stat_name, stat_value in updated_stats.items():
            new_msg += f"\n{stat_name} : {stat_value}"
        easygui.msgbox(title=title, msg=new_msg)
    else:
        # If the creature does not exist, display an error message
        easygui.msgbox(f"{searched_monster} not found in the dictionary.")


def f_search_creature(searched_monster):
    # Prompt the user to enter a creature name to search for
    

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


def f_delete_creature():
    # Loop
    while True:
        # Create a list of available monster card names
        choices = []
        for name, stats in creatures.items():
            choices.append(name)

        # Display a dialog box for the user to select monster cards to delete
        selected = easygui.multchoicebox(choices=choices)

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
            
            f_display_creature()
            break

        
# Main routine
# Looping
while True:
    # Title for the message box
    title_output = "Hello"

    # Message to display in the message box
    MSG = "Choose one of the following buttons"

    # List of buttons for the user to select
    buttons = ["Display", "Add","Configure", "Delete", "Search", "Exit"]

    # Display the message box with the button choices and store the selected button
    select_button = easygui.buttonbox(msg=MSG, title=title_output, choices=buttons)

    # If the user selects "Exit", display a message and break out of the loop
    if select_button == "Display":
        f_display_creature()
    elif select_button == "Add":
        output = f_add_creature()
        if output is False:
            easygui.msgbox("Cancelled")
    elif select_button == "Configure":
        f_configure_creature()
    elif select_button == "Delete":
        f_delete_creature()
    elif select_button == "Search":
        f_search_creature(searched_monster = easygui.enterbox("Type in creature that you want to search: "))
    else:
        easygui.msgbox("You Exit the program")
        exit()
