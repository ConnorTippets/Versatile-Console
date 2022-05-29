import commands

def console(command_list):
    command = input(": ")
    command_name = command.split(" ")[0]
    if command_name in command_list:
        if command_name == "help":
            print("\n"+commands.command_help()+"\n")
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
