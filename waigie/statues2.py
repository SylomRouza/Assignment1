from bs4 import BeautifulSoup

with open('sg_law_cleaned.txt', 'w', encoding='UTF-8') as clean_file:
    with open('sg_law.txt', 'r', encoding='UTF-8') as law_file:
        soup = BeautifulSoup(law_file.read(), features='html.parser')
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split('  '))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        clean_file.write(text)
        clean_file.write('\n')
