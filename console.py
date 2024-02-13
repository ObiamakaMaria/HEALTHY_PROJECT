#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.disease import Disease
from models.article import Article
from models.engine.storage import DBStorage

classes = {"Article": Article, "BaseModel": BaseModel, "Disease": Disease, "User": User}

class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
    
        """Create a new instance of a specified class"""
        new_instance = User(username="IyanuLoluwa Adigun", email="memmalino@gmail.com", password_hash="welcome")
        new_instance.save()
        print("hello")
    def do_bring(self, arg):
        print(models.storage.all())

if __name__ == "__main__":
    HBNBCommand().cmdloop()

