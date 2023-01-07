from abc import ABCMeta
import unittest
from lib.util.logger import IoLogger


class IoTestBase(unittest.TestCase, IoLogger, metaclass=ABCMeta):

    # @abstractclassmethod
    @classmethod
    def listTest(cls) -> list[object]:
        tests = [cls(p) for p in cls.__dict__.keys() if p.startswith(
            "test") and callable(cls.__dict__[p])]
        if len(tests) < 1:
            raise NotImplementedError(
                f"{cls.__name__} no method exists that start with test")
        return tests
