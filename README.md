# URL Detox

Removes all the tracking junk at the end of URLs, so you can copy and paste clean URLs to share with
your friends.

Currently deployed at:
http://urldetox.nfshost.com/

(I may move to http://urldetox.pythonanywhere.com depending on how much the NFShost costs) 

Currently, this project has rather hack-ish hardcoding support for amazon, google, and ebay.

## Example
```
$ python3 clean.py (Your url)
Cleaning URL:
 https://www.amazon.com/Streaming-Media-Players/b/ref=tv_nav_vid_dm?ie=UTF8&node=13447451&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=BB1NHPZQT2MW11NF24PF&pf_rd_r=BB1NHPZQT2MW11NF24PF&pf_rd_t=101&pf_rd_p=056b28a2-3a15-42af-98dc-25e80d7d3be9&pf_rd_p=056b28a2-3a15-42af-98dc-25e80d7d3be9&pf_rd_i=1266092011

DONE. Cleaned url:
 https://www.amazon.com/Streaming-Media-Players/b/ref=tv_nav_vid_dm?node=13447451
 ```


For more:
https://gist.github.com/nouyang/0834e5bce03a0f27f64da06636e1371f

## Quickstart (Local)

Clone, 

```
git clone https://github.com/nouyang/urldetox.git
cd urldetox
pip install -r requirements.txt
export FLASK_APP=/home/protected/urldetox/app.py
export FLASK_DEBUG=0
python3 -m flask run
```

To debug, you can run the cleaning (detox, stripping, etc.) script directly on the commandline:
```
python3 clean.py 'http://yoururl.com/?q=some-parameters'
```

## Notes
SOURCE CODE for flask boilerplate:
https://github.com/realpython/flask-boilerplate/

https://bootswatch.com/sandstone/k

To deploy, see django:
https://blog.nearlyfreespeech.net/2014/11/17/how-to-django-on-nearlyfreespeech-net/

Notably, at the moment it seems that after git pull, it is still necessary to go through the NFShost web interface and send a KILL signal to the daeomn (which will the automatically restart) for changes to percolate.


### Notes on first time setup on NearlyFreeSpeech 

Create a new site on NFS.

SSH in to server.  `ssh membername_sitename@ssh.phx.nearlyfreespeech.net`
The git clone to /home/protected (this directory created for you by NFS).
```python 
pip install -r requirements.txt
```

Then created a file `run-flask.sh` as follows:
```sh
#!/bin/sh
export FLASK_APP=/home/protected/urldetox/app.py
export FLASK_DEBUG=0
exec python3 -m flask run
```

Then **make sure to make the file executable**

```
chmod a+x run-flast.sh
```

Finally, use the webinterface to set up a daemon for `/home/protected/run-flask.sh` 
https://members.nearlyfreespeech.net/nouyang/sites/urldetox

### Notes on pythonanywhere

As promised, was dead simple to set u [https://www.pythonanywhere.com/pricing/](PythonAnywhere).

[http://blog.pythonanywhere.com/121/](A beginner's guide to building a simple database-backed Flask website on PythonAnywhere).
### Notes (for myself) on urllib 

https://github.com/nouyang/WTFisThisRegister/blob/master/WTFisThisRegister.py

### Notes to self on urllib 
Example output of the urllib library:
```

In [160]: urlparse(glink)
Out[160]: ParseResult(scheme='https', netloc='www.google.com', path='/url', params='', query='q=https://gfycat.com/infiniteclumsygannet&sa=D&source=hangouts&ust=1528592055102000&usg=AFQjCNHCoxWZyt5tJ1PFZuoGK-QxVi6PGw', fragment='')
```

**NOTE: Use `parse_qs` on the URL data, not directly on the URL string!**
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


### Notes on 'algorithm' (hardcoded rules)

On Ebay, I found that parameters whos names began with "LH" were used to filter the 
The Amazon links were really annoying to deal with. I feel like most of the time I just want to link
people to products anyway, so I dealt with that easy case and made an attempt at URLs you might get
if you wanted to link someone to a search you did. Annoyingly, for amazon the `ref` parameter does
seem to affect the page you get when you enter in a link.

If we don't find a "known" website in the url, then it passes through and we just strip the url of
any obvious ones such as "utm" and "ref".

## Similar project

urlclean.com -- but it only supports Google links, so I went ahead and made my own to support more
links.

## Todo

There's a lot of CSS stuff I want to fix. An easy one would be to add the print out of how many
hara

# Thanks

I welcome contributions of code, bug reports, feature wishes, or indication if you found this useful. 

I can be contacted at `githubusername@alum.mit.edu`.
