"""
目标：PO模式scripts脚本实现
    操作：
        1. 新建测试模块(test_页面对象.py)
        2. 类名(使用大驼峰去掉下划线)
        3. 不用过脑(def setup_class teardown_class test_login)编写三个方法
            setup_class
                1. 实例化 page页面对象
            teardown_class
                1. 关闭 driver对象
            test_login()
                1.根据操作步骤调用page对象内方法
                2. 断言
                3. 截图
"""
import sys
import os

import allure

sys.path.append(os.getcwd())
from base.read_login_txt import ReadLoginTxt
from base.read_login_yaml import ReadLoginYaml
import pytest
from base.get_driver import get_driver
from page.page_login import PageLogin

# 用yaml
# def get_data():
#     datas=ReadLoginYaml("data_login.yaml").raad_login_yaml().values()
#     arrs=[]
#     for data in datas:
#         arrs.append((data.get("username"),data.get("password")))
#     return arrs
#用txt:
def get_data():
    datas=ReadLoginTxt().read_login_txt().values()
    arrs=[]
    for data in datas:
        arrs.append((data.get("username"),data.get("password")))
    return arrs

class TestLogin():
    def setup_class(self):
        self.login = PageLogin(get_driver())

    def teardown_class(self):
        self.login.driver.quit()

    #allure是用来增强报告的,优先级,测试步骤描述,测试内容描述8

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("登录操作")
    @pytest.mark.parametrize("username,password", get_data())
    def test_login(self, username, password):
        # 输入用户名
        allure.attach("登录操作","")
        self.login.page_input_username(username)
        # 输入密码
        self.login.page_input_password(password)
        # 点击登录
        self.login.page_submit()
