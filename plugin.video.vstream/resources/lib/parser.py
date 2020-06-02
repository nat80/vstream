# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons

import re


class cParser:

    def parseSingleResult(self, sHtmlContent, sPattern):
        aMatches = re.compile(sPattern).findall(sHtmlContent)
        if (len(aMatches) == 1):
            aMatches[0] = self.__replaceSpecialCharacters(aMatches[0])
            return True, aMatches[0]
        return False, aMatches

    def __replaceSpecialCharacters(self, sString):
        """ /!\ pas les mêmes tirets, tiret moyen et cadratin. Puis on supprimme le tiret pour les séries """
        return sString.replace('\r', '').replace('\n', '').replace('\t', '').replace('\\/', '/').replace('&amp;', '&')\
                      .replace('&#039;', "'").replace('&#8211;', '-').replace('&#038;', '&').replace('&rsquo;', '\'')\
                      .replace('\xc9', 'E').replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<')\
                      .replace('&nbsp;', '').replace('–', '-').replace('—', '-').replace(' - Saison', ' Saison')

    def parse(self, sHtmlContent, sPattern, iMinFoundValue=1):
        sHtmlContent = self.__replaceSpecialCharacters(str(sHtmlContent))
        aMatches = re.compile(sPattern, re.IGNORECASE).findall(sHtmlContent)
        if (len(aMatches) >= iMinFoundValue):
            return True, aMatches
        return False, aMatches

    def replace(self, sPattern, sReplaceString, sValue):
        return re.sub(sPattern, sReplaceString, sValue)

    def escape(self, sValue):
        return re.escape(sValue)

    def getNumberFromString(self, sValue):
        sPattern = '\d+'
        aMatches = re.findall(sPattern, sValue)
        if (len(aMatches) > 0):
            return aMatches[0]
        return 0

    def titleParse(self, sHtmlContent, sPattern):
        sHtmlContent = self.__replaceSpecialCharacters(str(sHtmlContent))
        aMatches = re.compile(sPattern, re.IGNORECASE)
        try:
            [m.groupdict() for m in aMatches.finditer(sHtmlContent)]
            return m.groupdict()
        except:
            return {'title': sHtmlContent}

    def abParse(self, sHtmlContent, start, end, startoffset=''):
        # usage oParser.abParse(sHtmlContent, 'start', 'end')
        # startoffset (int) décale le début pour ne pas prendre en compte start dans le résultat final si besoin
        # usage2 oParser.abParse(sHtmlContent, 'start', 'end', 6)
        # ex youtube.py
        if startoffset:
            return sHtmlContent[startoffset + sHtmlContent.find(start):sHtmlContent.find(end)]
        else:
            return sHtmlContent[sHtmlContent.find(start):sHtmlContent.find(end)]
