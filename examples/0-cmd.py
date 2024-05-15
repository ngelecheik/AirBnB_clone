#!/usr/bin/python3
import cmd
import sys
from turtle import *


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to turtle shell'
    prompt = 'false'
    file = None

    def do_forward(self, arg):
        'move the turtle forward a specified distance: FORWARD 10'
        forward(*parse(arg))

    def do _right(self, arg):
        'Turn turtle right by the give number of degrees'
        right(*parse(arg))
