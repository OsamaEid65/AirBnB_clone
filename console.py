#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage
from models.city import City
from models.amenity import Amenity


def searcher(arg):
    pass


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    all_the_classes = {
            "BaseModel", "User", "Review", "State", "Place", "City", "Amenity"}

    def the_Base_interpreter(self, arg):

        commands_dict = {
                "show": self.do_show(),
                "all": self.do_all(), "destroy": self.do_destroy()}

    def do_creat(self, line):

        """creat class"""
        result = searcher(arg)

        if len(result) == 0:
            print("** class name missing **")
        elif result[0] not in HBNBCommand.all_the_classes:
            print("** class doesn't exist **")
        else:
            print(eval(result[0])().id)
            FileStorage.save()

    def do_quit(self, arg):

        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):

        """Eixt """
        return True

    def emptyline(self):

        """when there is empty line do nothing"""
        pass

    def do_show(self, arg):

        result = searcher(arg)
        objects = FileStorage.all()
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
        objects = FileStorage.all()
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
            FileStorage.save()

    def do_all(self, arg):

        """show string representations """
        result = searcher(arg)
        if len(result) > 0 and result[0] not in HBNBCommand.all_the_classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for objec in FileStorage.all().values():
                if len(result) > 0 and result[0] == objec.__class__.__name__:
                    object_list.append(objec.__str__())
                elif len(result) == 0:
                    object_list.append(objec.__str__())
            print(object_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
