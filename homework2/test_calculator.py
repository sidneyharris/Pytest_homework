
import pytest
from homework2.check_cal import Calcultor
import yaml

with open('testdatas/database.yml') as f:
    datas = yaml.safe_load(f)

class TestCal:
    cal = Calcultor()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,result',datas["add"])
    @pytest.mark.dependency(name="add")
    def test_add(self,star1,a,b,result):
        print('测试相加')
        assert result == self.cal.add(a,b)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(('a', 'b', 'result'),datas['sub'])
    @pytest.mark.dependency(depends=["add"])
    def test_sub(self,star1,a,b,result):
        print('测试相减')
        assert result == self.cal.sub(a,b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(('a', 'b', 'result'),datas['mul'])
    @pytest.mark.dependency(name="mul")
    def test_mul(self,star1,a,b,result):
        print('测试相乘')
        assert result == self.cal.mul(a,b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    @pytest.mark.parametrize(('a', 'b', 'result'),datas['div'])
    def test_div(self,star1,a,b,result):
        print('测试相除')
        try:
            assert result == self.cal.div(a,b)
        except Exception:
            raise Exception("除数不能为0")