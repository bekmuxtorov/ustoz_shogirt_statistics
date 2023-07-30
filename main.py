import requests
from datetime import datetime
from bs4 import BeautifulSoup


def define_content(message_id: int) -> list[str]:
    url = 'https://t.me/UstozShogird/' + str(message_id)
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, "html.parser")
        elements = soup.find("meta", attrs={"name": "twitter:description"})
        content = elements.get("content")
        try:
            return content.replace(' ', '').splitlines()[-3].split('#')
        except IndexError:
            pass
    else:
        return None


def get_message_id(url: str) -> int:
    return int(url.split('/')[-1])


def main():
    first_message_id = input('first_message_id: ')
    first_message = 'https://t.me/UstozShogird/' + first_message_id
    last_message_id = input('first_message_id: ')
    last_message = 'https://t.me/UstozShogird/' + last_message_id
    for i in range(get_message_id(first_message), get_message_id(last_message)+1):
        start_time = datetime.now()
        content = define_content(i)
        last_time = datetime.now()
        print(f'{i}: Parsing uchun vaqt: {last_time - start_time} ')
        if content:
            try:
                data = f'INSERT INTO contents (message_id, need_why, texnologies, location) values ({i}, "{content[1]}", "{content[2:-1]}", "{content[-1]}");\n'
                with open("contents.sql", "a", encoding='UTF-8') as data_file:
                    data_file = data_file.write(data)
            except IndexError:
                pass
        else:
            continue


main()
print(''.join(['<', '='*30, '>']))
