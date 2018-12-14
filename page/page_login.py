"""
    目标：PO模式page页面封装
    提示：
        1. 类名 为大驼峰模块名(去掉下划线)
        2. 每一步操作，为单独的方法
    核心：page页面对象要集成Base
"""
from selenium.webdriver.common.by import By

import page



# com.vcooline.aike爱客包名
from base.base import Base


class PageLogin(Base):

    def page_input_username(self, username):
        self.base_input_value(page.loc_username,username)

    def page_input_password(self, password):
        self.base_input_value(page.loc_password,password)

    def page_submit(self):
        self.base_click_element(page.loc_btn)
