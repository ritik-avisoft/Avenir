
def captureOTP(page, Sign_up_as_MDF, n=0):
    #this wait for any http respond metching the OTP api endpoint
    with page.expect_response("**/api/v1/partner_credentials_otp") as resp_info:
        Sign_up_as_MDF.click_on_get_otp(n)

    response =resp_info.value
    json_data= response.json()
    otp = json_data["data"]["OTP"]
    return otp