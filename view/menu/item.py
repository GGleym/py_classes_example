from typing import Callable

FuncMenu = Callable[[None], None]


class Item:
    __id: int
    __title: str
    __func: FuncMenu

    def __init__(self, menuID: int, title: str, func: FuncMenu):
        self.__id = menuID
        self.__title = title
        self.__func = func

    def id(self) -> int:
        return self.__id

    def title(self) -> str:
        return self.__title

    def func(self) -> FuncMenu:
        return self.__func
