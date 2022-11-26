#!/usr/bin/python3
"""Module contaning the AirBnB console program"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """
        End of file input to exit handler
        """
        return True

    def do_quit(self, line):
        """
        quit command to exit handler
        """
        return True

    def emptyline(self):
        """
        empty line input handler
        """
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
