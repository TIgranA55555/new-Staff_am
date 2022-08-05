from selenium.webdriver.common.by import By

from PageObjects.mid_level_page import MidLevelPage


class VacancyPage:

    def __init__(self, driver):
        self.driver = driver

    JOB_TITLES = (By.XPATH, "//div[@id='jobsfilter-category']//label/en")
    JOB_TITLES_VACANCIES_NUMS = (By.XPATH, "//div[@id='jobsfilter-category']//label/span")
    VACANCIES_LIST = (By.XPATH, '//div[@class="list-view"]/div')
    MID_LEVEL = (By.XPATH, '//div//div[@id="jobsfilter-job_candidate_level"]/label/input[@value="3"]')

    def jobs_title_category_list(self):
        return self.driver.find_elements(*self.JOB_TITLES)

    def jobs_titles_vacancies_count_list(self):
        return self.driver.find_elements(*self.JOB_TITLES_VACANCIES_NUMS)

    def extract_vacancies_list(self):
        return self.driver.find_elements(*self.VACANCIES_LIST)

    def click_on_mid_level(self):
        self.driver.find_element(*self.MID_LEVEL).click()
        midLavelPage = MidLevelPage(self.driver)
        return midLavelPage
