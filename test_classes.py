import pytest
from classes import *

class Test:
    def setup_method(self):
        self.tv1 = Television(0, 0, False)

    def teardown_method(self):
        del self.tv1

    # def test_init(self):
    #     assert self.tv1.power(self) == 'True'

    def test_volume_up(self):
        assert self.tv1.volume_up(self.volume) == 1