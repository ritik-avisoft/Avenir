from playwright.sync_api import Page,expect
from Pages.Sign_up_as_MFD import SignUpAsMFD
from helpers.otp_helper import captureOTP
from Pages.Home_page import HomePage

def test_sign_up_as_mfd(open_app, page:Page):
    sign_up=SignUpAsMFD(page)
    home_page=HomePage(page)

    home_page.click_on_Sign_up_as_MFD(page)
    sign_up.verify_user_on_MFD_sign_up_page()
    # sign_up.click_on_general_info()
    sign_up.enter_first_name("Ritik")
    sign_up.enter_last_name("Ranjan") 
    sign_up.enter_dob("01/01/2002")
    # page.pause()
    # sign_up.select_gender("Male")

    sign_up.enter_email("abcdefg@gmail.com")

    email_otp=captureOTP(page,sign_up)
    otp = email_otp
    sign_up.enter_otp(str(otp))
    sign_up.click_on_verify_button()

    sign_up.enter_mobile("7683649229")

    mobile_otp=captureOTP(page, sign_up, 1)
    otp = mobile_otp
    print(otp)
    sign_up.enter_otp(str(otp))
    sign_up.click_on_verify_button()

    page.pause()


