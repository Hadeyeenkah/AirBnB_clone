#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel

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

    def do_create(self, line):
        """create command for creating instances
        """
        if not line:
            print("** class name missing **")
            return

        class_name = line.split()[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        instance = BaseModel()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """command that Prints the string representation of an
            instance based on the class name and id
        """
        lists = args.split()
        if not args:
            print("** class name missing **")
            return

        if lists[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(lists) < 2:
            print("** instance id missing **")
            return

        key = f"{lists[0]}.{lists[1]}"
        dictionary = storage.all()
        if key not in dictionary:
            print("** no instance found **")
            return
        obj = dictionary.get(key)
        print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        lists = line.split()
        if not lists:
            print("** class name missing **")
            return
        if lists[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(lists) < 2:
            print("** instance id missing **")
            return
        key = f"{lists[0]}.{lists[1]}"
        dictionary = storage.all()
        # obj = dictionary.get(key)
        if key not in dictionary:
            print("** no instance found **")
            return
        del dictionary[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all
            instances based or not on the class name
        """
        listing = []
        lists = line.split()
        if lists[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if not lists:
            dictionary = storage.all()
            for key in dictionary.values():
                listing.append(str(key.__dict__))
            print(listing)
            return

        if lists:
            dictionary = storage.all()
            for value in dictionary.values():
                listing.append(value.__str__())
            print(listing)
            return

    def do_update(self, line):
        """Updates an instance based on the class name and id
            by adding or updating attribute
        """
        lists = line.split()
        lists1 = []
        if not lists:
            print("** class name missing **")
            return

        if lists[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(lists) < 2:
            print("** instance id missing **")
            return

        key = f"{lists[0]}.{lists[1]}"
        dictionary = storage.all()
        if key not in dictionary:
            print("** no instance found **")
            return
        for key_keys in dictionary.keys():
            if key_keys == key:
                if len(lists) < 3:
                    print("** attribute name missing **")
                    return
                if len(lists) < 4:
                    print("** value missing **")
                    return
                if len(lists) > 4 or len(lists) == 4:
                    lists1 = lists[0:4]
                    dict_value = dictionary[key]
                    dict_value.__dict__[lists[2]] = lists[3]
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
