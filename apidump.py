import json
import codecs
from urllib.request import urlopen

url = "http://letsrant.azurewebsites.net/api/values"

reader = codecs.getreader("utf-8")
obj = json.load(reader(urlopen(url)))

print (obj)
