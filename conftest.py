import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://acy-zh.com/en/open-live-account")
    driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/img').click()
    driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[3]/a').click()
    yield driver
    driver.quit()