from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def decline_cookies(driver):
    try:
        consent_buttons = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button|//a"))
        )
        for button in consent_buttons:
            text = button.text.lower()
            if any(
                keyword in text
                for keyword in ["decline", "reject", "no", "dismiss", "close", "got it"]
            ):
                button.click()
                print(f"LOG: Clicked on cookie consent button: '{text}'")
                return
    except:
        print("ERROR: No cookie consent banner found.")


search_query = input("Feeling Lucky about: ")
driver = webdriver.Firefox()
driver.get("https://duckduckgo.com/")

search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_bar.send_keys(search_query)
search_bar.send_keys(Keys.RETURN)

first_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#r1-0 h2 a"))
)
first_link.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
decline_cookies(driver)
