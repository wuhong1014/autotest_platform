#utf-8
import configparser
'''读取配置'''
class ConfInfo:
    def __init__(self,file):
        self.file=file
    def get_conf(self,section,option):
        config=configparser.ConfigParser()
        config.read(self.file)
        dictres={}
        if isinstance(option,list):
            for op in option:
                dictres[op]=config.get(section,op)
        else:
            dictres[option]=config.get(section,option)
        return dictres
