import sys
import clipboard
import json # to store the clipboard

# clipboard.copy("abc") # Copy from clipboard
# data = clipboard.paste() # store whatever is copied into data


# Save to json file
def saveItems(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)



# read json file
def loadJson(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        return data



if len(sys.argv) == 2: # Get system args
    cmd = sys.argv[1] 

    if cmd == "save":
        print("save")
    elif cmd == "load":
        print("load")
    elif cmd == "list":
        print("list")
    else:
        print("Unknown command. Please enter 1 of - save | load | list")

else:
    print("Enter a command - save | load | list")
