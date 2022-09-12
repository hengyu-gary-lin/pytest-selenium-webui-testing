import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import random
import string

class TestAcy():
    def test_reg(self, test_setup):
        #Account type
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[1]/div/div/div[1]').click()
        #personal
        test_setup.find_element(By.XPATH, '//*[@id="liWrapper"]/li[1]').click()
        #country
        test_setup.find_element(By.XPATH,'//*[@id="input-box"]/div[1]/div').click()
        test_setup.find_element(By.XPATH,'//*[@data-testid="country0"]').click()
        #title
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[3]/div/div/div[1]').click()
        test_setup.find_element(By.XPATH,'//*[@data-testid="title0"]').click()
        #first name
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[4]/div/input').send_keys('hengyu')
        #last name
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[6]/div/input').send_keys('lin')
        #email
        test_setup.find_element(By.XPATH,'//*[@data-testid="email"]').send_keys('test@gmail.com')
        #phone area
        pa = test_setup.find_element(By.CLASS_NAME, 'jss119')
        test_setup.execute_script("arguments[0].click();", pa)
        pa_t = test_setup.find_element(By.XPATH,'//*[@data-testid="undefined1"]')
        test_setup.execute_script("arguments[0].click();", pa_t)
        #phone number
        test_setup.find_element(By.XPATH,'//*[@data-testid="phone"]').send_keys('0910206016')
    
    def test_account_type(self, test_setup):
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[1]/div/div/div[1]').click()
        personal = test_setup.find_element(By.XPATH, '//*[@id="liWrapper"]/li[1]').click()
        msg_p = test_setup.find_element(By.XPATH,'//*[text()="Personal"]').text
        business = test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[1]/div/div/div[1]').click()
        msg_b = test_setup.find_element(By.XPATH, '//*[text()="Business"]').text
        assert msg_p == 'Personal'
        assert msg_b == 'Business'
    
    def test_invalid_first_name(self, test_setup):
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[4]/div/input').send_keys(' ')
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[6]/div/input').send_keys(' ')
        sleep(2)
        msg_req = test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[4]/span').text
        assert msg_req == 'This field is required*'
    
    invalid_meg = "Invalid first name.(max length 40)"
    invalid_symbol = ('!','@', '#', '$','%','^','*','+','|')
    random_string = ''.join(random.choice(string.ascii_letters) for i in range(41))
    @pytest.mark.parametrize("test_input, expected",[
        (invalid_symbol[0], invalid_meg),
        (invalid_symbol[1], invalid_meg),
        (invalid_symbol[2], invalid_meg),
        (invalid_symbol[3], invalid_meg),
        (invalid_symbol[4], invalid_meg),
        (invalid_symbol[5], invalid_meg),
        (invalid_symbol[6], invalid_meg),
        (invalid_symbol[7], invalid_meg),
        (invalid_symbol[8], invalid_meg),
        (random_string, invalid_meg)
        ])
    def test_invalid_first_name_with_symbol(self, test_setup, test_input, expected):
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[4]/div/input').send_keys(test_input)
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[6]/div/input').send_keys(' ')
        sleep(2)
        msg_req = test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[4]/span').text
        assert msg_req == expected

    e_iv_msg = 'The email format is wrong'
    @pytest.mark.parametrize("email_input, e_expected",[
        ('testAgmail.com', e_iv_msg),
        ('test@gmail', e_iv_msg),
        ('.test@gmail.com', e_iv_msg)
    ])
    def test_invalid_email(self, test_setup, email_input, e_expected):
        test_setup.find_element(By.XPATH,'//*[@data-testid="email"]').send_keys(email_input)
        test_setup.find_element(By.XPATH,'//*[@id="personal-basicinfo"]/div[2]/div/div/form/div[6]/div/input').send_keys(' ')
        sleep(2)
        msg_em = test_setup.find_element(By.XPATH, '//span[contains(text(),"The email format is wrong")]').text
        assert msg_em == e_expected