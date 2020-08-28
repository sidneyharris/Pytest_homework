import pytest
import yaml
from homework1.cal import Calcultor

'''
1、补全计算器（加减乘除）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、conftest.py中创建fixture 完成setup和teardown
4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
'''

# @pytest.mark.parametrize(('a','b'),yaml.safe_load(open('database.yml')))
class TestCal:
    cal = Calcultor()

    def test_add(self,star):
        datas = yaml.safe_load(open('datas/data_add.yaml'))
        print('测试相加')
        for data in datas:
            assert data[2] == self.cal.add(data[0],data[1])

    @pytest.mark.parametrize(('a','b','result'), yaml.safe_load(open('datas/data_sub.yaml')))
    def test_sub(self,star,a,b,result):
        print('测试相减')
        assert result == self.cal.sub(a,b)

    @pytest.mark.parametrize(('a', 'b', 'result'), yaml.safe_load(open('datas/data_mul.yaml')))
    def test_mul(self,star,a,b,result):
        print('测试乘法')
        assert result == self.cal.mul(a,b)

    @pytest.mark.parametrize(('a', 'b', 'result'), yaml.safe_load(open('datas/data_div.yaml')))
    def test_div(self,star,a,b,result):
        print('测试除法')
        assert result == self.cal.div(a,b)