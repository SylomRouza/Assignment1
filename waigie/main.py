from selenium import webdriver

homepage = 'https://softwareengineering.stackexchange.com/?tab=month'
hot_questions_css = '#question-mini-list a.question-hyperlink'
question_body_css = '.js-post-body'
file_name = 'softwareengineering.txt'

print('Opening Chrome')
driver = webdriver.Chrome()
print('Getting homepage')
driver.get(homepage)
print('Getting hot questions!')
hot_questions = driver.find_elements_by_css_selector(hot_questions_css)[:20]  # Top 20 only
print('Hot questions retrieved!')

def file_writeln(my_file, content: str, delimiter: str = '\n'):
    my_file.write(content)
    my_file.write(delimiter)

print('Retrieving urls')
hot_questions_urls = []
for question in hot_questions:
    hot_questions_urls.append(question.get_attribute('href'))

print('Looping through hot questions')
with open(file_name, 'w', encoding='UTF-8') as my_file:
    for url in hot_questions_urls:
        driver.get(url)
        file_writeln(my_file, '%s | %s' % (driver.title, url))
        bodies = driver.find_elements_by_css_selector(question_body_css)
        for body in bodies:
            file_writeln(my_file, body.get_attribute('innerHTML').strip())
        file_writeln(my_file, '')

driver.close()
print('We\'re done!')
