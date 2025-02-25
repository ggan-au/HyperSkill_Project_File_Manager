import os, sys

os.chdir('module/root_folder')

while (command := input("Input the command: ")) != "quit":
    valid_commands = {"pwd", "quit"}
    is_relative = command.startswith("cd ") and len(command) > 3 and command[3] not in {".", "\\", "/"}
    is_command = (command in valid_commands) or (command.startswith("cd ") and len(command) > 3)

    if is_command:
        try:
            if command == "pwd":
                print(os.getcwd())
            elif command == "cd ..":
                os.chdir("..")
                print(os.getcwd())
            elif is_relative:
                os.chdir(command[3:])
                print(os.getcwd())
        except FileNotFoundError:
            print("The directory was not found. Try again")
    else:
        print("Invalid Command")
