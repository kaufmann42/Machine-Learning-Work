import urllib
import csv

class GeroProtector(object):
    """docstring for GeroProtector"""
    def __init__(self, name, link):
        self.name = name
        self.links = []
        self.links.append(link)

    def addLink(self, link):
        self.links.append(link)

# checks the first 100 pages of the geroprotectors website for geroprotectors and forms a list of objects
def findGeroProtectors():
    # geroprotectors list of GeroProtector objects
    geroprotectors = []

    # search first 100 pages
    for x in range(1, 100):
        # variable used to check if a page has new entries
        checkpage = len(geroprotectors)

        # system message
        print "Found " + str(len(geroprotectors)) + " geroprotectors! Searching for more..."
        print "Checking page " + str(x) + " for results.."

        # open page
        f = urllib.urlopen("http://geroprotectors.org/?page=" + str(x))

        # read and tokenize result based on html formatting
        result = f.read()
        tokenized = result.split('>')

        # search page for geroprotectors and/or add links to geroprotector
        for x in range(0,len(tokenized)):
            if '/compounds/' in tokenized[x] and x+1 < len(tokenized):
                cache = [w for w in geroprotectors if w.name == tokenized[x+1][:-3]]
                name = tokenized[x+1][:-3]
                link = tokenized[x+12][43:-1]
                if not cache:
                    geroprotectors.append(GeroProtector(name,link))
                else:
                    cache[0].addLink(link)

        # exit if no geroprotectors found
        if len(geroprotectors) == checkpage:
            print "no new entries... exiting!"
            break

    # return a list of geroprotectors with there relevant links
    return geroprotectors

results = findGeroProtectors()

print [w.name for w in results]
print len(results)

def writeCSV(arg):
    with open('data.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
