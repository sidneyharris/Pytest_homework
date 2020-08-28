import pytest

@pytest.fixture(scope='function')

def star():
    print('开始计算')
    yield None
    print('计算结束')

