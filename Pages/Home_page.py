from playwright.sync_api import Page,expect

class HomePage:

    def __init__(self,page:Page):
        self.page=page
        self.page_main_logo=page.locator(".flex.cursor-pointer")
        self.page_login_button=page.get_by_role("button", name="Login")
    
    def verify_user_on_home_page(self):
        expect(self.page).to_have_url("https://staging-mf-partners.vercel.app/")

    def click_on_Sign_up_as_MFD(self,page:Page):
        self.sign_up_as_MFD=page.locator("text=Sign up as MFD")
        self.sign_up_as_MFD.click()

    # we should verify this inside the SignUpAsMFD page 
    # def verify_user_on_sign_up_page(self):
    #     expect(self.page).to_have_url("https://staging-mf-partners.vercel.app/register/mfd")

    def click_on_Sign_up_as_partner(self, page:Page):
        self.sign_up_as_partner=page.locator("text=Sign up as Partner")
        self.sign_up_as_partner.click()
        # expect(page).to_have_url("https://staging-mf-partners.vercel.app/register/partner")

    

