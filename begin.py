# -*- coding:utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import HTMLTestRunner
# 把 login 目录添加到 path 下，这里用的相对路径
# import sys
# sys.path.append("\login")
# from login import baidu
# from login import huomao
# import allcase_list
# 这里需要导入测试文件

if __name__ == "__main__":
    # 定义一个单元测试容器
    # testunit=unittest.TestSuite()
    #
    # 用例组装数组
    # alltestnames =allcase_list.caselist()
    #
    # 将测试用例加入到测试容器中
    # makesuite加载整个类用例，a.a()加载某个用例
    # for test in alltestnames:
    #     testunit.addTest(unittest.makeSuite(test))

    # 用例目录
    listcase = 'E:\\selenium\\autotest\\testcase'

    def creatsuitel():
        testunit = unittest.TestSuite()
        # discover 方法,加载目录下testcase
        discover = unittest.defaultTestLoader.discover(
            listcase,
            pattern='case_*.py',
            top_level_dir=None
        )
        # discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
                print(testunit)
        return testunit

    alltestnames = creatsuitel()

    # 取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 定义个报告存放路径，支持相对路径
    filename = 'E:\\selenium\\autotest\\result\\' + now + 'result.html'
    fp = open(filename, "wb")

    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title=u'测试报告', description=u'用例执行情况：')

    # 运行测试用例
    runner.run(alltestnames)
