from selenium.webdriver.common.by import By

from base.base_operation import BaseOperation


class AddCartElement(BaseOperation):

    # 所有商品(XPATH)
    all_products = (By.XPATH, '/html/body/header/div[2]/div/div/div[1]/a/h3')

    # 食品饮料(LINK_TEXT)
    food_and_drinks = (By.LINK_TEXT, '食品饮料')

    # 进口食品(LINK_TEXT)
    imported_foods = (By.LINK_TEXT, '进口食品')

    # 商品标题(CLASS_NAME)
    goods_title = (By.CLASS_NAME, 'goods_title')

    # 加入购物车图标(ID)
    join_cart_button = (By.ID, 'joinCarButton')

