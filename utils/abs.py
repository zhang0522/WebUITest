# -*- encoding:utf-8 -*-

'''
单例模式
'''
def Singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner
