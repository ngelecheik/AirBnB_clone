#!/usr/bin/python3
"""This module is the entry point of the program"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the entry point of the program"""
    prompt = '(hbnb)'

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
