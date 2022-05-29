# Versatile Console

Simple (yet versatile) console created for fun\
Coded in Python 3.8

## Guide on creating commands
Want to make some commands? It takes a bit of work, but you'll manage.\
For this tutorial, we're gonna make a command that simply says `hello`

### Add command to commands.txt
First step is to add your command name to `commands.txt`, so our console can detect its a command\
Our command name is gonna be `hello`, so lets add that
```python
#rest of commands#
hello
```
That was pretty easy, lets move on!

### Add your command to help_text.txt
Second step is to add our command name to `help_text.txt`, so people can know your command exists\
Once again, our command name is `hello`, so lets add that
```python
///COMMANDS///
#rest of commands#
hello
///END OF COMMANDS///
```
Once again, this was really easy. Lets move on

### Create the code for your command
Now its time for the big action, the actual command!\
Open up `commands.py`, as thats where all the command code is\
In this tutorial, all our command will do is say `hello`, but you can do any command or anything you want, the possibilites are endless!
```python
def command_hello():
  return "hello"
```
Since our command was really simple, it took no effort to make. But your command could be anything, and take any amount of time to create\
Alright, onto the last step

### Add command to console checking
We're finally here! All we have to do is add the command to our console check to allow users to use it\
Open `console.py`, as thats where the console code is\
This command is the simplest you can get, so its not that hard to code\
Find the line `def exec_commands(command_name, command):`, and scroll down to the last `print("")` line\
Just before that line, we'll put in our checking code
```py
elif command_name == "hello":
        print(commands.command_hello(command))
```
And voila! You have a new command!

### Testing the command
Try it out! Run `console.py`, and try running the command you made.
```python
: hello

hello

: 
```
