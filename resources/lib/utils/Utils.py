from builtins import str
import urllib.request, urllib.parse, urllib.error
import json
import xbmcgui
import xbmc


def buildUrl(query, base_url):
    return base_url + '?' + urllib.parse.urlencode(query)

def find_key_by_value(json_data, target_key):
    for key, value in json_data.items():
        if key == target_key:
            return key, value
    return None, None

def getHtml(url):
    try:

        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        link = response.read()
        response.close()


        return link

    except urllib.error.URLError as e:
        xbmc.log("getHtml error - " + str(e))
        xbmc.log("getHtml url - " + url)

        return None


def toSeconds(durada):
    if durada:

        if len(durada) == 8:
            # durada hh:mm:ss

            h = durada[0:2]
            m = durada[3:5]
            s = durada[6:]

            r = (int(h) * 3600) + (int(m) * 60) + int(s)

            return r

        elif len(durada) == 11:
            # PT00H32M13S

            h = durada[2:4]
            m = durada[5:7]
            s = durada[8:10]

            r = (int(h) * 3600) + (int(m) * 60) + int(s)

            return r

        else:

            return None

    else:

        return None
