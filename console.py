#!/usr/bin/python3

import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        return True
    
    def emptyline(self) -> bool:
        return super().emptyline()
    
    def help_quit(self, arg):
        print("Quit command to exit the program")
    
    def do_EOF(self):
        print()
        return True
    
    def do_create(self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.valid_classes:
            print("** class does not exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)
    
    def do_show(self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds not in self.valid_classes:
            print("** class does not exist **")
        elif len(cmds) < 2:
            print('** instance id missing **')
        else:
            objs = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")



    def do_all(self, arg):
        cmds = shlex.split(arg)
        objs = storage.all()

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds not in self.valid_classes:
            print("** no instance found **")
        elif len(cmds) < 2:
            print('** instance id missing **')
        else:
            objs = storage.all()
            for key, value in objs.items():
                if key.split('.')[0] == cmds[0]:
                    val = str(value)
                    print(val)

    def do_destroy(self,arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds not in self.valid_classes:
            print("** no instance found **")
        elif len(cmds) < 2:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(cmds[0],  cmds[1])
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds not in self.valid_classes:
            print("** class does not exist **")
        elif len(cmds) < 2:
            print('** instance id missing **')
        else:
            objs = storage.all()
            key = "{}.{}".format(cmds[0],  cmds[1])
            if key in objs:
              print("** no instance found **")
            elif len(cmds) < 3:
                print("** attribute name missing **")
            elif len(cmds) < 4:
                print("** value missing **")
            else:
                obj = objs[key]
                name = cmds[2]
                value = cmds[3]

                try:
                    value = eval(value)
                except Exception:
                    pass
                setattr(obj, name, value)
                obj.save()

    
if __name__ == "__main__":
    HBNBCommand().cmdloop()