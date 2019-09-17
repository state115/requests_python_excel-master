import unittest
import os
from appium import webdriver
from time import sleep
import time
import HTMLTestRunner #导入HTMLTestRunner.py进行输出结果,后文有介绍说明

# SimpleIOSTests 继承自 unittest.TestCase，该类中只包含了 test_scroll 一个测试用例
class SimpleIOSTests(unittest.TestCase):

    # 重写setUp()方法，设置自动化测试的一些基本参数
    def setUp(self):
        app = os.path.abspath('../../apps/HHH/build/Release-iphonesimulator/HHH.app')
        self.driver = webdriver.Remote(
                               command_executor='http://127.0.0.1:4723/wd/hub',
                               desired_capabilities={
                               'app': app,
                               'platformName': 'iOS',
                               'platformVersion': '10.2',
                               'deviceName': 'iPhone 7',
                               })

    # tearDown()中清除在数据库中产生的数据，然后关闭连接。注意tearDown的过程很重要，要为以后的TestCase留下一个干净的环境
    def tearDown(self):
        self.driver.quit()

    # 测试用例，以test开头
    def test_scroll(self):

        # 找到 accessibility_id 为 "button" 的控件执行 点击操作
        self.driver.find_element_by_accessibility_id('button').click()

        sleep(1)

        # 找到 值为 "HHH" 的控件
        textF1 = self.driver.find_element_by_name('HHH')

        print("HHHHHHHH1 %s" % (self.driver.contexts))
        print("HHHHHHHH2 %s" % (self.driver.page_source))

        sleep(1)

        # 为 textF1 输入框 赋值，只有 UITextFiled和UITextView可以改变值，如果发现能改变UIButton或者UILabel的值，请告知我 ��
        textF1.send_keys("HHHHHHH")

        sleep(1)
        # 消失键盘
        self.driver.hide_keyboard()

        try:
            sleep(1)
        except:
            pass



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)

    # 生成此刻的时间
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    # 输出文件
    filename = "/Users/Sp/Desktop/appiumresult" + timestr + ".html"
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                                       stream=fp,
                                       title='testresult',
                                       description='testreport'
                                       )
    runner.run(suite)
    fp.close()
