#!/usr/bin/python3
"""Command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command iterpreter public class which inherites from base class cmd.
    """
    prompt = '(hbnb) '
    __cls = ["BaseModel", "User", "State", "City", "Amenity", "Place",
             "Review"]

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Ctrl+D command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Called when empty line + Enter. Override the default behaviour,
        execute the previous command, with just do nothing.
        """
        pass

    def do_create(self, line):
        """ Usage: create BaseModel
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif not args[0] in __class__.__cls:
            print("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                inst = BaseModel()
            elif args[0] == "User":
                inst = User()
            elif args[0] == "State":
                inst = State()
            elif args[0] == "City":
                inst = City()
            elif args[0] == "Amenity":
                inst = Amenity()
            elif args[0] == "Place":
                inst = Place()
            elif args[0] == "Review":
                inst = Review()
            print(inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id.
        """
        args = line.split(" ")
        if args[0] in __class__.__cls:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    if key == obj_id:
                        print(all_objs[obj_id])
                        break
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        elif args[0] == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        args = line.split(" ")
        if args[0] in __class__.__cls:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                objs_dict = storage.all()
                if objs_dict.pop(key, None) is None:
                    print("** no instance found **")
                else:
                    storage.save()
            else:
                print("** instance id missing **")
        elif args[0] == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name.
        """
        args = line.split(" ")
        if args[0] == "" or args[0] in __class__.__cls:
            str_obj = []
            all_objs = storage.all()
            for obj_key in all_objs.keys():
                if args == [''] or obj_key.split(".")[0] == args[0]:
                    str_obj.append(str(all_objs[obj_key]))
            print(str_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute.
        """
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif not args[0] in __class__.__cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs.keys():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
