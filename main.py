from HotlinePages import SearchHelper

def test_hotline_searchBox(browser):
    hotline_main_page = SearchHelper(browser)
    hotline_main_page.go_to_site()

    search_text = "Razer Basilisk Ultimate Black (RZ01-03170100-R3G1)"
    hotline_main_page.enter_word(search_text)
    hotline_main_page.click_on_the_search_button()
    response = hotline_main_page.get_response_title_name()
    assert search_text in response

def test_catalog_selected(browser):
    hotline_main_page = SearchHelper(browser)
    hotline_main_page.go_to_site()

    search_text = "Дитячі товари"
    nav_bar = hotline_main_page.find_navigation_bar_element()
    hotline_main_page.click_on_the_navigation_bar_element(nav_bar)

    response = hotline_main_page.get_response_navigation_bar_element_title()
    assert search_text in response