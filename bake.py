import time, datetime, urllib2

from grazing.models import *
from BeautifulSoup import BeautifulSoup


allotments = Health.objects.all()
allotments_count = allotments.count()

counter = 0
for a in allotments:

    try:
        address = ('http://127.0.0.1:8000/allotments/{}/'.format(a.allotment_unique))
        html = urllib2.urlopen(address).read()
        soup = BeautifulSoup(html)

        html_str = "{}".format(soup)

        html_file= open("static/{}.html".format(a.allotment_unique),"w")
        html_file.write(html_str)
        html_file.close()

        counter += 1
        print "finished with {}, number {} out of {} total".format(a.allotment_unique, counter, allotments_count)
    except:
        print "SOMETHING'S FUCKED UP WITH {}".format(a.allotment_unique)
