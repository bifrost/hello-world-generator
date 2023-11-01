"""
Test the hello world generator.
"""
import unittest

from ..src.hello_world import (
    simple_hello_world,
)


class GeneratorTest(unittest.TestCase):
    """
    Test the hello world generator.
    """

    def test_simple_hello_world(self) -> None:
        """
        Test the simple hello world function.
        """
        actual = simple_hello_world()
        self.assertTrue(actual == "Hello world!")
