import os
import manager_utils

os.chdir('module/root_folder')

def main():
    while True:
        user_input = input()
        input_list = user_input.split(" ")
        print(input_list)

        if user_input == "quit":
            break;

        if manager_utils.is_command(input_list[0]):
            try:
                if input_list[0] == "pwd":
                    manager_utils.command_pwd()
                elif input_list[0] == "cd":
                    manager_utils.command_cd(*input_list)
                elif input_list[0] == "ls":
                    manager_utils.command_ls(*input_list)
                elif input_list[0] == "rm":
                    manager_utils.command_rm(*input_list)
                elif input_list[0] == "mv":
                    manager_utils.command_mv(*input_list)
                elif input_list[0] == "mkdir":
                    manager_utils.command_mkdir(*input_list)
            except FileNotFoundError:
                print("The directory was not found. Try again")
        else:
            print("Invalid Commands")

main()
