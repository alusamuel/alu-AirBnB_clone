#!/usr/bin/python3
"""Command-line interface for AirBNB clone"""

import cmd
import readline
import rlcompleter
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Enable tab completion
readline.parse_and_bind("tab: complete")

# Command history file
HISTORY_FILE = ".cmd_history"

try:
    # Load history if available
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    pass


def inform_user_given_one_arg(arg):
    """Print error based on one argument"""
    if arg == "":
        print("** class name missing **")
    elif arg not in [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    ]:
        print("** class doesn't exist **")
    else:
        print("** instance id missing **")


def inform_user_given_two_arg(class_name):
    """Print error based on two arguments"""
    if class_name not in [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    ]:
        print("** class doesn't exist **")
    else:
        print("** no instance found **")


class HBNBCommand(cmd.Cmd):
    """Command-line tool for managing AirBNB objects"""
    prompt = "(hbnb) "
    classes = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    ]

    def do_quit(self, arg):
        """Exit the program"""
        print("Have a Good Day!")
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit"""
        return True

    def emptyline(self):
        """Ignore empty input"""
        return False

    def do_create(self, arg):
        """Create a new object"""
        set_instance = {
            "BaseModel": BaseModel(),
            "User": User(),
            "State": State(),
            "City": City(),
            "Amenity": Amenity(),
            "Place": Place(),
            "Review": Review(),
        }
        if arg in set_instance:
            instance = set_instance[arg]
            instance.save()
            print(instance.id)
        else:
            print("** class name missing **" if arg ==
                  "" else "** class doesn't exist **")

    def do_show(self, arg):
        """Show object by class and ID"""
        try:
            class_name, id = arg.split()
            all_objs = storage.all()
            key = f"{class_name}.{id}"
            if key in all_objs:
                print(all_objs[key])
            else:
                inform_user_given_two_arg(class_name)
        except ValueError:
            inform_user_given_one_arg(arg)

    def do_destroy(self, arg):
        """Delete object by class and ID"""
        try:
            class_name, id = arg.split()
            all_objs = storage.all()
            key = f"{class_name}.{id}"
            if key in all_objs:
                storage.delete(key)
            else:
                inform_user_given_two_arg(class_name)
        except ValueError:
            inform_user_given_one_arg(arg)

    def do_all(self, arg):
        """Show all objects or by class"""
        if arg in self.classes or arg == "":
            all_objs = storage.all()
            print([
                str(obj) for key, obj in all_objs.items()
                if arg == "" or key.startswith(arg)
            ])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update object attributes"""
        try:
            class_name, id, attr_name, attr_value = arg.split()
            all_objs = storage.all()
            key = f"{class_name}.{id}"
            if class_name in self.classes and key in all_objs:
                instance = all_objs[key]
                setattr(instance, attr_name, attr_value)
                instance.save()
            elif class_name in self.classes:
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except ValueError:
            args = arg.split()
            if not args:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")


if __name__ == "__main__":
    """Start command loop"""
    HBNBCommand().cmdloop()
    readline.write_history_file(HISTORY_FILE)
