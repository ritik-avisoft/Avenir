from playwright.sync_api import Page,expect
from Pages.Home_page import HomePage

def test_on_plateform_page(open_app,page:Page):
    home_page=HomePage(page)
    expect(home_page.page_main_logo).to_be_visible()
    home_page.click_on_Sign_up_as_MFD(page)



    
