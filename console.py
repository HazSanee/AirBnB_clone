#!/usr/bin/python3
"""Module contaning the AirBnB console program"""
import cmd
from datetime import datetime
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """
        End of file command to exit th program
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        an empty line + ENTER shouldn't execute anything
        cursor would be move to new line
        """
        pass

    def do_create(self, line):
        """
        create instance of a given model
        Ex: $ create BaseModel
        """
        classes = storage.classes()
        if line == '':
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            newModel = classes[line]()
            newModel.save()
            print(f"Instance of {line} created and saved")
        # print("line: ", line)

    def do_show(self, line):
        """
        print string representation of instance of a given model
        Ex: $ show BaseModel 1234-1234-1234
        """
        classes = storage.classes()
        if line == '':
            print("** class name missing **")
            return
        line = line.split()
        if line[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        key = '.'.join(line)
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """
        destroys instance of a given model
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        classes = storage.classes()
        if line == '':
            print("** class name missing **")
            return
        line = line.split()
        if line[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        key = '.'.join(line)
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """
        Prints string representation of all instances
        based or not on the class name
        Ex: $ all BaseModel
            or
            $ all
        """
        classes = storage.classes()
        words = line.split()
        if line == '':
            print([str(obj) for key, obj in storage.all().items()])
        elif words[0] not in classes:
            print("** class doesn't exist **")
        else:
            all_class = []
            for key, obj in storage.all().items():
                if key.startswith(words[0]):
                    all_class.append(str(obj))
            print(all_class)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        classes = storage.classes()
        if line == '':
            print("** class name missing **")
            return
        line = line.split()
        if line[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        elif len(line) == 2:
            print("** attribute name missing **")
            return
        elif len(line) == 3:
            print("** value missing **")
            return
        key = line[0] + '.' + line[1]
        attr_name = line[2]
        attr_val = ' '.join(line[3:])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if attr_name != 'created_at' and attr_name != 'updated_at':
            print("review text:", attr_val)
            setattr(objs[key], attr_name, attr_val)
            # setattr(objs[key], 'updated_at', datetime.now())
            objs[key].save()
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
