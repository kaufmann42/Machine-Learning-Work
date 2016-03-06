import urllib


def duplicateGeroProtector(geroprotectors, token, link):
    x = 0
    while token + str(x) in geroprotectors:
        x += 1
    geroprotectors[token+str(x)] = link

    return geroprotectors

def findGeroProtectors():
    geroprotectors = {}

    for x in range(1, 100):
        checkpage = len(geroprotectors)
        print "Found " + str(len(geroprotectors)) + " geroprotectors! Searching for more..."
        print "Checking page " + str(x) + " for results.."
        f = urllib.urlopen("http://geroprotectors.org/?page=" + str(x))
        result = f.read()

        # page = requests.get('http://geroprotectors.org/?page=1')
        #
        # broken_html = unicode(page.content, "utf-8")
        #
        # parser = etree.HTMLParser()
        # tree   = etree.parse(StringIO(broken_html), parser)

        # result = etree.tostring(tree.getroot(), pretty_print=True, method="html")

        tokenized = result.split('>')

        for x in range(0,len(tokenized)):
            if '/compounds/' in tokenized[x] and x+1 < len(tokenized):
                if tokenized[x+1][:-3] not in geroprotectors:
                    geroprotectors[tokenized[x+1][:-3]] = tokenized[x+12][43:-1]
                else:
                    geroprotectors = duplicateGeroProtector(geroprotectors, \
                                                            tokenized[x+1][:-3], \
                                                            tokenized[x+12][43:-1])
        if len(geroprotectors) == checkpage:
            print "no new entries!"
            break

    return geroprotectors

results = findGeroProtectors()

print results
print len(results)
