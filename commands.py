"""
    Command Pattern Example

    Author: Leandro Beretta <lea.beretta@gmail.com>
"""

import os


class Command:

    def execute(self):
        pass

    def undo(self):
        pass


class ListDirCommand(Command):

    def execute(self):
        elements = os.listdir('.')

        for element in elements:
            print(element)

    def undo(self):
        pass


class CreateFileCommand(Command):

    def __init__(self, name):
        self.name = name

    def execute(self):
        open(self.name, 'w')

    def undo(self):
        os.remove(self.name)


class MoveFileCommand(Command):

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def execute(self):
        os.rename(self.src, self.dst)

    def undo(self):
        os.rename(self.dst, self.src)


class Invoker:

    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.execute()

    def undo(self):
        self.command.undo()


if __name__ == '__main__':
    list_dir_command = ListDirCommand()
    create_file_command = CreateFileCommand('file_a')
    move_file_command = MoveFileCommand('file_a', 'file_b')

    list_dir_invoker = Invoker(list_dir_command)
    create_file_invoker = Invoker(create_file_command)
    move_file_invoker = Invoker(move_file_command)

    list_dir_invoker.execute()

    create_file_invoker.execute()

    move_file_invoker.execute()
    move_file_invoker.undo()

    create_file_invoker.undo()

    list_dir_invoker.execute()
