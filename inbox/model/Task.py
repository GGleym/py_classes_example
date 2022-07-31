from common.id.generator import generateID

ID = str


class Task:
    __id: ID
    __title: str

    def __init__(self, title: str):
        self.__id = ID(generateID())
        self.__title = title

    def id(self) -> ID:
        return self.__id

    def title(self) -> str:
        return self.__title
