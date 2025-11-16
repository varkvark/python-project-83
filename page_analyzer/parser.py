import requests
from bs4 import BeautifulSoup


def extract_data_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return {
            'title': (
                soup.find('title').text
                if soup.find('title')
                else None
            ),
            'h1': (
                soup.find('h1').text
                if soup.find('h1')
                else None
            ),
            'description': (
                soup.find('meta', attrs={'name': 'description'})['content']
                if soup.find('meta', attrs={'name': 'description'})
                else None
            ),
            'status_code': response.status_code
        }
    except requests.RequestException:
        return {'error': 'Произошла ошибка при проверке'}
