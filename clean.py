#!/usr/bin/python3
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from sys import argv


def delargs(url_params, whitelist_keys, url_data):
    todel = []
    for key in url_params:
        if key not in whitelist_keys:# 'search-alias'
            todel.append(key)
    for k in todel:
        url_params.pop(k, None)
    clean_url = url_data._replace(query=urlencode(url_params, True), params=None)
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
        # the 'ref' is actually necessary most of the amazon urls 

        # Check for 'product' type url
        if  '/dp/' in url_data.path:
            clean_url = clean_url.split('/ref')[0]

        # Check for search
        elif '/s/' in url_data.path:
            whitelist = ['url', 'field-keywords', 'rh']
            clean_url = delargs(query_params, whitelist, url_data)

        elif '/b/' in url_data.path:
            whitelist = ['node']
            clean_url = delargs(query_params, whitelist, url_data)

    ######## GOOGLE ########
    elif 'google' in url_data.netloc:
        if '/url' in url_data.path: 
            #this is a URL redirect, as you might find when copying a link out of google hangouts
            clean_url = query_params['q'][0]
        else:
            whitelist = ['q']
            clean_url = delargs(query_params, whitelist, url_data)

    ######## BING (not well tested) ########
    elif 'bing' in url_data.netloc:
        whitelist = ['q']
        clean_url = delargs(query_params, whitelist, url_data)

    ######## YAHOO (not well tested) ########
    elif 'yahoo' in url_data.netloc:
        whitelist = ['p']
        clean_url = delargs(query_params, whitelist, url_data)

    ######## EBAY ########
    elif 'ebay' in url_data.netloc:
        if '/sch/' in url_data.path:
            # we should include '_sacat' as well, since it changes the results, but the URL is ugly
            # enough already
            todel = []
            for key in query_params.keys():
                if 'LH_' not in key and key != '_nkw':# 'search-alias'
                    todel.append(key)
            for k in todel:
                query_params.pop(k, None)
            clean_url = url_data._replace(query=urlencode(query_params, True))
            clean_url = urlunparse(clean_url)

        else: #items have no parameters -- strip all of them
            clean_url = url_data._replace(query=None).geturl()
            clean_url = urlunparse(clean_url)

    ######## GENERIC ########
    # Use BLACKLIST instead.
    else:
        todel = []
        for key in query_params.keys():
            if 'utm' or 'ref' in key:
                todel.append(key)
        for k in todel:
            query_params.pop(k, None)
        clean_url = url_data._replace(query=urlencode(query_params, True))
        clean_url = urlunparse(clean_url)


    ##########################
    print('DONE. Cleaned url:\n', clean_url)
    print('\nThe new URL is %0.0f percent of original length (before: %d chars, now: %d chars)' 
          % ( (len(clean_url) / len(input_url_str)*100), len(input_url_str), len(clean_url)) )
    return clean_url

if __name__ == '__main__':
    input_url_str = str(argv[1]).strip()
    # print('argv', argv)
    
    clean_url(input_url_str)

