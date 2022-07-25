from selenium.webdriver.common.by import By

from PageObjects.VacancyPage import VacancyPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    jobs_filter_category = (By.ID, 'jobsfilter-category')
    search_button = (By.XPATH, '//button[@data-url="/en/site/search"]')

    def jobItems(self):
        return self.driver.find_element(*HomePage.jobs_filter_category)

    def jobSearch(self):
        self.driver.find_element(*HomePage.search_button).click()
        vacancyPage = VacancyPage(self.driver)
        return vacancyPage
