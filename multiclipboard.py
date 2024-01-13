import sys
import clipboard
import json # to store the clipboard

# clipboard.copy("abc") # Copy from clipboard
# data = clipboard.paste() # store whatever is copied into data


# pass command line args using sys module
print(sys.argv) # argv gives the cmd line args

if len(sys.argv) == 2:
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
