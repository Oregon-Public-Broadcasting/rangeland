import time, datetime, urllib2

from grazing.models import *
from BeautifulSoup import BeautifulSoup

allotments = Health.objects.all()

for a in allotments:

    try:
        address = ('http://127.0.0.1:8000/allotments/{}/'.format(a.allotment_unique))
        html = urllib2.urlopen(address).read()
        soup = BeautifulSoup(html)

        html_str = "{}".format(soup)

        html_file= open("static/{}.html".format(a.allotment_unique),"w")
        html_file.write(html_str)
        html_file.close()

        print "finished with {}".format(a.allotment_unique)
    except:
            print "SOMETHING'S FUCKED UP WITH {}".format(a.allotment_unique)
