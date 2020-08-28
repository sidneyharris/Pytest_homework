import pytest
import yaml

from homework2.check_cal import Calcultor


# @pytest.mark.parametrize(('a','b','result'),yaml.safe_load(open('../homework1/datas/data_add.yaml')))
# class CheckCal:
#     cal = Calcultor()
#
#     def check_a(self,a,b,result):
#
#         print('check a')
#         assert result == self.cal.add(a,b)
def check_a():
    print('check a')

class CheckAbc:
    def check_abc(self):
        print('abc')