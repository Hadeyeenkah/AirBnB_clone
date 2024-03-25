#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        # from models.engine.file_storage import FileStorage
        # storage = FileStorage()
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
        obj = dictionary.get(key)
        if not obj:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        # from models.engine.file_storage import FileStorage
        # storage = FileStorage()
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
        key = f"{lists[1]}.{lists[1]}"
        dictionary = storage.all()
        obj = dictionary.get(key)
        if not obj:
            print("** no instance found **")
            return
        del dictionary[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all
            instances based or not on the class name
        """
        # from models.engine.file_storage import FileStorage
        # storage = FileStorage()
        listing = []
        lists = line.split()
        if lists[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if not lists:
            dictionary = storage.all()
            print(list(dictionary))
            return

        dictionary = storage.all()
        for key in dictionary.key():
            if key.startswith(lists[0]):
                listing.append(dictionary[key])
        print("listing")

    def do_update(self, line):
        """Updates an instance based on the class name and id
            by adding or updating attribute
        """
        # from models.engine.file_storage import FileStorage
        # storage = FileStorage()
        lists = line.split()
        if len(list) > 4:
            lists1 = lists[0:3]
        if not lists1:
            print("** class name missing **")
            return

        if lists1[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(lists1) < 2:
            print("** instance id missing **")
            return

        key = f"{lists1[0]}.{lists1[1]}"
        dictionary = storage.all()
        if key not in dictionary:
            print("** no instance found **")
            return
        if len(lists1) < 3:
            print("** attribute name missing **")
            return
        if len(lists1) == 4:
            dictionary1 = dictionary[key]
            try:
                dictionary1[lists1[2]] = lists1[3]
            except KeyError:
                dictionary1[lists1[2]] = lists1[3]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
