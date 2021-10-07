from selenium.webdriver.common.by import By


class HomePage:
    item_name = (By.LINK_TEXT, 'Iphone 6 32gb')
    item_cost = (By.XPATH,"//*[@id='tbodyid']/div[5]/div/div/h5")

    def __init__(self,driver):
        self.driver = driver

    def click_item(self):
        return self.driver.find_element(*HomePage.item_name)
    def cost_item(self):
        return self.driver.find_element(*HomePage.item_cost)