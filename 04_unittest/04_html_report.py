from Tools.HTMLTestRunner import HTMLTestRunner
import time

report_path = '../Report/{}.html'.format(time.strftime('%Y%m%d%H%M%S'))


def getHTMLReport(suit):
    with open(report_path, 'wb') as f:
        HTMLTestRunner(stream=f, title='自动化测试报告').run(suit)
