from selenium.webdriver.common.by import By

from PageObjects.midLevel import MidLevelPage


class VacancyPage:

    def __init__(self, driver):
        self.driver = driver

    job_titles = (By.XPATH, "//div[@id='jobsfilter-category']//label/en")
    job_titles_vacancies_nums = (By.XPATH, "//div[@id='jobsfilter-category']//label/span")
    vacancies_list = (By.XPATH, '//div[@class="list-view"]/div')
    mid_level = (By.XPATH, '//div//div[@id="jobsfilter-job_candidate_level"]/label/input[@value="3"]')

    def getJobTitleCategory(self):
        return self.driver.find_elements(*VacancyPage.job_titles)

    def getJobTitleCategoryVacancyNums(self):
        return self.driver.find_elements(*VacancyPage.job_titles_vacancies_nums)

    def getVacanciesList(self):
        return self.driver.find_elements(*VacancyPage.vacancies_list)

    def getMidLevel(self):
        self.driver.find_element(*VacancyPage.mid_level).click()
        midLavelPage = MidLevelPage(self.driver)
        return midLavelPage
