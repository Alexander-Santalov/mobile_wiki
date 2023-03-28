import os
from appium import webdriver
from dotenv import load_dotenv
from selene.support.shared import browser


class Application:

    def __init__(self, env):
        load_dotenv()
        user = os.getenv('LOGIN')
        key = os.getenv('KEY')
        url = os.getenv('APPIUM_BROWSERSTACK')
        if env == 'android':
            desired_capabilities = {
                "app": "bs://425839e6a98de51e3f63ac2fe0d80a101029905c",
                "deviceName": "Google Pixel 3",
                "os_version": "10.0",
                "platformName": "android",
                "project": "Python project",
                "build": "browserstack-build",
                "name": "Diplom"
            }

            driver = webdriver.Remote(command_executor=f"http://{user}:{key}@{url}/wd/hub",
                                      desired_capabilities=desired_capabilities)
            browser.config.driver = driver

    def destroy(self):
        browser.quit()
