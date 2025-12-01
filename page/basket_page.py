from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Not a basket page"

    def should_be_empty_basket(self):
        self.should_not_be_basket_items()
        self.should_be_empty_basket_message()

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"

        message_element = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        message_text = message_element.text
        assert "empty" in message_text.lower() or "пуста" in message_text.lower(), \
            f"Empty basket message text is incorrect: '{message_text}'"
