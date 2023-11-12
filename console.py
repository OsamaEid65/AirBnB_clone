#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_creat(self,line):
        print("i have created ",line)

    def do_quit(self,arg):
        """Quit command to exit the program"""
        return True
    def do_EOF(self,line):
        """Eixt """
        return True
    def precmd(self,line):
        return cmd.Cmd.precmd(self,line)

if __name__=='__main__':
    HBNBCommand().cmdloop()
