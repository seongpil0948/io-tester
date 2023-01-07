import unittest
from ..base import IoTestBase
from . import common, shop
from pprint import pprint
from itertools import chain
from importlib import import_module


def determineTest(v): return v.endswith("Test")


# suite = import_module("FrontRedirectTest", common.__package__)
if __name__ == '__main__':
    # print(">>>>> \n", common.__path__, "<<<<< \n")
    # print(">>>>> \n", common.__package__, "<<<<< \n")
    # print(">>>>> \n", dir(common), "<<<<< \n")

    # suitesNames = filter(getSuite, chain(dir(common), dir(shop)))
    runner = unittest.TextTestRunner(
        descriptions="[Service]IoFront Test ", verbosity=2)
    suite = unittest.TestSuite()
    for suiteName in filter(determineTest, chain(dir(common))):
        cases = getattr(common, suiteName)
        # print(">>>>> \n", dir(suite), "<<<<< \n")
        if issubclass(cases, IoTestBase):
            suite.addTests(cases.listTest())
    result = runner.run(suite)
