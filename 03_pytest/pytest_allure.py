"""
   pytest-allure 测试报告美化和定制
   allure特性：
    - 希望在测试报告中看到测试功能，子功能，测试场景，测试步骤，以及附加信息
        @allure.feature（模块） , story（testcase）, step, attach
        attach :数据，文本，图片，视频，等附加信息

    - 过滤执行
        需求：上线前把主流程和重要模块跑一遍
        //按特性执行
        features优先级大于stories
         --allure-features/ --allure-stories
        pytest -v -s pytest_allure.py --allure-features '登陆模块'
        pytest -v -s pytest_allure.py --allure-stories '登陆失败'

        //按重要级别执行
        @allure.severity(allure.severity_level.NORMAL)
         pytest -v -s  pytest_allure.py --allure-severities normal,trivial


    - 关联测试用例（给测试用例加地址链接）:将allure报告和测试管理系统集成，
        //@allure.link("www.baidu.com", name="链接") 链接太长，用name指定别名
        //@allure.testcase(TESTCASE_LINK, "testcase title")

        //@allure.issue("140", "这是一个issue")
           pytest pytest_allure.py --allure-link-pattern=issue:http://www.baidu.com/issue/{} --alluredir=./report/3

    - 在测试报告里添加网页和截图，和文本
        //   allure.attach 文本和html
        //   allure.attach.file  图片

    - 如果自动化测试和手工测试关联起来，能覆盖手工测试到一定比例，这就说明自动化测试有价值
      @allure.testcase 能关联到测试用例管理路径下，就能计算测试用例覆盖率
      @allure.issue 是用来关联你的测试bug单链接的的（公司测试bug管理工具上的路径）

      自动化测试可以做到当测试用例运行失败，自动生成一个bug单，并同时关联上？
"""
import allure


@allure.feature("登陆模块")
class TestLogin():

    @allure.story("登陆成功")
    def test_login_success(self):
        with allure.step("输入用户民"):
            print("输入用户民")
        with allure.step("输入密码"):
            print("输入密码")
        print("登陆成功")
        pass

    @allure.story("登陆失败")
    def test_login_fail(self):
        print("登陆失败")
        pass

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_001(self):
        print("登陆失败")
        pass


@allure.feature("登陆模块02")
class TestLogin02():

    @allure.story("登陆成功02")
    def test_login_success(self):
        with allure.step("输入用户民02"):
            print("输入用户民02")
        with allure.step("输入密码02"):
            print("输入密码02")
        print("登陆成功02")
        pass

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("www.baidu.com", name="链接")
    def test_login_fail(self):
        print("登陆失败02")
        pass

    TESTCASE_LINK = "管理测试用例的地址"

    @allure.testcase(TESTCASE_LINK, "testcase title")
    def test_login_testcase_link(self):
        print("登陆失败02")
        pass

    # --allure-link-pattern=issue:链接地址/issue/{}
    # --allure-link-pattern=issue:https://www.baidu.com/issue/{}
    # 运行  pytest pytest_allure.py --allure-link-pattern=issue:http://www.baidu.com/issue/{} --alluredir=./report/3
    # 140 issueId
    @allure.issue("140", "这是一个issue")
    def test_login_issue_link(self):
        print("登陆失败02")
        pass


def test_attach_text():
    allure.attach("这是一个纯文本信息", attachment_type=allure.attachment_type.TEXT)
    print("附加纯文本信息")


def test_attach_html():
    allure.attach("<body>这是一个body</body>", "这是一个html", attachment_type=allure.attachment_type.HTML)
    print("附加html")


def test_attach_photo():
    # 注意：图片要用allure.attach.file
    allure.attach.file("/Users/neil/PycharmProjects/pythonGame/Third/Source/1.png", "这是一个图片",
                       attachment_type=allure.attachment_type.PNG)
    print("附加图片")
