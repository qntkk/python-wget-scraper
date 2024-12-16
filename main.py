import requests
import time
import os
url = 'https://web.archive.org/cdx/search/cdx?url=https://a-site-with-media/*&fl=original&collapse=digest&filter=mimetype:video/mp4'

print("scraping ...")
t1 = time.time()
r = requests.get(url, stream=True) 
print("scraped list ", str(time.time()-t1), "s")

t1 = time.time()
for index, link in enumerate(r.iter_lines(decode_unicode=True)):
    print(link)
    r2 = requests.get(link)  
    with open(os.path.join('downloadedvids', link.split("/")[-1]), 'wb') as fd:
        fd.write(r2.content)

print("fetched ", index, " items in ", time.time()-t1, " seconds")