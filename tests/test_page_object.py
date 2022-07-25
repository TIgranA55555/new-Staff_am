
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.VacancyPage import VacancyPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_with_page_objects(BaseClass):

    def test_page_object(self):
        elem = HomePage(self.driver).jobItems()
        dropdown = Select(elem)
        job_titles_num = len(dropdown.options)
        dropdown.select_by_index(2)
        vacancyPageObject = HomePage(self.driver).jobSearch()
        #WebDriverWait(self.driver, 30)
        filter_by_job_category = vacancyPageObject.getJobTitleCategory()
        filter_by_job_category_numbers = vacancyPageObject.getJobTitleCategoryVacancyNums()

        filter_by_job_category_num = len(filter_by_job_category)
        assert job_titles_num - 1 == filter_by_job_category_num
        job_category_names = []
        for job in filter_by_job_category:
            job_category_names.append(job.text)

        job_category_count = []
        for job in filter_by_job_category_numbers:
            job_category_count.append(job.text)
        job_category_count_new = list(map(lambda x: int(x.strip("()")), job_category_count))
        assert len(job_category_names) == len(job_category_count_new)

        job_vacancies_dict = dict(zip(job_category_names, job_category_count_new))

        assert job_vacancies_dict['Quality Assurance /Control'] == len(
            vacancyPageObject.getVacanciesList())

    def test_mid_level(self):
        pass


