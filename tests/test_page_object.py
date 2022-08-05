import time

import pytest

from PageObjects.profile_page import ProfilePage
from PageObjects.vacancy_page import VacancyPage
from PageObjects.home_page import HomePage
from utilities.base_class import BaseClass


class Test_with_page_objects(BaseClass):
    #@pytest.mark.skip
    def test_home_page_object(self):
        HomePage(self.driver).click_on_home_page_button()
        vacancy_page_object_1 = self.open_vacancies_page_from_job_titles(HomePage(self.driver), 2)

        filter_by_job_category = vacancy_page_object_1.jobs_title_category_list()
        filter_by_job_category_numbers = vacancy_page_object_1.jobs_titles_vacancies_count_list()
        job_category_names = [job.text for job in filter_by_job_category]
        job_category_count = [job.text for job in filter_by_job_category_numbers]
        job_category_count_new = [int(x.strip("()")) for x in job_category_count]
        job_vacancies_dict = dict(zip(job_category_names, job_category_count_new))

        assert len(job_category_names) == len(job_category_count_new) and job_vacancies_dict[
            'Quality Assurance /Control'] == len(VacancyPage(self.driver).extract_vacancies_list())


    #@pytest.mark.skip
    def test_mid_level(self):
        HomePage(self.driver).click_on_home_page_button()
        vacancy_page_object_2 = self.open_vacancies_page_from_job_titles(HomePage(self.driver), 2)

        midLevelPageObject = vacancy_page_object_2.click_on_mid_level()
        view_more_buttons_list = midLevelPageObject.extract_view_more_buttons_list()
        self.checking_mid_level_with_loop(view_more_buttons_list, 2, midLevelPageObject)


    #@pytest.mark.skip
    def test_navigation_buttons(self):
        HomePage(self.driver).click_on_home_page_button()
        nav_btn_list = [elem.text for elem in HomePage(self.driver).extract_navigation_buttons()]
        btn_elements = HomePage(self.driver).extract_navigation_buttons_with_dropdowns()[:2]
        btn_elements_list = [elem.text for elem in btn_elements]
        nav_btn_list.extend(btn_elements_list)
        assert ['Jobs', 'Trainings', 'Companies', 'StaffMedia', 'For Companies', 'For Job-seekers'] == nav_btn_list

    #@pytest.mark.skip
    def test_profile_changing_notification(self):
        HomePage(self.driver).click_on_home_page_button()
        HomePage(self.driver).click_on_job_seekers()
        HomePage(self.driver).click_on_sign_in()
        time.sleep(3)
        HomePage(self.driver).login_process()
        time.sleep(3)
        self.driver.current_window_handle
        time.sleep(3)

        ProfilePage(self.driver).education_city_enter()
        self.verify_visibility_of_element(ProfilePage.NOTIFICATION, 10)
        assert "Notification" in ProfilePage(self.driver).notification_text()
