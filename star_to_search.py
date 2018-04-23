import random
import xml.etree.ElementTree as ET, urllib.request, gzip, io

def are_close(col1, col2):
    """This function used to compare values of collections with numeric data
    """
    if len(col1) != len(col2):
        raise ValueError("Different size of input collections")
    result = []
    for x, y in zip(col1, col2):
        result.append(abs(abs(x) - abs(y)) < 0.4)
    
    r = True
    for c in result:
        r = r & c
    return r


def get_known_stars():    
    url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
    oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))

    mags = []
    magsB = []
    magsV = []
    magsJ = []
    magsH = []
    magsK = []

    for planet in oec.findall(".//star"):
        name = planet.findtext("name")
        magB = planet.findtext("magB")
        magV = planet.findtext("magV")
        magJ = planet.findtext("magJ")
        magH = planet.findtext("magH")
        magK = planet.findtext("magK")

        if magB and magV and magJ and magH and magK:
            f_magB = float(planet.findtext("magB"))
            magsB.append(f_magB)
            f_magV = float(planet.findtext("magV"))
            magsV.append(f_magV)
            f_magJ = float(planet.findtext("magJ"))
            magsJ.append(f_magJ)
            f_magH = float(planet.findtext("magH"))
            magsH.append(f_magH)
            f_magK = float(planet.findtext("magK"))
            magsK.append(f_magK)
            mag = [name, f_magB, f_magV, f_magJ, f_magH, f_magK]
            mags.append(mag)
    
    return mags, magsB, magsV, magsJ, magsH, magsK

mags, magsB, magsV, magsJ, magsH, magsK = get_known_stars()

minB = min(magsB)
maxB = max(magsB)
minV = min(magsV)
maxV = max(magsV)
minJ = min(magsB)
maxJ = max(magsB)
minH = min(magsH)
maxH = max(magsH)
minK = min(magsK)
maxK = max(magsK)

found = False
iterations = 0
while not found:

    r_magB = random.uniform(minB, maxB)
    r_magV = random.uniform(minV, maxV)
    r_magJ = random.uniform(minJ, maxJ)
    r_magH = random.uniform(minH, maxH)
    r_magK = random.uniform(minK, maxK)

    r_mag = [r_magB, r_magV, r_magJ, r_magH, r_magK]

    iterations = iterations + 1

    if iterations % 100000 == 0:
        print('iteration: ', iterations)

    for m in mags:
        close = are_close(r_mag, m[1:])
        if close:
            found = True
            print('Star: ', m)
            print('Random magnitudes: ', r_mag)
