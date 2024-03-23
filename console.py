#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class definition of the entry point of thr command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Default exist of the command interpreter
        """
        return True

    def emptyline(self):
        """Overwritting the emptyline method to fail executing the previous
            command if emptylin + ENTER
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
