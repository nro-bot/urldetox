#!/usr/bin/python3
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from sys import argv

def clean_url(input_url_str):
    # print('Cleaning URL:\n', input_url_str, '\n')
    # clean_url = ''

    url_data = urlparse(input_url_str)
    query_params = parse_qs(url_data.query)
    clean_url = url_data._replace(query=None).geturl()

    if 'amazon' in url_data.netloc:
        # print('query params', query_params)

        # Check for product
        if  '/dp/' in url_data.path:
            clean_url = clean_url.split('/ref')[0]

        # Check for search
        elif '/s/' in url_data.path:
            todel = []
            for key in query_params.keys():
                if key not in ['url', 'field-keywords', 'rh']:# 'search-alias'
                    # print('key', key)
                    todel.append(key)
            for k in todel:
                query_params.pop(k, None)
            clean_url = url_data._replace(query=urlencode(query_params, True))
            clean_url = urlunparse(clean_url)

    print('Cleaned url:\n', clean_url)

if __name__ == '__main__':
    input_url_str = str(argv[1])
    # print('argv', argv)
    
clean_url(input_url_str)

"""


# remove ref,
# remove everything except search-alias nad field keywords

url = 'http://example.com/?a=text&q2=text2&q3=text3&q2=text4'

u = urlparse(url)
query = parse_qs(u.query)
query.pop('q2', None)
u = u._replace(query=urlencode(query, True))
print(urlunparse(u))


a1._replace(query=None).geturl()
"""
