# content of test_class.py
import pytest
import sys


class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "check"
        assert hasattr(x, "check")

    def test_three(self):
        assert 7 == 5

    def add_numbers(self, x, y):
        return x + y

    @pytest.mark.skip(reason='do not execute this test add number function')
    # Skip this test case using skip decorator
    def test_add(self):
        assert self.add_numbers(7, 5) == 4

    def string_comp(self):
        return 'String'


    def test_string_comparison(self):
        assert self.string_comp() == 'Abc'

    @pytest.mark.skipif(sys.version_info > (3, 3), reason='do not execute this test add number function')
    # Skip this test case using skipif decorator if version>(3,3)
    def test_add_negative_numbers(self):
        assert self.add_numbers(-1, 5) == 4

    @pytest.mark.parametrize('num1,num2,result', [
        (7, 5, 12), ('Hello', ' World', 'hello world')
    ])
    def test_parametrise_decorator_fuction(self, num1, num2, result):
        assert self.add_numbers(num1, num2) == result

    @pytest.mark.xfail
    def test_string_xfail(self):
        assert self.string_comp() == 'Abc'
