import os, shutil

valid_commands = {"pwd",
                  "quit",
                  "cd",
                  "ls",
                  "rm",
                  "mv",
                  "mkdir",
                  "cp"}

rel_paths = {
                 "..",
}

def add_trailing_slash(path):
    if path in rel_paths:
        return path + '/'
    return path

def sort_files(files):
    return sorted(files, key=lambda f: ("." in f, f))

def is_command(command):
    is_valid_cmd = (command in valid_commands) or (command.startswith("cd ") and len(command) > 3)
    return is_valid_cmd

def command_pwd():
    print(os.getcwd())

def command_mkdir(*args):
    num_args = len(args)
    if num_args < 2:
        print("Specify the name of the directory to be made")
        return
    path = args[1]
    try:
        os.mkdir(path)
    except FileExistsError:
        print("The directory already exists")

def command_cd(*command):
    num_args = len(command)
    if num_args == 1:
        print("Incorrect number of arguments")
    elif num_args == 2 and command[1] == "..":
        os.chdir("..")
        print(os.getcwd())
    else:
        os.chdir(command[1])
        print(os.getcwd())

def command_rm(*args):
    num_args = len(args)
    if num_args < 2:
        print("Specify the file or directory")
        return

    path = args[1]

    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        print("No such file or directory")

def command_cp(*args):
    num_args = len(args)

    if num_args < 3:
        print("Specify the file")
        return

    if num_args > 3:
        print("Specify the current name of the file or directory and the new location and/or name")
        return

    src = args[1]
    dst = args[2]

    if os.path.exists(dst) and dst not in rel_paths:
        print(f"{src} already exists in this directory")
    elif os.path.exists(src):
        src = add_trailing_slash(src)
        dst = add_trailing_slash(dst)
        shutil.copy(src, dst)
    else:
        print("No such file or directory")

def command_mv(*args):
    num_args = len(args)

    if num_args != 3:
        print("Specify the current name of the file or directory and the new location and/or name")
        return

    src = args[1]
    dst = args[2]

    src = add_trailing_slash(src)
    dst = add_trailing_slash(dst)

    if os.path.exists(dst) and not os.path.isdir(dst):
        print("The file or directory already exists")
    elif os.path.exists(src):
        shutil.move(src, dst)
    else:
        print("No such file or directory")



def command_ls(*args):
    num_args = len(args)
    ls_file_list = os.listdir()
    ls_sorted_files = sort_files(ls_file_list)

    if num_args == 1:
        for ls_file in ls_sorted_files:
            print(ls_file)

    if num_args == 2:
        if args[1] == "-l":
            for ls_file in ls_sorted_files:
                print(f"{ls_file} {os.stat(ls_file).st_size}")
        elif args[1] == "-lh":
            for ls_file in ls_sorted_files:
                if os.path.isdir(ls_file):
                    print(f"{ls_file}")
                else:
                    print(f"{ls_file} {file_size_convert(ls_file)}")
        else:
            print(f"Invalid argument for ls command: {args[1]}")


def file_size_convert(files):
    file_size = os.stat(files).st_size
    file_size_format = ""

    if file_size < 1024:
        file_size = file_size
        file_size_format = "B"
    elif file_size < 1024**2:
        file_size = int(file_size / 1024)
        file_size_format = "KB"
    elif file_size < 1024**3:
        file_size = int(file_size / (1024**2))
        file_size_format = "MB"
    elif file_size < 1024**4:
        file_size = int(file_size / (1024**3))
        file_size_format = "GB"

    return f"{file_size}{file_size_format}"