from debug import debug, debug_log
import sys
x = debug_log.append("[VersatileConsole] Initializing...") if debug else None
x = debug_log.append("[Python] Imported command functions") if debug else None
import commands
import atexit
x = debug_log.append("[Python] Imported script termination functions") if debug else None

def exec_commands(command_name, command):
    x = debug_log.append("[VersatileConsole] Executing commands") if debug else None
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
    elif command_name == "end":
        sys.exit()
    print("")
    x = debug_log.append("[VersatileConsole] Execution of commands completed") if debug else None

def console(command_list):
    command = input(": ")
    command_name = command.split(" ")[0]
    command_name = command_name.lower()
    x = debug_log.append('[VersatileConsole] Got input of "cmd"'.replace("cmd", command)) if debug else None
    if command_name in command_list:
        exec_commands(command_name, command)
        return console(command_list)
    else:
        x = debug_log.append('[ERROR] "cmd_name" not a command. Restarting.'.replace("cmd_name", command_name.upper())) if debug else None
        print("Syntax Error: Not a command")
        return console(command_list)

def exit_handle():
    if debug:
        debug_log.append("[Python] Script Ending, calling script termination functions")
        with open("log.txt", "w") as log_file:
            log_file.write("\n".join(debug_log))

atexit.register(exit_handle)
commands_file = open("commands.txt", "r")
command_list = commands_file.read().split("\n")
commands_file.close()
x = debug_log.append("[VersatileConsole] Found list of commands") if debug else None
print("Versatile Console 1.1 Initialized")
print("Type help for a list of commands")
console(command_list)
