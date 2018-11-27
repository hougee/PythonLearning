#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
功能说明：通过命令行为运行程序添加参数
使用方法：
      直接在命令行输入如下内容
      python ArgvArgparse.py -h
      python ArgvArgparse.py xiaoming 1991.11.11
      python ArgvArgparse.py xiaoming 1991.11.11 -p xiaohong xiaohei -a 25 -r han -g female -o 1 2 3 4 5 6
'''

__author__ = 'HouBin'

import sys
import argparse
def cmd():
    '''
    ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True)
    （1）prog ：文件名，默认为sys.argv[0]，用来在help信息中描述程序的名称
    （2）usage ：描述程序用途的字符串
    （3）description ：help信息前显示的信息
    （4）epilog ：help信息之后显示的信息
    （5）parents ：由ArgumentParser对象组成的列表，它们的arguments选项会被包含到新ArgumentParser对象中。(类似于继承)
    （6）formatter_class ：help信息输出的格式
    （7）prefix_chars ：参数前缀，默认为’-‘(最好不要修改)
    （8）fromfile_prefix_chars ：前缀字符，放在文件名之前
    （9）conflict_handler ：解决冲突的策略，默认情况下冲突会发生错误，(最好不要修改)
    （10）add_help ：是否增加-h/-help选项 (默认为True)，一般help信息都是必须的。设为False时，help信息里面不再显示-h –help信息
    （11）argument_default： - (default: None)设置一个全局的选项的缺省值，一般每个选项单独设置，基本没用
    '''
    args = argparse.ArgumentParser(description = 'Personal Information ',epilog = 'Information end ')
    '''
    ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
    （1）name or flags ：参数有两种，可选参数（parser.add_argument('-f', '--foo')）和位置参数（parser.add_argument('bar')）
    （2）action： 默认为store
    （3）metaver：帮助信息中显示的参数名称
    （4）nargs： 参数的数量（*(任意多个，可以为0个)，+(一个或更多)，?（首先从命令行获得参数，如果有-y后面没加参数，则从const中取值，如果没有-y，则从default中取值））
    （5）const ：保存一个常量
    （6）default ：默认值
    （7）type ：参数类型，默认为str
    （8）choices ：设置参数值的范围，如果choices中的类型不是字符串，记得指定type
    （9）required ：该选项是否必选，默认为True
    （10）dest ：参数名
    '''
    #必写属性,第一位
    args.add_argument("name",type = str,help = "Your name")
    #必写属性,第二位
    args.add_argument("birth",type = str,help = "birthday")
    #可选属性,默认为None
    args.add_argument("-r",'--race',  type = str, dest = "race",help = u"民族")
    #可选属性,默认为0,范围必须在0~150
    args.add_argument("-a", "--age",  type = int, dest = "age",help = "Your age",default = 0,choices=range(150))
    #可选属性,默认为male
    args.add_argument('-g',"--gender", type = str, dest = "gender", help = 'Your gender', default = 'male', choices=['male', 'female'])
    #可选属性,默认为None,-p后可接多个参数
    args.add_argument("-p","--parent",type = str, dest = 'parent', help = "Your parent",default = "None", nargs = '*')
    #可选属性,默认为None,-o后可接多个参数
    args.add_argument("-o","--other", type = str, dest = 'other',  help = "other Information",required = False,nargs = '*')
    
    args = args.parse_args()  #返回一个命名空间,如果想要使用变量,可用args.attr
    print("argparse.args=",args,type(args))
    print('name = %s'%args.name)
    d = args.__dict__
    for key,value in d.items():
        print('%s = %s'%(key,value))

if __name__=="__main__":
    cmd()
