from typing import List

import pytest
import yaml


@pytest.fixture(scope='function',autouse="True")
def star1():
    print('开始计算')
    yield None
    print('计算结束')

'''收集上来的测试用例实现定制化功能eg:执行顺序、编码问题、自定义标签
    1.items就是所有的测试用例列表，item代表每个测试用例对象
'''
# def pytest_collection_modifyitems(
#     session:"Session",config:"Config",items: List["Item"]
# ) ->None:
#     # items.reverse()#翻转列表顺序
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # if "add" in item.nodeid:
        #     item.add_marker(pytest.mark.add)
        # elif 'sub' in item.nodeid:
        #     item.add_marker(pytest.mark.sub)
        # elif 'mul' in item.nodeid:
        #     item.add_marker(pytest.mark.mul)
        # elif "div" in item.nodeid:
        #     item.add_marker(pytest.mark.div)

def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  #group 将下面所有到option都展示在这个group下
    mygroup.addoption("--env",  #注册一个命令行选项
                    default='test',
                    dest='env',
                    help='set your run env'
                      )

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env",default='test')
    if myenv =='test':
        print('获取测试数据')
        with open("testdatas/test/test.yaml") as f:
            datas = yaml.safe_load(f)
    elif myenv =='dev':
        print('获取开发数据')
        with open("testdatas/test/dev.yaml") as f:
            datas = yaml.safe_load(f)

    elif myenv =='st':
        print('获取系统数据')
        with open("testdatas/test/st.yaml") as f:
            datas = yaml.safe_load(f)
    return datas