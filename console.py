#!/usr/bin/python3

"""
console.py contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    console.py contains the entry point of the command interpreter
    """
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

        if class_name not in [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]:
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


        className = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}
        import shlex

        args = shlex.split(arg)
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            del models.storage._FileStorage__objects[args[0]+'.'+args[1]]
            models.storage.save()


        

        """
        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]:
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
        """

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.

        Usage:
            destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        obj_dict = storage.all()

        key = "{}.{}".format(class_name, obj_id)
        if key not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict[key]
            storage.save()
            storage.reload()

    def do_update(self, arg):
        """Updates an instance based on the class name and id.

        Usage:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_id = arg_list[1]
        obj_dict = storage.all()

        key = "{}.{}".format(class_name, obj_id)
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attribute_name = arg_list[2]
        attribute_value = arg_list[3]

        obj = obj_dict[key]

        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_all(self, arg):
        """Prints all string representations of all instances.

        Usage:
            all BaseModel or all
        """
        obj_dict = storage.all()
        if not arg:
            print([str(obj_dict[key]) for key in obj_dict])
            return

        arg_list = arg.split()
        class_name = arg_list[0]

        if class_name not in [
                "BaseModel",
                "User",
                "Place",
                "State",
                "City",
                "Amenity",
                "Review"
                ]:
            print("** class doesn't exist **")
            return

        print([str(obj_dict[key]) for key in obj_dict if class_name in key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
