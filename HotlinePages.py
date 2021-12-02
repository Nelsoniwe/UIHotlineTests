from Base import BasePage
from selenium.webdriver.common.by import By

class HotlineSeacrhLocators:
    LOCATOR_HOTLINE_SEARCH_FIELD = (By.ID, 'searchbox')
    LOCATOR_HOTLINE_SEARCH_BUTTON = (By.ID, 'doSearch')
    LOCATOR_HOTLINE_RESPONSE_TITLE = (By.CLASS_NAME, 'title__main')
    LOCATOR_HOTLINE_NAV_LINK_DETI = (By.CLASS_NAME, 'deti')
    LOCATOR_HOTLINE_RESPONSE_CELL12 = (By.CLASS_NAME, "cell-12")

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(HotlineSeacrhLocators.LOCATOR_HOTLINE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(HotlineSeacrhLocators.LOCATOR_HOTLINE_SEARCH_BUTTON,time=2).click()

    def get_response_title_name(self):
        return self.find_element(HotlineSeacrhLocators.LOCATOR_HOTLINE_RESPONSE_TITLE).text

    def find_navigation_bar_element(self):
        return self.find_element(HotlineSeacrhLocators.LOCATOR_HOTLINE_NAV_LINK_DETI,time=2)

    def click_on_the_navigation_bar_element(self,element):
        return element.click()

    def get_response_navigation_bar_element_title(self):
        return self.find_elements(HotlineSeacrhLocators.LOCATOR_HOTLINE_RESPONSE_CELL12,time=2)[2].text