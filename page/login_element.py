from selenium.webdriver.common.by import By
from base.base_operation import BaseOperation


class LoginElement(BaseOperation):
    # 首页右上角登录(LINK_TEXT)
    login_icon = (By.LINK_TEXT, '登录')

    # 用户名输入框(NAME)
    username = (By.NAME, 'login_info')

    # 密码输入框(NAME)
    password = (By.NAME, 'password')

    # 登录提交(XPATH)
    submit = (By.XPATH, '//input[@value="登录"]')







