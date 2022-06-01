from debug import debug, debug_log
import sys
x = debug_log.append("[VersatileConsole] Initializing...") if debug else None
x = debug_log.append("[Python] Imported command functions") if debug else None
import commands
import atexit
x = debug_log.append("[Python] Imported script termination functions") if debug else None
import tkinter as tk
x = debug_log.append("[Python] Imported GUI functions") if debug else None
import keyboard
x = debug_log.append("[Python] Imported Textbox clearance functions") if debug else None

def giveInput(event):
    inp = textbox.get(1.0, "end-1c")
    print(inp)
    console(command_list, inp)

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

root = tk.Tk()
root.title("Console")
root.geometry("720x720")
textbox = tk.Text(root, height = 1, width = 720)
textbox.pack(side="bottom")
outputLabel = tk.Label(root, text="")
outputLabel.pack(side="bottom")
def exec_commands(command_name, command):
    x = debug_log.append("[VersatileConsole] Executing commands") if debug else None
    output = ""
    if command_name == "help":
        output = commands.command_help()
    elif command_name == "echo":
        output = commands.command_echo(command)
    elif command_name == "exec":
        command = commands.command_exec(command)
        command_name = command.split(" ")[0]
        return exec_commands(command_name, command)
    elif command_name == "iddqd":
        output = commands.command_iddqd()
    elif command_name == "end":
        root.destroy()
        sys.exit()
    elif command_name == "cls" or "clear":
        outputLabel.config(text="")
    x = debug_log.append("[VersatileConsole] Execution of commands completed") if debug else None
    return output

def console(command_list, command):
    command_name = command.split(" ")[0]
    command_name = command_name.lower()
    command_name = command_name.split("\n")[0]
    x = debug_log.append('[VersatileConsole] Got input of "cmd"'.replace("cmd", command)) if debug else None
    if command_name in command_list:
        out = exec_commands(command_name, command)
        if out:
            outputLabel.config(text=outputLabel.cget("text")+out+"\n")
            keyboard.press_and_release('ctrl+a,backspace')
        else:
            outputLabel.config(text=outputLabel.cget("text")+out)
            keyboard.press_and_release('ctrl+a,backspace')
    else:
        if command_name[1:] in command_list:
            out = exec_commands(command_name[1:], command)
            if out:
                outputLabel.config(text=outputLabel.cget("text")+out+"\n")
                keyboard.press_and_release('ctrl+a,backspace')
            else:
                outputLabel.config(text=outputLabel.cget("text")+out)
                keyboard.press_and_release('ctrl+a,backspace')
        else:
            x = debug_log.append('[ERROR] "cmd_name" not a command. Restarting.'.replace("cmd_name", command_name.upper())) if debug else None
            outputLabel.config(text=outputLabel.cget("text")+"Syntax Error: Not a command"+"\n")
            keyboard.press_and_release('ctrl+a,backspace')

root.bind('<Return>', giveInput)
root.mainloop()
