#!/usr/bin/python3
"""Module contains HBNB console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models import storage
from models.city import City
from models.amenity import Amenity
import re
from shlex import split


def searcher(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand that represents console"""

    prompt = "(hbnb) "
    all_the_classes = {
            "BaseModel", "User", "Review", "State", "Place", "City", "Amenity"}

    def the_Base_interpreter(self, arg):

        commands_dict = {
                "show": self.do_show(),
                "all": self.do_all(),
                "destroy": self.do_destroy(),
                "count": self.do_count(),
                "update": self.do_update()
                }
        check = re.search(r"\.", arg)
        if check is not None:
            temparg = [arg[:check.span()[0]], arg[check.span()[1]:]]
            check = re.search(r"\((.*?)\)", argtemp[1])
            if check is not None:
                comm = [argtemp[1][:check.span()[0]], check.group()[1:-1]]
                if comm[0] in commands_dict.keys():
                    call = "{} {}".format(argtemp[0], comm[1])
                    return commands_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, line):

        """create class"""
        result = searcher(line)

        if len(result) == 0:
            print("** class name missing **")
        elif result[0] not in HBNBCommand.all_the_classes:
            print("** class doesn't exist **")
        else:
            print(eval(result[0])().id)
            storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, line):
        """Exit"""

        print("")
        return True

    def emptyline(self):
        """when there is empty line do nothing"""

        pass

    def do_show(self, arg):

        result = searcher(arg)
        objects = storage.all()
        if len(result) == 0:
            print("** class name missing **")
        elif result[0] not in HBNBCommand.all_the_classes:
            print("** class doesn't exist **")
        elif len(result) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(result[0], result[1]) not in objects:
            print("** no instance found **")
        else:
            print(objects["{}.{}".format(result[0], result[1])])

    def do_destroy(self, arg):

        """destroy class"""
        result = searcher(arg)
        objects = storage.all()
        if len(result) == 0:
            print("** class name missing **")
        elif result[0] not in HBNBCommand.all_the_classes:
            print("** class doesn't exist **")
        elif len(result) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(result[0], result[1]) not in objects.keys():
            print("** no instance found **")
        else:
            del objects["{}.{}".format(result[0], result[1])]
            storage.save()

    def do_all(self, arg):

        """show string representations """
        result = searcher(arg)
        if len(result) > 0 and result[0] not in HBNBCommand.all_the_classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for objec in storage.all().values():
                if len(result) > 0 and result[0] == objec.__class__.__name__:
                    object_list.append(objec.__str__())
                elif len(result) == 0:
                    object_list.append(objec.__str__())
            print(object_list)

    def do_update(self, ar):
        """Updates Class"""

        argtemp = searcher(ar)
        obdict = storage.all()

        if len(argtemp) == 0:
            print("** class name missing **")
            return False
        if argtemp[0] not in HBNBCommand.all_the_classes:
            print("** class doesn't exist **")
            return False
        if len(argtemp) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argtemp[0], argtemp[1]) not in obdict.keys():
            print("** no instance found **")
            return False
        if len(argtemp) == 2:
            print("** attribute name missing **")
            return False
        if len(argtemp) == 3:
            try:
                type(eval(argtemp[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argtemp) == 4:
            ob = obdict["{}.{}".format(argtemp[0], argtemp[1])]
            if argtemp[2] in ob.__class__.__dict__.keys():
                valtype = type(ob.__class__.__dict__[argtemp[2]])
                ob.__dict__[argtemp[2]] = valtype(argtemp[3])
            else:
                ob.__dict__[argtemp[2]] = argtemp[3]
        elif type(eval(argtemp[2])) == dict:
            ob = obdict["{}.{}".format(argtemp[0], argtemp[1])]
            for k, v in eval(argtemp[2]).items():
                if (k in ob.__class__.__dict__.keys() and
                        type(ob.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(ob.__class__.__dict__[k])
                    ob.__dict__[k] = valtype(v)
                else:
                    ob.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
