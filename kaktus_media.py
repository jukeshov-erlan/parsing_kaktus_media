import requests
from bs4 import BeautifulSoup as bs


def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    return response.text


def special_data_for_desc(html):
    soup = bs(html, 'lxml')
    return soup


def get_data(html):
    soup = bs(html, 'html.parser')
    information = soup.find('div', class_ = 'Tag--articles')
    for info in information:
        try:
            title = info.find('a', class_='ArticleItem--name').text.strip()
            # print(title)
        except:
            title = ''

        try:
            description_link = info.find('a', class_='ArticleItem--name').get('href')
            # print(description_link)
        except:
            description_link = ''


        try:
            photo = info.find('img').get('src')
            # print(photo)
        except:
            photo = ''

        description = special_data_for_desc(get_html(description_link))
        print(description)


    data = []


        # data = {
        #     'title': title,
        #     'description': description,
        #     'time': time,
        #     'photo': photo
        # }
        # write_to_csv(data)
        
    


def main():
    url = 'https://kaktus.media/?lable=8&date=2023-12-14&order=time'
    html = get_html(url)                                               #response
    get_data(html)



main()