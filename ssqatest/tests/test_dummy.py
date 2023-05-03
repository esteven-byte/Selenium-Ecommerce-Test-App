import pytest


# @pytest.mark.usefixtures("init_driver")
class TestDummy():

    def test_dummy_func(self):
        print("I am dummy testline 1")
        print("I am dummy testline 2")
        import pdb; pdb.set_trace()