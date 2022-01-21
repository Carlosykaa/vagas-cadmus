import pyderman as dr
from selenium import webdriver
from time import sleep


class Cadmus:
    def __init__(self):
        self.url = 'https://cadmus.com.br/vagas-tecnologia/'
        self.path = dr.install(dr.chrome, file_directory="./driver/", overwrite=True, filename="chromedriver.exe")
        print(self.path)
        self.driver = webdriver.Chrome(self.path)
        self.driver.implicitly_wait(30)

    
    def access_site(self):
        self.driver.get(self.url)
    
    
    def move_to_element(self):
        try:
            scroll = self.driver.find_elements_by_tag_name('h3')[1]
            scroll.location_once_scrolled_into_view()
        except TypeError:
            pass
        sleep(0.5)
    

    def get_name_local(self):
        elements = self.driver.find_elements_by_css_selector('a[class="btn azul"]')
        self.gen_data = []
        for num, element in enumerate(elements):
            infos = {}
            infos['name'] = self.driver.find_elements_by_tag_name('h3')[num].text
            infos['local'] = self.driver.find_elements_by_class_name('local')[num].text
            infos['script'] = self.driver.find_elements_by_css_selector('a[class="btn azul"]')[num].get_attribute('onclick')
            infos['link'] = self.driver.find_elements_by_css_selector('a[class="btn azul"]')[num].get_attribute('href')
            self.gen_data.append(infos)
        

    def get_desc(self):
        for job in self.gen_data:
            self.driver.execute_script(job.get('script'))
            self.driver.get(job.get('link'))
            job['desc'] = self.driver.find_element_by_css_selector('div[id="boxVaga"] p').text
            self.driver.get('https://cadmus.com.br/vagas-tecnologia/')
    

    def driver_quit(self):
        self.driver.quit()
