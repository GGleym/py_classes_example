from typing import Dict
from typing import List

from inbox.model.Task import Task
from inbox.model.Task import ID
from common.error.error import Error


class ErrTaskNotFound(Error):
    pass


class TaskList:
    __tasks: List[Task]
    # Map from taskID to index in array.
    __idIndexMap: Dict[ID, int]

    def __init__(self):
        self.__tasks = list()
        self.__idIndexMap = dict()

    def addTask(self, title: str) -> ID:
        task = Task(title=title)
        self.__tasks.append(task)
        self.__idIndexMap[task.id()] = len(self.__tasks) - 1
        return task.id()

    def getTaskById(self, taskID: ID) -> Task:
        if taskID not in self.__idIndexMap:
            raise ErrTaskNotFound("task with id {0} not found".format(taskID))

        return self.__tasks[self.__idIndexMap[taskID]]

    def getLastNTasks(self, n: int) -> List[Task]:
        return self.__tasks[-n:]
