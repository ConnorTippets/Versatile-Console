from debug import debug, debug_log
x = debug_log.append("[Commands] Initializing...") if debug else None
def command_getparams(command_name, src):
    x = debug_log.append('[Commands] Getting params from input of "src"'.replace("src", src)) if debug else None
    src_fixed = src[len(command_name)+1:]
    src_fixed = src_fixed.split(" ")
    conjoined1 = []
    conjoined2 = []
    for idx, param in enumerate(src_fixed):
        if param.startswith('"'):
            for idxx in range(idx+1, len(src_fixed)):
                conjoined = [param+" "]
                if src_fixed[idxx].endswith('"'):
                    conjoined[0] = conjoined[0]+src_fixed[idxx]
                    conjoined1.append(conjoined)
                    break
                else:
                    conjoined[0] = conjoined[0]+src_fixed[idxx]+" "
    for idx, param in enumerate(src_fixed):
        if param.startswith("'"):
            for idxx in range(idx+1, len(src_fixed)):
                conjoined = [param+" "]
                if src_fixed[idxx].endswith("'"):
                    conjoined[0] = conjoined[0]+src_fixed[idxx]
                    conjoined2.append(conjoined)
                    break
                else:
                    conjoined[0] = conjoined[0]+src_fixed[idxx]+" "
    x = debug_log.append("[Commands] Found params and strings, returning to command execution") if debug else None
    return src_fixed, conjoined1, conjoined2

def command_help():
    help_txt = open("help_text.txt", "r")
    commands = help_txt.read()
    help_txt.close()
    return commands
def command_echo(src):
    params = command_getparams("echo", src)[0]
    return " ".join(params)
def command_exec(src):
    params = command_getparams("exec", src)[0]
    return " ".join(params)
def command_iddqd():
    return "Degreelessness Mode on"
