from InternetSpeedTwitterBot import InternetSpeedTwitterBot
from selenium.webdriver.chrome.service import Service

PROMISED_DOWN = "The Promised download spead of your internet contract"
PROMISED_UP = "The Promised upload spead of your internet contract"
CHROME_WEBDRIVER_PATH = "The path to your chrome webdriver"
TWITTER_EMAIL = "Your twitter email"
TWITTER_PASSWORD = "Your twitter password"

ser = Service(CHROME_WEBDRIVER_PATH)

bot = InternetSpeedTwitterBot(ser)

bot.get_internet_speed()

print(f"UP {bot.up}\nDOWN {bot.down}")

if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    MESSAGE = f"Hey Internet Provider, why is my internet speed {bot.down}down/{bot.up}up when I pay for " \
              f"{PROMISED_DOWN}down/{bot.up}up?"
    bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, MESSAGE)
