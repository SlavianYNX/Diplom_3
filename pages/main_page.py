import allure
from pages.base_page import BasePage
from locators import locators


class HeaderPage(BasePage):


    @allure.step('Клик по кнопке Конструктор')
    def click_to_constructor_btn(self):
        self.move_to_element_click(locators.MainFuncConstruct.BUTTON_CONSTRUCT)

    @allure.step('Клик по кнопке Лента заказов')
    def click_to_order_btn(self):
        self.move_to_element_click(locators.MainFuncConstruct.BUTTON_ORDER_LENT)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_login_btn(self):
        self.click_button(locators.MainFuncConstruct.PERS_ACCOUNT)


class MainPage(BasePage):


    @allure.step('Проверка отображения формы конструктора')
    def check_view_constructor_form(self):
        return self.check_element(locators.MainFuncConstruct.CONSTRUCTOR_FORM)

    @allure.step('Проверка отображения формы Лента заказов')
    def check_view_order_lent_form(self):
        return self.check_element(locators.MainFuncConstruct.ORDER_LENT_FORM)

    @allure.step('Клик по Краторной булке N200i')
    def click_to_crators_bun(self):
        self.click_button(locators.MainFuncConstruct.BUN)

    @allure.step('Проверка отображения окна с информацией о булке')
    def check_view_info_ingredient(self):
        return self.check_element(locators.MainFuncConstruct.POP_WINDOW)

    @allure.step('Закрытие окна с информацией об ингредиенте')
    def close_popup_info(self):
        self.move_to_element_click(locators.MainFuncConstruct.BUTTON_CROSS)

    @allure.step('Проверка закрытия окна с ингредиентами')
    def check_close_popup(self):
        return self.check_element_not_vision(locators.MainFuncConstruct.POP_WINDOW)

    @allure.step('Добавить булку в корзину')
    def add_bun_cart(self):
        self.drag_and_drop(locators.MainFuncConstruct.BUN, locators.MainFuncConstruct.CART)

    @allure.step('Добавление соуса в корзину')
    def add_sauce_cart(self):
        self.drag_and_drop(locators.MainFuncConstruct.INGREDIENT_SAUCE, locators.MainFuncConstruct.CART)

    @allure.step('Добавление начинки в корзину')
    def add_filling_cart(self):
        self.drag_and_drop(locators.MainFuncConstruct.INGREDIENT_FILLING, locators.MainFuncConstruct.CART)

    @allure.step('Ожидание загрузки кнопки Оформление заказа')
    def wait_place_order_btn(self):
        self.wait_element_load(locators.MainFuncConstruct.PLACE_ORDER)

    @allure.step('Получение значения счетчика')
    def check_get_info_counter(self):
        return self.get_text_element(locators.MainFuncConstruct.COUNTER_INGREDIENT)
