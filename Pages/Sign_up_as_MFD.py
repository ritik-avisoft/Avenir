from playwright.sync_api import Page,expect

class SignUpAsMFD:

    def __init__(self,page:Page):
        self.page=page
        self.dob_input = page.get_by_placeholder("DD/MM/YYYY")
        self.select_gender = page.get_by_test_id("select-gender-trigger")
        self.first_name_input = page.locator("input[name='firstName']")
        self.last_name_input = page.locator("input[name='lastName']")
        self.email_input = page.locator("input[name='email']")
        self.get_otp_button = page.get_by_role("button", name="Get OTP")
        self.phone_input=page.get_by_label("Mobile")
        self.phone_get_otp_button = page.get_by_role("button", name="Get OTP").nth(1)
        self.otp_inputs = page.locator("input[maxlength='1']")
        self.address_field=page.get_by_label()
        
        
    def verify_user_on_MFD_sign_up_page(self):
        expect(self.page).to_have_url("https://staging-mf-partners.vercel.app/register/mfd")
    
    def enter_first_name(self, first_name:str):
        self.first_name_input.click()
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name:str):
        self.last_name_input.click()
        self.last_name_input.fill(last_name)

    def enter_dob(self, dob:str):
        self.dob_input.click()
        self.dob_input.fill(dob)

    def select_gender(self, gender:str):
        self.select_gender.click()
        self.page.get_by_test_id(gender).click()

    def enter_email(self, email:str):
        self.email_input.click()
        self.email_input.fill(email)

    def click_on_get_otp(self, n):
        self.get_otp_button.nth(n).click()
    
    def enter_otp(self, otp):
        self.page.wait_for_timeout(3000)
        for i,digit in enumerate(otp):
            self.otp_inputs.nth(i).type(digit)

    def enter_mobile(self, phone:str):
        self.phone_input.click()
        self.phone_input.fill(phone)

    def click_on_verify_button(self):
        self.page.get_by_role("button", name="Verify").click()
    
    
    