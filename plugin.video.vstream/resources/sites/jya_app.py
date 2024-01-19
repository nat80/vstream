# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# return False  # CF depuis le 26/11/2020
import json
import re

from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import VSlog, VSupdate, progress, siteManager, dialog
from resources.lib.util import cUtil, Unquote
import xbmcgui

SITE_IDENTIFIER = 'jya_app'
SITE_NAME = 'JYA'
SITE_DESC = ' films remux'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

MOVIE_NEWS = (URL_MAIN + 'filmsenstreaming/', 'showMovies')
MOVIE_GENRES = (True, 'showMovieGenres')

SERIE_NEWS = (URL_MAIN + 'seriesenstreaming/', 'showMovies')
SERIE_GENRES = (True, 'showSerieGenres')
SERIE_VF = (URL_MAIN + 'seriesenstreaming/series-vf/', 'showMovies')
SERIE_VOSTFR = (URL_MAIN + 'seriesenstreaming/series-vostfr/', 'showMovies')

key_search_movies = '#searchsomemovies'
key_search_series = '#searchsomeseries'
URL_SEARCH = (URL_MAIN + 'get_movie_links2', 'showMovies')
URL_SEARCH_MOVIES = (key_search_movies, 'showMovies')
URL_SEARCH_SERIES = (key_search_series, 'showMovies')

# recherche utilisé quand on n'utilise pas le globale
MY_SEARCH_MOVIES = (True, 'showSearchMovie')
MY_SEARCH_SERIES = (True, 'showSearchSerie')

# Menu GLOBALE HOME
MOVIE_MOVIE = (True, 'showMenuMovies')
SERIE_SERIES = (True, 'showMenuTvShows')


def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_SEARCH[0])
    # oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche Films & Series', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_MOVIES[1], 'Recherche Films', 'search.png', oOutputParameterHandler)

    # oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    # oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    # oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    # oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

    # oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_SERIES[0])
    # oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_SERIES[1], 'Recherche Séries ', 'search.png', oOutputParameterHandler)

    # oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    # oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    # oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    # oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Série (Genres)', 'genres.png', oOutputParameterHandler)

    # oOutputParameterHandler.addParameter('siteUrl', SERIE_VF[0])
    # oGui.addDir(SITE_IDENTIFIER, SERIE_VF[1], 'Séries (VF)', 'vf.png', oOutputParameterHandler)

    # oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFR[0])
    # oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFR[1], 'Série (VOSTFR)', 'vostfr.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


# def showMenuMovies():
#     oGui = cGui()

#     oOutputParameterHandler = cOutputParameterHandler()
#     oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_MOVIES[0])
#     oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_MOVIES[1], 'Recherche Films', 'search.png', oOutputParameterHandler)

#     oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
#     oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)

#     oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
#     oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

#     oGui.setEndOfDirectory()


# def showMenuTvShows():
#     oGui = cGui()

#     oOutputParameterHandler = cOutputParameterHandler()
#     oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_SERIES[0])
#     oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_SERIES[1], 'Recherche Séries', 'search.png', oOutputParameterHandler)

#     oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
#     oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries (Derniers ajouts)', 'news.png', oOutputParameterHandler)

#     oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
#     oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Série(Genres)', 'genres.png', oOutputParameterHandler)

#     oOutputParameterHandler.addParameter('siteUrl', SERIE_VF[0])
#     oGui.addDir(SITE_IDENTIFIER, SERIE_VF[1], 'Séries (VF)', 'vf.png', oOutputParameterHandler)

#     oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFR[0])
#     oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFR[1], 'Série(VOSTFR)', 'vostfr.png', oOutputParameterHandler)

#     oGui.setEndOfDirectory()


def showSearchSerie():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = key_search_series + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return




def showSearchMovie(sTmdb2=''):
    VSlog("showSearchMovie")
    oDialog = dialog()
    oDialog.VSinfo('Recherche en cours...')
    # progress = xbmcgui.DialogProgressBG()
    
    
    # progress.create("wait", "test")
    # progress.update(50, "recherche" )

    # progress_.VSupdate(progress_, 100)

    oInputParameterHandler = cInputParameterHandler()
    sTmdbId = oInputParameterHandler.getValue('sTmdb')
    sYear = oInputParameterHandler.getValue('sYear')
    sTitle = oInputParameterHandler.getValue('sTitle')
    VSlog("sTmdbId")
    VSlog(sTmdbId)
    VSlog("sYear")
    VSlog(sYear)
    VSlog("sTitle")
    VSlog(sTitle)
    
    showMovies(sTmdbId, sTitle, sYear)
    return


def showSearch():
    VSlog("Calling showSearch")
    oInputParameterHandler = cInputParameterHandler()
    sTmdbId = oInputParameterHandler.getValue('sTmdb')
    sYear = oInputParameterHandler.getValue('sYear')
    sTitle = oInputParameterHandler.getValue('sTitle')
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = sSearchText
        VSlog("sSearchText")
        VSlog(sSearchText)
        showMovies(sTmdbId, sTitle, sYear)
        oGui.setEndOfDirectory()
        return


def showMovieGenres():
    showGenres(URL_MAIN + 'filmsenstreaming/', '')


def showSerieGenres():
    showGenres(URL_MAIN + 'seriesenstreaming/', '-s')


def showGenres(urltype, s):
    oGui = cGui()

    liste = []
    listegenre = ['action', 'animation', 'aventure', 'biopic', 'comedie', 'drame', 'documentaire', 'epouvante-horreur',
                  'espionnage', 'famille', 'fantastique', 'guerre', 'historique', 'policier', 'romance',
                  'science-fiction', 'thriller', 'western']

    # https://www.filmoflix.net/filmsenstreaming/action/
    # https://www.filmoflix.net/seriesenstreaming/action-s/

    for igenre in listegenre:
        liste.append([igenre.capitalize(), urltype + igenre + s + '/'])

    oOutputParameterHandler = cOutputParameterHandler()
    for sTitle, sUrl in liste:
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sTmdbId, sTitle, sYear, sSearch=''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    siteUrl = oInputParameterHandler.getValue('siteUrl')
    # sYear = oInputParameterHandler.getValue('sYear')
    # sTitle = oInputParameterHandler.getValue('sTitle')
    if not sTmdbId:
        sTmdbId = oInputParameterHandler.getValue('sTmdbId')
    oOutputParameterHandler = cOutputParameterHandler()  # Define oOutputParameterHandler
    VSlog(sYear)
    if sTmdbId:
        VSlog("--------------------------sTmdbId")
        VSlog(sTmdbId)
        oOutputParameterHandler.addParameter('sTmdbId', sTmdbId)  # Utilisé par TMDB
    if sYear:
        
        oOutputParameterHandler.addParameter('sYear', sYear)  # Utilisé par TMDB
    VSlog("sTitle")
    VSlog(sTitle)
    if sTitle:
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)

    sUrl = URL_MAIN

    sUrl += '&sMedia=film'
    if sYear:
        sUrl += '&sYear=' + sYear
    if sTmdbId:
        sUrl += '&idTMDB=' + sTmdbId
        sUrl += '&sRes=4k'
    sUrl += '&sTitle=' + sTitle
        
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    sDisplayTitle = sTitle
    oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, 'films.png', '', '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
    
# def showHosters(sTmdb):
#     VSlog("showHosters")
#     VSlog("sTmdb")
#     VSlog(sTmdb)
#     oGui = cGui()
#     # oInputParameterHandler = cInputParameterHandler()
#     VSlog("oInputParameterHandler")
#     # sYear = oInputParameterHandler.getValue('sYear')
#     # sTitle = oInputParameterHandler.getValue('sMovieTitle').replace(' | ', ' & ')
#     # siteUrl = oInputParameterHandler.getValue('siteUrl')
    
#     oOutputParameterHandler = cOutputParameterHandler()
    
#     # sTmdbId = oInputParameterHandler.getValue('sTmdbId')
    
    
#     # oOutputParameterHandler.addParameter('sYear', "str(sYear)")
#     #Source JYA
#     oOutputParameterHandler.addParameter('sRes', '4K')
#     oOutputParameterHandler.addParameter('sMovieTitle', "sTitle")
#     oOutputParameterHandler.addParameter('sTmdbId', "sTmdbId")
#     #Important pour marquer vu / progression
#     oOutputParameterHandler.addParameter('siteUrl', "siteUrl")
#     sDisplayName = "JYA"
#     oGui.addLink(SITE_IDENTIFIER, 'showMovies', sDisplayName, 'host.png', '', oOutputParameterHandler)
#     oGui.setEndOfDirectory()


def showHosters():
    VSlog("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
    oHosterGui = cHosterGui()
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    
    sTmdbId = oInputParameterHandler.getValue('sTmdbId')
    sTitle = oInputParameterHandler.getValue('sTitle')
    sYear = oInputParameterHandler.getValue('sYear')
    
    sThumb = ''
    
    VSlog("id_tmdb")
    # VSlog(sSearch)
    # progress_ = progress()

    # progress_ = progress().VScreate(SITE_NAME)
    # progress_.VSupdate(progress_, 100)
    params = f'tmdbid={sTmdbId}'
    VSlog(URL_SEARCH[0])
    oRequest = cRequestHandler(URL_SEARCH[0])
    oRequest.setRequestType(0)
    oRequest.addParametersLine(params)

    res = oRequest.request()

    jsonRes = json.loads(res)
    
    VSlog(jsonRes)
    l_magnets_infos = jsonRes['data']['links']
    
    
    total = len(l_magnets_infos)
    
    oOutputParameterHandler = cOutputParameterHandler()
    
    
    
    VSlog("sYear")
    VSlog(sYear)
    
    for torrents_infos in l_magnets_infos:
        if 'filename' in torrents_infos:
            torrent_title = torrents_infos['filename']
            filesize = torrents_infos['filesize']
            movie_link = torrents_infos['link']
            title = torrents_infos['title']
            release_year = torrents_infos['release_year']
            VSlog("release_year")
            VSlog(release_year)
        # progress_.VSupdate(progress_, total)
        oHoster = oHosterGui.checkHoster(movie_link)
        
        if not sYear or len(sYear) == 0:
            sYear = release_year
        if torrent_title != '':
            sCleanReleaseName = getCleanReleaseNameByUrl(torrent_title)
        else:
            sCleanReleaseName = getCleanReleaseNameByUrl(movie_link)
        if not sTitle:
            sTitle = title
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sTmdbId', sTmdbId)
        oOutputParameterHandler.addParameter('sYear', str(sYear))
        oOutputParameterHandler.addParameter('siteUrl', "siteUrl")
        
        VSlog(oOutputParameterHandler.getParameterAsUri())
        sDisplayName = sTitle +' ('+release_year+') '
        sDiplaySize = ''
        sSizeGo = str(round( filesize / 1_073_741_824,1 ))
        sDiplaySize = sSizeGo+'Go'
        sDisplayName = sDisplayName +'['+sDiplaySize+']'
        oHoster.setSize(filesize)
        oHoster.setDisplayName(sDisplayName)
        oHoster.setFileName(sTitle)
        oHoster.setReleaseName(sCleanReleaseName)
        oHoster.setVideoStreamDetail(getVideoStreamDetail(sCleanReleaseName))
        oHoster.setAudioStreamDetail(getAudioStreamDetail(sCleanReleaseName))
        oHosterGui.showHoster(oGui, oHoster, movie_link, sThumb)
        
    # progress_.VSclose(progress_)
    
    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('sMovieTitle', "sTitle")
    # oOutputParameterHandler.addParameter('sTmdbId', "sTmdbId")
    # oOutputParameterHandler.addParameter('siteUrl', "siteUrl")
    # sDisplayName = "test"
    
    # oGui.addLink(SITE_IDENTIFIER, 'showJYAlink2', sDisplayName, 'host.png', '', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()


def getCleanReleaseNameByUrl(sHosterUrl):
    sReleaseName = sHosterUrl.split('/')[-1]
    sReleaseName = Unquote(sReleaseName)
    sOriginalReleaseName = sReleaseName
    # regex pour garder seulement ce qu'il y a après la date
    dateEpisodesPattern = r"(?:(?!1080|2160)\d{4}|S\d{1,2}E\d{1,2})(?:[\s.()\[\]-]*)(.*)"
    match = re.search(dateEpisodesPattern, sReleaseName)
    if match:
        sReleaseName = match.group(1).strip()
    # regex pour retirer l'id TMDB du film
    tmPattern = r"TM\d+TM"
    sReleaseName = re.sub(tmPattern, '', sReleaseName)
    # On retire les '.mkv', on garde les .mp4
    sReleaseName = re.sub(r'.mkv', '', sReleaseName)
    # On retire les points + espaces en fin de nom
    sReleaseName = re.sub(r'[.\s]+$', '', sReleaseName)
    if len(sReleaseName) < 20:
        sReleaseName = sOriginalReleaseName+" "
    return sReleaseName


def getVideoStreamDetail(sCleanReleaseName):
    videoStreamDetail = {}
    hdrType = None
    videoCodec = None
    aspectRatio = 2.38
    dolbyvision_words = ['dv', 'dovi', 'dolbyvision']
    hdr10plus_words = ['hdr10+', 'hdr10p']
    sLowerCleanReleaseName = sCleanReleaseName.lower()
    uhd_words = ['uhd', '4k', '2160']
    fhd_words = ['1080', 'fhd', 'fullhd', 'full hd', 'full-hd']
    if any(word in sLowerCleanReleaseName for word in uhd_words):
        width = 3840
        height = 2160
    elif any(word in sLowerCleanReleaseName for word in fhd_words):
        width = 1920
        height = 1080
    elif '720' in sLowerCleanReleaseName:
        width = 1280
        height = 720
    else:
        width = 0
        height = 0
    videoStreamDetail['width'] = width
    videoStreamDetail['height'] = height
    if any(word in sLowerCleanReleaseName for word in dolbyvision_words):
        hdrType = 'dolbyvision'
    elif any(word in sLowerCleanReleaseName for word in hdr10plus_words):
        hdrType = 'hdr10'
    elif 'hdr' in sLowerCleanReleaseName:
        hdrType = 'HDR'
    if hdrType is not None :
        videoStreamDetail['hdrtype'] = hdrType
    h265_words = ['h265','x265','hevc']
    h264_words = ['h264','x264','avc']
    if any(word in sLowerCleanReleaseName for word in h265_words):
        videoCodec = 'h265'
    elif any(word in sLowerCleanReleaseName for word in h264_words):
        videoCodec = 'h264'
    if videoCodec is not None :
        videoStreamDetail['codec'] = videoCodec
        videoStreamDetail['aspect'] = aspectRatio
    return videoStreamDetail

def getAudioStreamDetail(sCleanReleaseName):
    sLowerCleanReleaseName = sCleanReleaseName.lower()
    language = ''
    audioCodec = ''
    channels = 0
    if '7.1' in sLowerCleanReleaseName:
        channels = 8
    elif '5.1' in sLowerCleanReleaseName or '6ch' in sLowerCleanReleaseName:
        channels = 6
    vff_words = ['vff', 'vfi', 'vfo', 'vof', 'vf2', 'truefrench', 'true french']
    if any(word in sLowerCleanReleaseName for word in vff_words):
        language = 'fr'
    dtshdma_words = ['hdma','dtshd','dts.hd','dts-hd']
    eac3_words = ['eac3','dd+','ddp']
    truehd_words = ['thd','truehd','true-hd','true.hd','truhd']
    dtsx_words = ['dts-x','dtsx','dts:x']
    if any(word in sLowerCleanReleaseName for word in dtshdma_words):
        audioCodec = 'dtshdma'
    elif any(word in sLowerCleanReleaseName for word in dtsx_words):
        audioCodec = 'dtsx'
    elif any(word in sLowerCleanReleaseName for word in truehd_words):
        audioCodec = 'truehd'
    elif any(word in sLowerCleanReleaseName for word in eac3_words):
        audioCodec = 'eac3'
    elif 'ac3' in sLowerCleanReleaseName:
        audioCodec = 'ac3'
    audioStreamDetail = {'codec': audioCodec, 'channels':channels, 'language':language}
    return audioStreamDetail


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = 'navigation.+?<span>\d+</span> <a href="([^"]+).+?>([^<]+)</a></div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        sNextPage = aResult[1][0][0]
        sNumberMax = aResult[1][0][1]
        sNumberNext = re.search('page/([0-9]+)', sNextPage).group(1)
        sPaging = sNumberNext + '/' + sNumberMax
        return sNextPage, sPaging

    return False, 'none'


def showSaisons():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = 'property="og:description".+?content="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sDesc = 'FilmoFlix'
    if aResult[0]:
        sDesc = ('[I][COLOR grey]%s[/COLOR][/I] %s') % ('Synopsis : ', aResult[1][0])

    sPattern = 'th-item">.+?href="([^"]*).+?src="([^"]*).+?title.+?>([^<]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in reversed(aResult[1]):

            sUrl2 = aEntry[0]
            sThumb = aEntry[1]
            if 'http' not in sThumb:
                sThumb = URL_MAIN[:-1] + sThumb
            sSaison = aEntry[2]  # SAISON 2

            sTitle = ("%s %s") % (sMovieTitle, sSaison)

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)

            oGui.addSeason(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    else:
        oGui.addText(SITE_IDENTIFIER)

    oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sStart = 'class="saisontab'
    sEnd = 'class="clearfix'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = 'href="([^"]+).+?fsa-ep">([^<]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sUrl2 = aEntry[0]
            sEpisode = aEntry[1].replace('é', 'e').strip()  # épisode 2
            if 'http' not in sUrl2:
                sUrl2 = URL_MAIN[:-1] + sUrl2
            sTitle = sMovieTitle + ' ' + sEpisode

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addEpisode(SITE_IDENTIFIER, 'showSerieLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    else:
        oGui.addText(SITE_IDENTIFIER)

    oGui.setEndOfDirectory()


def showSerieLinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')

    oParser = cParser()
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    cook = oRequestHandler.GetCookies()

    sPattern = "class=\"lien.+?playEpisode.+?\'([^\']*).+?'([^\']*)"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            videoId = aEntry[0]
            xfield = aEntry[1]
            hosterName = xfield.replace('_', ' ').capitalize().replace('vf', '(VF)').replace('vostfr', '(VOSTFR)')

            postdata = 'id=' + videoId + '&xfield=' + xfield + '&action=playEpisode'
            sUrl2 = URL_MAIN + 'engine/ajax/Season.php'

            sDisplayTitle = ('%s [COLOR coral]%s[/COLOR]') % (sTitle, hosterName)

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('referer', sUrl)
            oOutputParameterHandler.addParameter('cook', cook)
            oOutputParameterHandler.addParameter('postdata', postdata)

            oGui.addLink(SITE_IDENTIFIER, 'showSerieHosters', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSerieHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    referer = oInputParameterHandler.getValue('referer')
    # cook = oInputParameterHandler.getValue('cook')
    postdata = oInputParameterHandler.getValue('postdata')

    oRequest = cRequestHandler(sUrl)
    oRequest.setRequestType(1)
    oRequest.addHeaderEntry('Referer', referer)
    oRequest.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
    # oRequest.addHeaderEntry('Cookie', cook) # pas besoin ici mais besoin pour les films
    oRequest.addParametersLine(postdata)
    sHtmlContent = oRequest.request()

    oParser = cParser()
    sPattern = '<iframe src=\'([^\']+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        sHosterUrl = aResult[1][0]
        oHoster = cHosterGui().checkHoster(sHosterUrl)
        if oHoster:
            oHoster.setDisplayName(sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()


def showMovieLinks():

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sYear = oInputParameterHandler.getValue('sYear')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    cook = oRequestHandler.GetCookies()

    oParser = cParser()
    sPattern = 'text clearfix">([^<]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sDesc = 'FilmoFlix'
    if aResult[0]:
        sDesc = ('[I][COLOR grey]%s[/COLOR][/I] %s') % ('Synopsis : ', aResult[1][0])
    sStart = '<ul class="player-list">'
    sEnd = '<div class="clearfix"></div>'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)
    sPattern = "lien fx-row.+?\"getxfield.+?(\d+).+?\'([^\']*).+?'([^\']*).+?images.([^\.]+).+?pl-5\">([^<]+)"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            videoId = aEntry[0]
            xfield = aEntry[1]
            token = 'undefined'
            # images :aEntry[3] (VF).png
            sQual = aEntry[2]
            hosterName = xfield.replace('_', ' ').capitalize().replace('vf', '(VF)').replace('vostfr', '(VOSTFR)')

            sUrl2 = URL_MAIN + 'engine/ajax/getxfield.php?id=' + videoId + '&xfield=' + xfield + '&token=' + token

            sDisplayTitle = ('%s [%s] [COLOR coral]%s[/COLOR]') % (sTitle, sQual, hosterName)

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('referer', sUrl)
            oOutputParameterHandler.addParameter('cook', cook)
            oGui.addMovie(SITE_IDENTIFIER, 'showMovieHosters', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovieHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    referer = oInputParameterHandler.getValue('referer')
    cook = oInputParameterHandler.getValue('cook')

    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('Referer', referer)
    if cook:
        oRequest.addHeaderEntry('Cookie', cook)
    sHtmlContent = oRequest.request()

    oParser = cParser()
    sPattern = '<iframe.+?replace\("([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:
        sHosterUrl = aResult[1][0]
        oHoster = cHosterGui().checkHoster(sHosterUrl)
        if oHoster:
            oHoster.setDisplayName(sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()