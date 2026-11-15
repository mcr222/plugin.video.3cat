from resources.lib.video.FolderVideo import FolderVideo
from resources.lib.utils.Urls import url_coleccions, url_mesvist


def getList(strings):
    coleccions = FolderVideo(strings.get('coleccions'), "", "coleccions", "", "")
    directe = FolderVideo(strings.get('directe'), "", "directe", "", "")
    pellicules = FolderVideo("Pel·lícules", "", "pellicules", "", "")
    return [coleccions, directe, pellicules]
