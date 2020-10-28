from selenium import webdriver
from random import randrange

driver = webdriver.Chrome()

def file_writeln(my_file, content: str, delimiter: str = '\n'):
    my_file.write(content)
    my_file.write(delimiter)


with open('sg_law.txt', 'w', encoding='UTF-8') as my_file:
    for i in range(27):
        current_url = 'https://sso.agc.gov.sg/Browse/Act/Current/All/%d?PageSize=20&SortBy=Title&SortOrder=ASC' % i
        driver.get(current_url)
        # $('table.table.browse-list tbody tr td:not(.hidden-xs)>a')
        # Randomly select 1
        selected_act_url = driver\
                            .find_elements_by_css_selector('table.table.browse-list tbody tr td:not(.hidden-xs)>a')[randrange(20)]\
                            .get_attribute('href')
        driver.get(selected_act_url)
        this_law = driver.find_element_by_css_selector('#legis.legis')
        file_writeln(my_file, this_law.get_attribute('innerHTML').strip())

driver.close()
print('We\'re done!')
