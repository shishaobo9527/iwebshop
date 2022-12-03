from base.base_operation import BaseOperation
from page.addcart_element import AddCartElement


class AddCartOperation(BaseOperation):

    def add_to_cart(self, index):
        self.hover(AddCartElement.all_products)
        self.hover(AddCartElement.food_and_drinks)
        self.click(AddCartElement.imported_foods)
        self.clicks(AddCartElement.goods_title, index)
        self.switch_handle()
        self.click(AddCartElement.join_cart_button)





