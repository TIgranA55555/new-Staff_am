from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r'C:\Users\USER\Desktop\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(20)
driver.get('https://staff.am/en')
driver.maximize_window()
elem = driver.find_element(By.ID, 'jobsfilter-category')
#elem.click()
dropdown = Select(elem)
job_titles_num = len(dropdown.options)
dropdown.select_by_index(2)
driver.find_element(By.XPATH, '//button[@data-url="/en/site/search"]').click()
wait = WebDriverWait(driver,30)
filter_by_job_category = driver.find_elements(By.XPATH, "//div[@id='jobsfilter-category']//label/en")
filter_by_job_category_numbers = driver.find_elements(By.XPATH, "//div[@id='jobsfilter-category']//label/span")

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

job_vacancies_dict = dict(zip(job_category_names,job_category_count_new))

assert job_vacancies_dict['Quality Assurance /Control']  == len(driver.find_elements(By.XPATH, '//div[@class="list-view"]/div'))

driver.close()