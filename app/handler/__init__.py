from typing import Dict, List

from app.exceptions.exc import BankingException
from app.schema import QueryType


class BaseExecutor:
    async def __run__(self, query_type: QueryType, rest_arguments: List[str]):
        executor = self.__getattribute__(query_type.lower())
        if executor:
            output = await executor(rest_arguments)
            return output
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
            for f in file:
                yield f

    async def set_executor(self, query_type: QueryType, executor: BaseExecutor):
        self.executor[query_type] = executor

    async def run_executor(self, query_type: QueryType, rest_arguments: List[str]):
        _exec_ = self.executor.get(query_type)
        if _exec_:
            return await _exec_.__run__(
                query_type=query_type, rest_arguments=rest_arguments
            )

    async def run(self, input_filepath: str = None):

        if input_filepath:
            commands = Handler._load_input(input_filepath)
            for arg in commands:
                arguments = arg
                print(arg)
                arguments = str(arguments).split(" ")
                query_type: QueryType = QueryType(arguments[0])
                rest_arguments = arguments[1:]
                try:
                    output = await self.run_executor(
                        query_type=query_type, rest_arguments=rest_arguments
                    )
                    print(output)
                except BankingException as e:
                    print(e)

            raise Exception("listen_done")
        else:
            arguments = Handler.__arguments__()
            query_type: QueryType = QueryType(arguments[0])
            rest_arguments = arguments[1:]
            await self.run_executor(
                query_type=query_type, rest_arguments=rest_arguments
            )
