import pytest
import source.shapes as shapes 

class TestCircle:

    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"tearing down method {method}")

    def test_one(self):
        assert True 

    def test_two(self):
        assert True