from typing import List
from typing import Dict

from common.error.error import Error
from view.menu.item import Item


class ErrMenuItemNotFound(Error):
    pass


class Menu:
    __items: List[Item]
    # Mapping from itemID to id in array.
    __itemIndex: Dict[int, int]

    def __init__(self, items: List[Item]):
        self.__items = list()
        self.__itemIndex = dict()
        for item in items:
            self.__items.append(item)
            self.__itemIndex[item.id()] = len(self.__items) - 1

    def startLoop(self):
        while True:
            self.startOnce()

    def startOnce(self):
        self.__printMenu()
        self.__items[self.__readItemIDFromStdIn()].func()()

    def __printMenu(self):
        for item in self.__items:
            print("{0}:\t{1}\n".format(item.id(), item.title()))

    def __readItemIDFromStdIn(self) -> int:
        while True:
            try:
                number = int(input(), 10)
                if number not in self.__itemIndex:
                    raise ErrMenuItemNotFound(
                        "menu item {0} not found".format(number)
                    )

                return self.__itemIndex[number]
            except ValueError:
                print("it is not a number")
            except ErrMenuItemNotFound:
                print("menu number with this number not found")
