# URL Detox

Removes all the tracking junk at the end of URLs, so you can copy and paste clean URLs to share with
your friends.

For instance:
```
$ python3 clean.py (Your url)
Cleaning URL:
 https://www.amazon.com/Streaming-Media-Players/b/ref=tv_nav_vid_dm?ie=UTF8&node=13447451&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=BB1NHPZQT2MW11NF24PF&pf_rd_r=BB1NHPZQT2MW11NF24PF&pf_rd_t=101&pf_rd_p=056b28a2-3a15-42af-98dc-25e80d7d3be9&pf_rd_p=056b28a2-3a15-42af-98dc-25e80d7d3be9&pf_rd_i=1266092011

DONE. Cleaned url:
 https://www.amazon.com/Streaming-Media-Players/b/ref=tv_nav_vid_dm?node=13447451
 ```

 Currently, rather hack-ish hardcoding to support amazon, google, and ebay.


## Todo

Links that will fail:

```


SOURCE CODE for flask boilerplate:
https://github.com/realpython/flask-boilerplate/

```

## Note

Example output of the urllib library:
```

In [160]: urlparse(glink)
Out[160]: ParseResult(scheme='https', netloc='www.google.com', path='/url', params='', query='q=https://gfycat.com/infiniteclumsygannet&sa=D&source=hangouts&ust=1528592055102000&usg=AFQjCNHCoxWZyt5tJ1PFZuoGK-QxVi6PGw', fragment='')
```

NOTE: Use `parse_qs` on the URL data, not directly on the URL strong!
Compare top (what is expected) vs bottom:

```
In [163]: parse_qs(urlparse(glink).query)
Out[163]: 
{'q': ['https://gfycat.com/infiniteclumsygannet'],
 'sa': ['D'],
 'source': ['hangouts'],
 'ust': ['1528592055102000'],
 'usg': ['AFQjCNHCoxWZyt5tJ1PFZuoGK-QxVi6PGw']}

In [161]: parse_qs(glink)
Out[161]: 
{'https://www.google.com/url?q': ['https://gfycat.com/infiniteclumsygannet'],
 'sa': ['D'],
 'source': ['hangouts'],
 'ust': ['1528592055102000'],
 'usg': ['AFQjCNHCoxWZyt5tJ1PFZuoGK-QxVi6PGw']}

```
