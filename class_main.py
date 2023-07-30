import requests
from datetime import datetime
from bs4 import BeautifulSoup


class Define:
    def __init__(self):
        self.BASE_URL = 'https://t.me/UstozShogird/'

    def get_message_id(self, url: str) -> int:
        return int(url.split('/')[-1])

    def get_content(self, url: str):
        return requests.get(url)

    def define_content(self, message_id: int) -> list[str]:
        url = self.BASE_URL + str(message_id)
        request = self.get_content(url)
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, "html.parser")
            elements = soup.find("meta", attrs={"name": "twitter:description"})
            content = elements.get("content")
            return content.replace(' ', '').splitlines()[-3].split('#')
        else:
            return None

    def write_sql(self, first_message_id: int, last_message_id: int):
        for i in range(first_message_id, last_message_id+1):
            start_time = datetime.now()
            content = self.define_content(i)
            last_time = datetime.now()
            print(f'{i}: Time for parsing: {last_time - start_time} ')
            if content:
                try:
                    data = f'INSERT INTO contents (message_id, need_why, texnologies, location) values ({i}, "{content[1]}", "{content[2:-1]}", "{content[-1]}");\n'
                    with open("contents.sql", "a", encoding='UTF-8') as data_file:
                        data_file = data_file.write(data)
                except IndexError:
                    pass
            else:
                continue


def main():
    first_message_id = int(input('first_message_id: '))
    last_message_id = int(input('last_message_id: '))

    content = Define()
    content.write_sql(first_message_id, last_message_id)


if __name__ == "__main__":
    main()
