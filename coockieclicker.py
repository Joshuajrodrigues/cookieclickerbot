from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")


driver.implicitly_wait(10)
cookie = driver.find_element_by_id("bigCookie")
score = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id(
    "productPrice" + str(i)) for i in range(1, -1, -1)]
# upgrades = [driver.find_element_by_id(
#     "upgrade" + str(i))for i in range(1, -1, -1)]
actions = ActionChains(driver)
actions.click(cookie)
for i in range(5000):
    actions.perform()
    count = int(score.text.split(" ")[0])
    for item in items:
        val = int(item.text)
        if val <= count:
            buy_action = ActionChains(driver)
            buy_action.move_to_element(item)
            buy_action.click()
            buy_action.perform()


# pip install selenium
