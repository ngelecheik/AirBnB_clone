#!/usr/bin/python3
"""This module is the entry point of the program"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import storage
import json


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
        if line in globals():
            my_model = globals()[line]()
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
        if args[0] in globals():
            if len(args) == 2:
                key = f"{args[0]}.{args[1]}"
            else:
                print("** instance id missing **")
                return
            if key in all_objs:
                my_object_s = globals()[args[0]](**all_objs[key])
                print(str(my_object_s))
            else:
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")
            return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and
         id (save the change into the JSON file).
          Ex: $ destroy BaseModel 1234-1234-1234."""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        all_objs = storage.all()
        if args[0] in globals():
            if len(args) == 2:
                key = f"{args[0]}.{args[1]}"
            else:
                print("** instance id missing **")
                return
            if key in all_objs:
                del all_objs[key]
                objects_json = json.dumps(all_objs)
                with open('file.json', 'w', encoding='utf-8') as f:
                    f.write(objects_json)
            else:
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")
            return

    def do_all(self, line):
        """Prints all string representation of
         all instances based or not on
          the class name. Ex: $ all BaseModel or $ all"""

        all_objs = storage.all()
        if line in globals():
            all_list = []
            for value in all_objs.values():
                new = globals()[line](**value)
                all_list.append(str(new))
            print(all_list)
        elif not line:
            all_list = []
            for value in all_objs.values():
                class_name = value['__class__']
                new = globals()[class_name](**value)
                all_list.append(str(new))
            print(all_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the
         class name and id by adding or updating
          attribute (save the change into the JSON file)"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        all_objs = storage.all()
        if args[0] in globals():
            if len(args) >= 2:
                key = f"{args[0]}.{args[1]}"
            else:
                print("** instance id missing **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return

            if len(args) < 4:
                print("** value missing **")
                return
            if key in all_objs:
                # get the object that I will change
                changing_object = all_objs[key]
                class_name = changing_object['__class__']
                # reomve the present one
                del all_objs[key]
                # bring life to the object from dict
                my_object = globals()[class_name](**changing_object)
                # set the third attribute with 4 value
                value = args[3]
                value = value.strip('"')
                setattr(my_object, args[2], value)
                # return the object to dictionary
                my_object_dict = my_object.to_dict()
                # add it to the retrived dictionary
                all_objs[key] = my_object_dict
                # update the json
                objects_json = json.dumps(all_objs)
                with open('file.json', 'w', encoding='utf-8') as f:
                    f.write(objects_json)
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
