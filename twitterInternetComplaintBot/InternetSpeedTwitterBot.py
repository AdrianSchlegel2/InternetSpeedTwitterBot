from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class InternetSpeedTwitterBot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=path)
        self.down = 0.0
        self.up = 0.0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.ID, "_evidon-banner-acceptbutton").click()
        sleep(1)

        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        sleep(10)

        while self.down == 0 or self.up == 0:
            try:
                self.driver.find_element(By.LINK_TEXT, "Back to test results").click()
                download = float(self.driver.find_element(
                    By.XPATH,
                    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                    '/div[2]/div/div[2]/span').text)

                upload = float(self.driver.find_element(
                    By.XPATH,
                    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                    '/div[3]/div/div[2]/span').text)

                self.down = download
                self.up = upload

            except NoSuchElementException:
                sleep(5)

    def tweet_at_provider(self, email, password, message):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(4)
        email_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
            'div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')

        email_input.send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2'
                                           ']/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]').click()
        sleep(2)

        try:
            password_input = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]'
                '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(password)
            self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]'
            ).click()

        except NoSuchElementException:
            popup_input = self.driver.find_element(By.TAG_NAME, "input")
            popup_input.send_keys("adrianschlegel1")
            self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'
            ).click()

            sleep(3)

            password_input = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]'
                '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(password)

            self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]'
            ).click()

        sleep(3)

        tweet_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]'
            '/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        tweet_input.send_keys(message)

        self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div'
            '[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div').click()
