import commands

def exec_commands(command_name, command):
    if not command_name == "exec":
        print("")
    if command_name == "help":
        print(commands.command_help())
    elif command_name == "echo":
        print(commands.command_echo(command))
    elif command_name == "exec":
        command = commands.command_exec(command)
        command_name = command.split(" ")[0]
        return exec_commands(command_name, command)
    elif command_name == "iddqd":
        print(commands.command_iddqd())
    print("")

def console(command_list):
    command = input(": ")
    command_name = command.split(" ")[0]
    if command_name in command_list:
        exec_commands(command_name, command)
        return console(command_list)
    else:
        print("Syntax Error: Not a command")
        return console(command_list)

print("Versatile Console 1.0 Initialized")
print("Type help for a list of commands")
commands_file = open("commands.txt", "r")
command_list = commands_file.read().split("\n")
commands_file.close()
console(command_list)
