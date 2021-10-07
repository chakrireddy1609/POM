import pytest

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class Test_E2E:

    def test_e2e_blaze(self):
        assert self.driver.title == "STORE"
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)
        product_name_home = homePage.click_item().text
        product_cost_home = homePage.cost_item().text
        homePage.click_item().click()
        product_name_click = self.driver.find_element_by_class_name("name").text
        product_cost_click = self.driver.find_element_by_class_name("price-container").text
        assert product_name_home == product_name_click
        assert product_cost_home in product_cost_click
        self.driver.find_element_by_xpath("//a[text()='Add to cart']").click()
        self.driver.find_element_by_id("cartur").click()
        product_name_cart = self.driver.find_element_by_xpath("//*[@id='tbodyid']/tr/td[2]").text
        product_cost_cart = self.driver.find_element_by_id("totalp").text
        assert product_name_home == product_name_cart
        assert product_cost_cart in product_cost_home
        self.driver.find_element_by_xpath("//button[text()='Place Order']").click()
        self.driver.find_element_by_id("name").send_keys("Chakri")
        self.driver.find_element_by_id("country").send_keys("India")
        self.driver.find_element_by_id("city").send_keys("Hyderabad")
        self.driver.find_element_by_id("card").send_keys("1234567890")
        self.driver.find_element_by_id("month").send_keys("October")
        self.driver.find_element_by_id("year").send_keys("2022")
        self.driver.find_element_by_xpath("//button[text()='Purchase']").click()
        alert_text = self.driver.find_element_by_xpath("//div[contains(@class,'sweet-alert')]/h2").text
        assert "Thank you for your purchase!" in alert_text


