from base.base_util import BaseUtil
from page.addcart_operation import AddCartOperation


class TestAddCart(BaseUtil):

    def test_01_add_to_cart(self):
        ac = AddCartOperation(self.driver)
        ac.add_to_cart(0)







