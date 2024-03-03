#!/usr/bin/python3

"""
console.py contains the entry point of the command interpreter
"""

import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]  # Add other valid class names here

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to the JSON file, and prints the id.
        
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id.
        
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = BaseModel.load()
        key = class_name + "." + instance_id
        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
        
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = BaseModel.load()
        key = class_name + "." + instance_id
        if key in all_instances:
            del all_instances[key]
            BaseModel.save(all_instances)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name.
        
        Usage: all [class name]
        """
        args = arg.split()
        all_instances = BaseModel.load()
        if not args:
            print([str(instance) for instance in all_instances.values()])
        else:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            filtered_instances = [str(instance) for instance in all_instances.values() if instance.__class__.__name__ == class_name]
            print(filtered_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute.
        
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = BaseModel.load()
        key = class_name + "." + instance_id
        if key not in all_instances:
            print("** no instance found **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 5:
            print("** value missing **")
            return
        attribute_value = args[3]
        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value[1:-1]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        instance = all_instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

