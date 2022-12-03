import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_util import BaseUtil
from page.login_operation import LoginOperation


class TestLogin(BaseUtil):

    def test_01_login(self):
        """正确的用户名和密码，登录成功"""
        lo = LoginOperation(self.driver)
        lo.login()

    # def test_01_login(self):
    #     """正确的用户名和密码，登录成功"""
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get("http://localhost:8081/iwebshop/index.php?controller=site&action=index")
    #     driver.find_element(By.LINK_TEXT, '登录').click()  # 首页右上角登录
    #     driver.find_element(By.NAME, 'login_info').send_keys("zhangsan")  # 用户名输入框
    #     driver.find_element(By.NAME, 'password').send_keys("123456")  # 密码输入框
    #     driver.find_element(By.XPATH, '//input[@value="登录"]').click()  # 登录提交
    #     lo = LoginOperation()
    #     lo.login()

    # def test_02_login(self):
    #     """正确的用户名和错误的密码，登录失败"""
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get("http://localhost:8081/iwebshop/index.php?controller=site&action=index")
    #     driver.find_element(By.LINK_TEXT, '登录').click()
    #     driver.find_element(By.NAME, 'login_info').send_keys("zhangsan")
    #     driver.find_element(By.NAME, 'password').send_keys("000000")
    #     driver.find_element(By.XPATH, '//input[@value="登录"]').click()
    #
    # def test_03_login(self):
    #     """错误的用户名和正确的密码，登录失败"""
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get("http://localhost:8081/iwebshop/index.php?controller=site&action=index")
    #     driver.find_element(By.LINK_TEXT, '登录').click()
    #     driver.find_element(By.NAME, 'login_info').send_keys("zhangsan2")
    #     driver.find_element(By.NAME, 'password').send_keys("123456")
    #     driver.find_element(By.XPATH, '//input[@value="登录"]').click()
    #
    # def test_04_add_to_cart(self):
    #     """添加购物车"""
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get("http://localhost:8081/iwebshop/index.php?controller=site&action=index")
    #     all_products = driver.find_element(By.XPATH, '/html/body/header/div[2]/div/div/div[1]/a/h3')
    #     ActionChains(driver).move_to_element(all_products).perform()
    #     food_and_drinks = driver.find_element(By.LINK_TEXT, '食品饮料')
    #     ActionChains(driver).move_to_element(food_and_drinks).perform()
    #     imported_foods = driver.find_element(By.LINK_TEXT, '进口食品')
    #     imported_foods.click()
    #     goods_title = driver.find_elements(By.CLASS_NAME, 'goods_title')
    #     goods_title[0].click()
    #     handles = driver.window_handles
    #     for handle in handles:
    #         if handle != driver.current_window_handle:
    #             driver.close()
    #             driver.switch_to.window(handle)
    #     join_cart_button = driver.find_element(By.ID, 'joinCarButton')
    #     join_cart_button.click()

    # def test_05_clear_cart(self):
    #     """清空购物车"""
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get("http://localhost:8081/iwebshop/index.php?controller=site&action=index")
    #     go_cart = driver.find_element(By.CLASS_NAME, 'go_cart')
    #     go_cart.click()
    #     clear_cart_button = driver.find_element(By.CLASS_NAME, 'clear_cart_btn')
    #     clear_cart_button.click()
    #     confirm = driver.find_element(By.CLASS_NAME, 'aui_state_highlight')
    #     confirm.click()
    #
    # def test_06_search(self):
    #     """搜索查询"""
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get("http://localhost:8081/iwebshop/index.php?controller=site&action=index")
    #     search_bar = driver.find_element(By.XPATH, '//input[@class="search_keyword"]')
    #     search_bar.clear()
    #     search_bar.send_keys('电饭煲')
    #     search_icon = driver.find_element(By.XPATH, '//button[@class="search_submit"]')
    #     search_icon.click()





