import sys

from inbox.model.TaskList import TaskList
from view.menu.item import Item
from view.menu.menu import Menu


class App:
    __menu: Menu
    __taskList: TaskList

    def __init__(self):
        self.__menu = Menu([
            Item(menuID=0, title="exit", func=lambda: sys.exit(0)),
            Item(menuID=1, title="add task",
                 func=self.__addTask),
            Item(menuID=2, title="Print tasks",
                 func=self.__printLastTasks)
        ])
        self.__taskList = TaskList()

    def start(self):
        self.__menu.startLoop()

    def __addTask(self):
        title = str(input())
        task_id = self.__taskList.addTask(title)
        print("task saved with ID {0}\n\n".format(task_id))

    def __printLastTasks(self):
        print("How many tasks must be writen?\n")
        n = int(input())
        tasks = self.__taskList.getLastNTasks(n)
        for task in tasks:
            print("{0}: {1}\n".format(task.id(), task.title()))
