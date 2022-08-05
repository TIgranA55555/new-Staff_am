from selenium.webdriver.common.by import By

from PageObjects.profile_page import ProfilePage
from PageObjects.vacancy_page import VacancyPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    HOME_PAGE_BUTTON = (By.CLASS_NAME, 'navbar-header')
    JOBS_FILTER_CATEGORY = (By.ID, 'jobsfilter-category')
    SEARCH_BUTTON = (By.XPATH, '//button[@data-url="/en/site/search"]')
    NAVIGATION_BUTTONS = (By.XPATH, '//a[@class="hs_nav_link"]')
    NAVIGATION_BUTTONS_DROPDOWN = (By.XPATH, "//a[@class='nav-item dropdown-toggle']")
    FOR_JOB_SEEKERS = (By.XPATH, '//li[@class="hs_nav_item hs_dropdown_hover hs_open_dropdown dropdown"]')
    SIGN_IN = (By.XPATH, '//li/ul/li/a[@data-url="/en/users/registration/sign-in"]')
    USERNAME = (By.ID, "loginform-email")
    PASSWORD = (By.ID, 'loginform-password')
    LOGIN_BTN = (By.ID, 'btn_login')

    def click_on_home_page_button(self):
        home_page_btn = self.driver.find_element(*self.HOME_PAGE_BUTTON).click()
        return home_page_btn

    def click_on_job_titles(self):
        return self.driver.find_element(*self.JOBS_FILTER_CATEGORY)

    def click_on_search_button(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        vacancyPage = VacancyPage(self.driver)
        return vacancyPage

    def extract_navigation_buttons(self):
        return self.driver.find_elements(*self.NAVIGATION_BUTTONS)

    def extract_navigation_buttons_with_dropdowns(self):
        return self.driver.find_elements(*self.NAVIGATION_BUTTONS_DROPDOWN)

    def click_on_job_seekers(self):
        forJobSeekers = self.driver.find_element(*self.FOR_JOB_SEEKERS).click()
        return forJobSeekers

    def click_on_sign_in(self):
        signIn = self.driver.find_element(*self.SIGN_IN).click()
        return signIn

    def login_process(self):
        self.driver.find_element(*self.USERNAME).send_keys('tigranaavagyan@gmail.com')
        self.driver.find_element(*self.PASSWORD).send_keys('armeniA$11111')
        self.driver.find_element(*self.LOGIN_BTN).click()
        profilePage = ProfilePage(self.driver)
        return profilePage
