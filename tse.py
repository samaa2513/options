'''A module to download ticker info'''
import persian
import requests
import urls


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
}

def get_code(_ticker):
    '''ticker'''
    _ticker = persian.convert_ar_characters(_ticker)
    url_search = urls.url_search.format(_ticker)
    html_search = requests.get(url_search, headers=HEADERS, timeout=30).text
    for ticker_info in html_search.split(';'):
        splitted_ticker_info = ticker_info.split(',')
        if persian.convert_ar_characters(splitted_ticker_info[0]) == _ticker:
            return splitted_ticker_info[2]
        else:
            raise NameError(f'{_ticker} does not exist. Please enter another one')

if __name__ == '__main__':
    ticker = input('Insert ticker: ')
    code = get_code(ticker)
    print(code)
