import urllib2
import urllib
import re
import webbrowser

print "Loading..."
request = urllib2.Request("http://www.itechzero.com/google-mirror-sites-collect.html")
response = urllib2.urlopen(request)
content = response.read().decode("utf-8")
pattern = pattern = re.compile('<span style="color:red">.*?</span><a href="(.*?)" target="_blank">(.*?)</a>',re.S)
items = re.findall(pattern,content)
quan = 0
for item in items:
    print item[0],'\n',item[1],'\n\n'
    quan+=1

print "\n\nThis website has ",quan," recommended links."

webbrowser.open(items[1][0])
