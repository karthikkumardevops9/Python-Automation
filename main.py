from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\Owner\\OneDrive\\Desktop\\DevOpsCourse\\Python\\Python-Automation\\chromedriver.exe')
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-info bars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service,options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())