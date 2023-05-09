"""Allow user to type in Monster name in the search box; allow user to type in 
new values for each fields and display it with easy,gui """

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
searched_card = easygui.enterbox("Enter the name of the creature you want to edit: ")

# Check if the entered creature name exists in the dictionary
if searched_card in creatures:
    # If the creature exists, allow the user to edit its stats
    creature_stats = creatures[searched_card]
    updated_stats = {}
    for stat in creature_stats:
        new_value = easygui.enterbox(f"Enter new value for {stat} (current value: {creature_stats[stat]}): ")
        if new_value is not None:
            updated_stats[stat] = int(new_value)
        else:
            updated_stats[stat] = creature_stats[stat]
    creatures[searched_card] = updated_stats
    new_msg = ""
    title = f"{searched_card}\n"
    for search_name, new_stats in updated_stats.items():
        new_msg += f"\n{search_name} : {new_stats}"
    easygui.msgbox(title=title, msg=new_msg)
else:
    # If the creature does not exist, display an error message
    easygui.msgbox(f"{searched_card} not found in the dictionary.")

#  easygui.msgbox(f"{searched_card} has been updated: {creatures[searched_card]}")