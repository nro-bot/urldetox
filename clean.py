#!/usr/bin/python3
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from sys import argv


def delargs(url_keys, whitelist_keys, url_data):
    todel = []
    for key in url_keys:
        if key not in whitelist_keys:# 'search-alias'
            todel.append(key)
    for k in todel:
        url_keys.pop(k, None)
    clean_url = url_data._replace(query=urlencode(url_keys, True))
    clean_url = urlunparse(clean_url)
    return clean_url

def clean_url(input_url_str):
    print('Cleaning URL:\n', input_url_str, '\n')
    # clean_url = ''

    url_data = urlparse(input_url_str)
    query_params = parse_qs(url_data.query)
    clean_url = url_data._replace(query=None).geturl()

    ######## AMAZON ########
    if 'amazon' in url_data.netloc:
        # print('query params', query_params)

        # Check for 'product' type url
        if  '/dp/' in url_data.path:
            clean_url = clean_url.split('/ref')[0]

        # Check for search
        elif '/s/' in url_data.path:
            whitelist = ['url', 'field-keywords', 'rh']
            clean_url = delargs(query_params.keys(), whitelist, url_data)

        elif '/b/' in url_data.path:
            whitelist = ['node']
            clean_url = delargs(query_params.keys(), whitelist, url_data)


    ######## GOOGLE ########
    elif 'google' in url_data.netloc:
        todel = []
        for key in query_params.keys():
            if key not in ['q']:
                todel.append(key)
        for k in todel:
            query_params.pop(k, None)
        clean_url = url_data._replace(query=urlencode(query_params, True))
        clean_url = urlunparse(clean_url)

    ######## EBAY ########
    elif 'google' in url_data.netloc:
        todel = []
        for key in query_params.keys():
            if key not in ['q']:
                todel.append(key)
        for k in todel:
            query_params.pop(k, None)
        clean_url = url_data._replace(query=urlencode(query_params, True))
        clean_url = urlunparse(clean_url)

    ######## GENERIC ########
    else:
        for key in query_params.keys():
            if 'utm' or 'ref' in key:
                # print('key', key)
                todel.append(key)
        for k in todel:
            query_params.pop(k, None)
        clean_url = url_data._replace(query=urlencode(query_params, True))

    print('DONE. Cleaned url:\n', clean_url)

if __name__ == '__main__':
    input_url_str = str(argv[1])
    # print('argv', argv)
    
clean_url(input_url_str)

"""
# remove ref,
# remove everything except search-alias nad field keywords
"""


