import requests


class PortfolioSession:
    url_login = 'https://portfolio.bmstu.ru/login'

    def __init__(self, login, password):
        self.session = None
        self.login = login
        self.password = password

    def create_session(self):
        """ Create and return session."""
        session = requests.session()
        headers = {
            'origin': 'https://portfolio.bmstu.ru',
            'referer': 'https://portfolio.bmstu.ru/',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': ('Mozilla/5.0 (Macintosh;'
                           ' Intel Mac OS X 10_14_6) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/78.0.3904.97'
                           ' Safari/537.36')
        }
        session.headers.update(headers)
        login_data = {
            'login': self.login,
            'password': self.password,
        }
        resp = session.post(self.__class__.url_login,
                            data=login_data)
        self.session = session
        return resp

    def get_table(self, length, start):
        url = (
            'https://portfolio.bmstu.ru/portfolio/datatables?draw=11&columns%5B0%5D%5Bdata%5D=function&columns%5B0%5D'
            '%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsear'
            'ch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=function&columns%5B'
            '1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bse'
            'arch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=group&columns%5B2'
            '%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsea'
            'rch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=2&order%5B0%5D%5B'
            f'dir%5D=asc&start={start}&length={length}&search%5Bvalue%5D=&search%5Bregex%5D=false)')
        resp = self.session.get(url)
        if resp.status_code != 200:
            return None
        data = resp.json()['data']
        return data
