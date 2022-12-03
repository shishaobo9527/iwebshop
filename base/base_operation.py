from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BaseOperation:

    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    # 定位一组元素
    def locator_elements(self, loc):
        return self.driver.find_elements(*loc)

    # 点击
    def click(self, loc):
        self.locator_element(loc).click()

    def clicks(self, loc, index):
        self.locator_elements(loc)[index].click()

    # 输入值
    def send_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 进入框架
    def goto_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 退出框架
    def quit_frame(self):
        self.driver.switch_to.default_content()

    # 选中下拉框元素
    def select_dropbox(self, loc, value):
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)

    # 切换窗口
    def switch_handle(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)

    # 悬停
    def hover(self, loc):
        ActionChains(self.driver).move_to_element(self.locator_element(loc)).perform()

    # 弹框（alert/confirm/prompt）
    def alert(self):
        al = self.driver.switch_to.alert
        al.accept()








