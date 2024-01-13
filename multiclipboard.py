import sys
import clipboard
import json 



SAVE_FILE = "mcb.json"

# Save to json file
def saveItems(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

# Delete Item from json file
def delItem(filename, keyItem):
    with open(filename, "r") as f:
        data = json.load(f)
        del data[keyItem]
    with open(filename, "w") as fp:
        json.dump(data, fp)



# read json file
def loadJson(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}



if len(sys.argv) == 2: # Get system args
    cmd = sys.argv[1] 
    data = loadJson(SAVE_FILE)

    # Save item to clipboard
    if cmd == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        saveItems(SAVE_FILE, data)

    # load item from clipboard
    elif cmd == "load":
        key = input("Enter key of item you want to load: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data successfuly copied to clipboard!")
        else:
            print("Key does not exist.")

    # Display clipboard
    elif cmd == "list":
        print("Items currently on the clipboard\n")
        print("Key -> Value\n")
        print("----------------\n")
        for i in data.keys():
            print(f"{i} -> {data[i]}\n")

    # Delete item from clipboard
    elif cmd == "del":
        keyItem = input("Enter the key of the object you want to delete: ")
        delItem(SAVE_FILE, keyItem)
        print("Successfuly deleted item")

    else:
        print("Unknown command. Please enter 1 of - save | load | list | del")

else:
    print("Enter a command - save | load | list | del")
