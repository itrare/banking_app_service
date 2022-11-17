from typing import Dict

from app.schema import QueryType


class BaseExecutor:

    async def __run__(self, query_type: QueryType):
        await self.__dict__.get(query_type)()


class Handler:
    executor: Dict[QueryType, BaseExecutor] = {}

    async def set_executor(self, query_type: QueryType, executor: BaseExecutor):
        self.executor[query_type] = executor

    async def run_executor(self, query_type: QueryType):
        _exec_ = self.executor.get(query_type)
        if _exec_:
            await _exec_.__run__(query_type=query_type)

    async def run(self):
        query_type: QueryType = QueryType(input())
        await self.run_executor(query_type=query_type)
