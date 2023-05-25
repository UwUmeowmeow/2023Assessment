"""Allow user to type in Monster name in the search box; allow user to type in 
new values for each field and display it with easy,gui """
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

# Allow user to type in the search box
searched_monster = easygui.enterbox(
    "Enter the name of the creature you want to edit: ")

# Check if the entered creature name exists in the dictionary
if searched_monster in creatures:
    # If the creature exists, allow the user to edit its stats
    creature_stats = creatures[searched_monster]
    updated_stats = {}
    for stat in creature_stats:
        while True:
            new_value = easygui.enterbox(f"Enter new value for {stat} "
                                         f"(current value: '"
                                         f"'{creature_stats[stat]}): ")
            try:

                if new_value is not None and new_value != "":
                    int_new = int(new_value)
                else:
                    break
            except ValueError:
                # Display an error message if an invalid number is entered
                easygui.msgbox("Please enter a valid number"
                               " for the status fields")
            else:
                if int_new > 25 or int_new < 1:
                    # Display an error message
                    # if the number is not within the valid range
                    easygui.msgbox("Please enter a"
                                   " number between 1 and 25")

                else:
                    updated_stats[stat] = creature_stats[stat]
                    creatures[searched_monster] = updated_stats
                    break

    # Display the updated stats of the creature
    new_msg = ""
    title = f"{searched_monster}\n"
    for stat_name, stat_value in updated_stats.items():
        new_msg += f"\n{stat_name} : {stat_value}"
    easygui.msgbox(title=title, msg=new_msg)
else:
    # If the creature does not exist, display an error message
    easygui.msgbox(f"{searched_monster} not found in the dictionary.")
