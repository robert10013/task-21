import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Setup WebDriver path and options
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# Navigate to the Sauce Demo website
driver.get("https://www.saucedemo.com/")
time.sleep(3)  # Wait for the page to load

# Display cookies before login
print("Cookies before login:")
cookies_before_login = driver.get_cookies()
for cookie in cookies_before_login:
    print(cookie)

# Log in to the dashboard
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()
time.sleep(3)  # Wait for the page to load

# Display cookies after login
print("\nCookies after login:")
cookies_after_login = driver.get_cookies()
for cookie in cookies_after_login:
    print(cookie)
    # Log out from the dashboard
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(2)  # Wait for the menu to open

    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    logout_link.click()
    time.sleep(3)  # Wait for the page to load

    # Verify cookies after logout
    print("\nCookies after logout:")
    cookies_after_logout = driver.get_cookies()
    for cookie in cookies_after_logout:
        print(cookie)

    # Close the browser
    # driver.quit()


