import json

from resources.lib.tv3cat.TV3cat import TV3cat
import urllib.request, urllib.parse, urllib.error

tv3 = TV3cat("", "")
tv3.listColeccions()
#temporades = tv3.getListTemporades("https://www.3cat.cat/3cat/10-2")
#print(len(temporades))
#videos = tv3.getListVideos("https://www.3cat.cat/3cat/bricoheroes/capitols/temporada/2/")
#print(len(videos))
#print(videos[0])
videoId = 6176980
apiJsonUrl = "https://api-media.3cat.cat/pvideo/media.jsp?media=video&versio=vast&idint={}&profile=pc_3cat&format=dm".format(
    videoId)
print(apiJsonUrl)
with urllib.request.urlopen(apiJsonUrl) as response:
    data = response.read()
    json_data = json.loads(data)
    print(json_data['media']['url'][0]['file'])
