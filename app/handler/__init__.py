from typing import Dict, List

from app.core.config import DEBUG
from app.schema import QueryType


class BaseExecutor:
    async def __run__(self, query_type: QueryType, rest_arguments: List[str]):
        executor = self.__getattribute__(query_type.lower())
        if executor:
            output = await executor(rest_arguments)
            print(output)
            return
        raise Exception("Invalid Executor")


class Handler:
    executor: Dict[QueryType, BaseExecutor] = {}

    @staticmethod
    def __arguments__():
        inline_input = str(input())
        return inline_input.split(" ")

    @staticmethod
    def _load_input(filepath: str):
        with open(filepath, "r") as file:
            yield file.readline()

    async def set_executor(self, query_type: QueryType, executor: BaseExecutor):
        self.executor[query_type] = executor

    async def run_executor(self, query_type: QueryType, rest_arguments: List[str]):
        _exec_ = self.executor.get(query_type)
        if _exec_:
            await _exec_.__run__(query_type=query_type, rest_arguments=rest_arguments)

    async def run(self, input_filepath: str = None):

        arguments = Handler.__arguments__()
        query_type: QueryType = QueryType(arguments[0])
        rest_arguments = arguments[1:]
        await self.run_executor(query_type=query_type, rest_arguments=rest_arguments)
