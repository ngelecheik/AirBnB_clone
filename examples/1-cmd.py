#!/usr/bin/python3
import cmd 

class HelloWorld(cmd.Cmd):
    '''simple commad processo example'''

    def do_greet(self, line):
        print("hello")

    def do_EOF(self, line):
        return True
if __name__=="__main__":
    HelloWorld().cmdloop()
