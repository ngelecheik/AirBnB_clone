#!/usr/bin/python3
"""This module is the entry point of the program"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """the entry point of the program"""
    prompt = '(hbnb)'

    def do_create(self, line):
        """reates a new instance of BaseModel,
         saves it (to the JSON file) and prints the id.
         Ex: $ create BaseModel"""
        if not line:
            print("** class name missing **")
            return
        if line == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an
         instance basedon the class name and id.
          Ex: $ show BaseModel 1234-1234-1234"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        all_objs = storage.all()
        if args[0] == "BaseModel":
            if len(args) == 2:
                key = f"BaseModel.{args[1]}"
            else:
                print("** instance id missing ** ")
                return
            if key in all_objs:
                print(str(all_objs[key]))
            else:
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")
            return

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "Exit program"
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
