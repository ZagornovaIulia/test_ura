
from bs4 import BeautifulSoup
import re


def typograph(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    def process_text(text):
        text = re.sub(r' - ', ' — ', text)
        text = text.replace("”", "«", 1)
        text = text[::-1].replace('”', '»', 1)[::-1]
        text = re.sub(r'”(.*?)”', lambda match: f'„{match.group(1)}“', text)

        return text

    for element in soup.find_all(text=True):
        if element.parent.name not in ['script', 'style']:
            element.replace_with(process_text(element))

    return str(soup)


html_input = '<h1>”Стоимость такого решения на 30-40% дешевле покупки в рознице”, - сказал Шестаков.</h1><p class=”kek” style=”color: red”>””Победа” останется или уйдет? Ценник Norwind в два раза выше”, - написала в группе аэропорта Кургана пользователь Юлия Зинченко.</p>'
html_output = typograph(html_input)
print(html_output)
