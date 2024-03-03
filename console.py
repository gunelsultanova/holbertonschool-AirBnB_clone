#!/usr/bin/python3


"""
console.py contains the entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the console."""
        return True

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D on Unix/Linux, Ctrl+Z on Windows)."""
        return True

    def do_help(self, arg):
        """Get help on commands.

        Usage:
            help [command]
        """
        if arg:
            super().do_help(arg)
        else:
            super().do_help(None)

    def emptyline(self):
        """Do nothing on an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
