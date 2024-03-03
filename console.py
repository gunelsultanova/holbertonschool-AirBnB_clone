#!/usr/bin/python3

"""
console.py contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel


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

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id.

        Usage:
            create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.

        Usage:
            show BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        obj_dict = storage.all()

        key = "{}.{}".format(class_name, obj_id)
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
