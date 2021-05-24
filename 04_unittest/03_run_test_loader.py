import unittest
from Tools.HTMLTestRunner import HTMLTestRunner
import time
import html_report

suit = unittest.defaultTestLoader.discover('../testcases', pattern='test*.py')
# unittest.TextTestRunner().run(suit)
html_report.getHTMLReport(suit)
# with open(report_path, 'wb') as f:
#     html_runner = HTMLTestRunner(stream=f, title='自动化测试报告').run(suit)
