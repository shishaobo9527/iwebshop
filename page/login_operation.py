from base.base_operation import BaseOperation
from page.login_element import LoginElement


class LoginOperation(BaseOperation):

    def login(self, username='zhangsan', password='123456'):
        self.click(LoginElement.login_icon)
        self.send_keys(LoginElement.username, username)
        self.send_keys(LoginElement.password, password)
        self.click(LoginElement.submit)



