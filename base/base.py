"""
    目标：po模式base(基类)类封装
    操作：
        1. 新建类(以大驼峰风格去编写类名)
        2. 新建公共的方法
            1. 找元素封装
            2. 输入方法封装
            3. 点击方法封装

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_input_value(self,loc,value):
        #查找的元素被调用
        ele = self.base_find_element(loc)
        # 调用定位元素,先清除元素文本
        ele.clear()
        ele.send_keys(value)

    def base_click_element(self,loc):
        self.base_find_element(loc).click()

    #获取toast消息方法
    def base_get_toast(self,msg):
        #组装loc
        loc=By.XPATH,"//*[contain(@text,'"+msg+"')]"
        #查找元素方法
        return self.base_find_element(loc,timeout=3,poll=0.1).text
