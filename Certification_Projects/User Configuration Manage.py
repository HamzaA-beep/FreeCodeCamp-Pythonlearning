#adds new settings to given dictionary
def add_setting(add_dict,add_tuple):
    key,value = add_tuple
    key = key.lower()
    value = value.lower()
    if key in add_dict.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    add_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

#modifys original settings of given dictionary
def update_setting(update_dict,update_tuple):
    key,value = update_tuple
    key = key.lower()
    value = value.lower()
    if key in update_dict.keys():
        update_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

#removes a setting from given dictionary
def delete_setting(delete_dict,delete_tuple):
    key = delete_tuple.lower()
    if key in delete_dict.keys():
        delete_dict.pop(key,None)
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

#allows viewing of given dictionary while capitalising the keys
def view_settings(view_dict):
    result = 'Current User Settings:\n'
    if not view_dict:
        return "No settings available."
    else:
        for key, value in view_dict.items():
            result += f"{key.capitalize()}: {value}\n"
        return result

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
print(view_settings(test_settings))
