#!/usr/bin/python3
"""
Defines the HBNBCommand class
"""

import cmd
from signal import signal, SIGINT
from sys import exit
from models.base_model import BaseModel
import models
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    """
    prompt = "(hbnb)"
    allowed_classes = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
        ]

    def do_quit(self, *args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, *args):
        """Exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def handler(signal_received, frame):
        """Handle the SIGINT or CTRL-C signal"""
        print("^C")
        exit(0)

    def do_create(self, args):
        """
        Create a new instance of a class
        """
        #Check if a class name is supplied as the argument.
        if len(args) == 0:
            self.err_handler(1)
        else:
            args = args.split()
            if args[0] in self.allowed_classes:
                #Create a new instance of the class
                new_instance = eval(args[0])(args[1:])
                print(new_instance.id)
                new_instance.save()
            else:
                self.err_handler(2)

    def do_show(self, args):
        """
         Prints the string representation of an instance based on the class name
        and id
        """
        if len(args) == 0:
            self.err_handler(1)
        elif len(args) == 1:
            self.err_handler(3)
        else:
            args = args.split()
            if args[0] in self.allowed_classes:
                models.storage.reload()
                #Create an identifier based on user input.
                identifier = args[0] + "." + args[1]
                if identifier in list(models.storage.all().keys()):
                    print(models.storage.all()[identifier])
                else:
                    self.err_handler(4)
            else:
                self.err_handler(2)


    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        args = args.split()
        if len(args) == 0:
            self.err_handler(1)
        elif len(args) == 1:
            if args[0] in self.allowed_classes:
                self.err_handler(3)
            else:
                self.err_handler(2)
        else:
            if args[0] in self.allowed_classes:
                models.storage.reload()
                identifier = args[0] + "." + args[1]
                if identifier in list(models.storage.all().keys()):
                    del models.storage.all()[identifier]
                    models.storage.save()
                else:
                    self.err_handler(4)
            else:
                self.err_handler(2)


    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        str_list = []
        #If length is zero, print all instances.
        if len(args) == 0:
            all_dict = models.storage.all()
            for id in all_dict.keys():
                obj = all_dict[id]
                str_list.append(str(obj))
            print(str_list)
        else:
            models.storage.reload()
            args = args.split()
            if args[0] in self.allowed_classes:
                all_dict = models.storage.all()
                for id in all_dict.keys():
                    if args[0] in id:
                        obj = all_dict[id]
                        str_list.append(str(obj))
                print(str_list)
            else:
                self.err_handler(2)


    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = shlex.split(args)
        if len(args) == 0:
            self.err_handler(1)
        elif len(args) == 1:
            if args[0] in self.allowed_classes:
                self.err_handler(3)
            else:
                self.err_handler(2)
        else:
            if args[0] in self.allowed_classes:
                models.storage.reload()
                identifier = args[0] + "." + args[1]
                if identifier in list(models.storage.all().keys()):
                    if len(args) == 2:
                        self.err_handler(5)
                    elif len(args) == 3:
                        self.err_handler(6)
                    else:
                        attr = args[2]
                        value = args[3]
                        setattr(models.storage.all()[identifier],attr, value)
                        models.storage.all()[identifier].save()
                else:
                    self.err_handler(4)
            else:
                self.err_handler(2)





    def err_handler(self, error_num):
        """Handles errors in the progrm"""
        if error_num == 1:
            print("** class name missing **")
        elif error_num == 2:
            print("** class doesn't exist **")
        elif error_num == 3:
            print("** instance id missing **")
        elif error_num == 4:
            print("** no instance found **")
        elif error_num == 5:
            print("** attribute name missing **")
        elif error_num == 6:
            print("** value missing **")
if __name__ == "__main__":
    signal(SIGINT, HBNBCommand.handler)
    HBNBCommand().cmdloop()
