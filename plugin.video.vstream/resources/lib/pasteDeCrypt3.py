# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: C:\dev\Crypt\pasteCrypt.py
# Bytecode version: 3.8.0rc1+ (3413)
# Source timestamp: 2023-10-24 22:25:23 UTC (1698186323)
 
import requests
import re
import random
from resources.lib.comaddon import addon
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.util import cUtil

try:
    from html.parser import HTMLParser
    py3 = True
    unicode = str
except ImportError:
    py3 = False
 
class Crypt:
 
    def __init__(self):
        self.s = 'chmo.:ABCDEGIKLMNOPRSTUWYbpstux'
        self.tabKey = ['Wq97wQmdlPOJBGvNnbxcDHzFj2gkYURftEKV163A5MeSp0r8IXoZTyiuCLh4as', 'KdSiCM8nf9tIbwDzH04X325O67mRuBFNWkQvVTEcpexGy1agZYqAPLsUolJjrh', '9Y6kURti4gzhCIGwZM0PpBXuoVcl3e5Ky7fNFSTjms8AbHErxWDO2dnLaJQvq1', 'AfEeszp0ZRgJuqtyGOokvFjhHPrVb4cB2NIXnU6KxaS8dlQ57TLCi39wMWY1Dm', 'yBhlVjFDA1EKYuoGZ2NqnxUesdMS3Ofp0arzwtRIc8kb9JPQ4WH5Tvg6iCX7mL', 'wTfLtya01MnzeYSW9d4FoHcNkJZCvXQ3bgiGpEu825RrjP7OVKUxDqAIlsBh6m', 'ButrYenv6fX9NmCUI3Rs2V7hTAWHDkKglLc50jFQOpSPqy8w1EiZ4abJGodMzx', '2gcSr0w8YeiXM4sAd6uxthnbqJ9BpQO7ZzKG3HTFUIVjlkEvL1oWRNmDyC5afP', 'R3ExPNnUhDyujmK4LAMVd52vIZtplqiHragzoekJ1TSb9W6GcOYfFBC0X87Qsw', 'ZgtAmxakYKD0zpcsqLT9wHndP5B4Ir2huCRFQfb8M67UlVN3eGyvOEjWSJoiX1', 'YZt86WeN3ECKHA1x9vdhF4jzISL2RGurgpPsDwlJ7n0mOaBoyMUVcfib5TkXqQ', 'uhl8iYHO6poTIvgDQ904PayfcrZ1J5zkmREFLVqBsUdNMxj7XCnGwtbW3AeKS2', 'VaU8utB2lSwpNq0yHhF7RMTJncDbIZYXs9dAiCzmj613QxOEW4PgfGL5oKvrek', 'zOFWr7JetVh0yN6vslDxn24fwHukXmEUj5qCSTRbgiYQPIZAM1aGL9dB8oKc3p', 'kM1AUuqnNfrKWRj0tOzm7C9lYShZGcQBL5J4DyF3wXT2aEd8VvoPHpbiexgsI6', '9HYjEcLTutQpI0rO3M75ZvwA4GFK2koqzhUiCny6xNSdmRfJegDaVBXbs1PW8l', '0UScdanhjeNVLrFXpx3wOD7ikZ4PBsmzJM8QI5RoyqWAtfEvY1l926TuHKCgGb', 'Bb3cNFeDkW5fwvVJm2QzgPiUL9nTZE4apdMSIqHhlxYrjC0AoK81uXRsOtGy76', 'n4tmQckyLRd13vPebl9EzhBa0MKXGj7NUf26CH8r5AFYWOopuxSDZwsiVIqJgT', 'ceQ68PDBs4huny23trq7ClvFWiAKHzZ1bgURwo9pXIOxdLNYVSkEfa0GJ5jmMT', 'jxMyhCUpStFgzs81lBvrXEOHAK6PbwiRDNd4ZTJ2oI03Lk9mucaY5V7WnQefGq', 'j4vcoE9lfpNwTsiDRQCdUbYu5k28JBWH7SeZrqyh3L6PxKGAXVOnm1tFIMazg0', 'Xk4teWwfzEBR9bHuUZoJ3Y0NxQO8phmGT1aFiyncj7KLqvPIrAlDsSC256dgVM', 'mWKyZVEilfpHD752LJRGvQuqIe0MawOnP81BFz69khdCSUsXjc4NYg3xrtboTA', '8LzXWwKhl2oGdTYAM6yIaJ3bBce4fsg9rUuQktCxpi7VD0OZPnvFNSEHqmRj15', 'kopQbKsUMz4FCn0aqwyNAc23DlET7GWSfmd1IHO8PtevxrV6ZLghjYRXBJu5i9', 'rz5wTkpAKgYH32OuRl4nD0yNQva186FM7eJiScBIXhbVsdUE9oGqxPCtjLmWfZ', 'H5KQUnLCvgWSYOka3PFAjhJ0cw61z2yR8tqmMXIlsupeZfoVNxT74EirdbDBG9', 'zvlEitNwd0bPqasYDArjgnJKIOoCSp589mM2TFy6WZk1RuxGBQL3hX7cHfeVU4', 'd5hjmCsA34nZu9pV76Sbz1NRYO8iFGlTLcMqUxHBgKvofXawDytIkeEWQPrJ02']
        self.numRot = 0
        self.posTable = 0
        self.adrPbi = 'https://anotepad.com/note/read/%s'
        self.adrPbi2 = 'https://rentry.co/%s/raw'
        self.motifAnotepad = '.*<div class="plaintext *">(?P<txAnote>.+?)</div>.*'
 
    def loadFile(self, numPaste):
        num = self._decryptNumPaste(numPaste)
        posDecal = self._numDecal(num)
        oRequestHandler = cRequestHandler(self.adrPbi % num)
        oRequestHandler.setTimeout(5)
        oRequestHandler.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        sContent = oRequestHandler.request()
        r = re.match(self.motifAnotepad, sContent, re.MULTILINE | re.DOTALL)
        if not r:
            return []
        try:
            tx = r.group('txAnote')
            if not py3:
                tx = unicode(tx, 'utf-8')
            tx = cUtil().unescape(tx)
            lignes = self._decrypt(tx, posDecal)
        except Exception as e:
            lignes = []
        return lignes
 
    def _revBit(self, n):
        low = n & 15
        high = n >> 4
        return low * 16 + high ^ 255
 
    def _numDecal(self, num):
        v1 = sum([ord(x) for x in num])
        v1 = self._revBit(v1) % 70
        return v1
 
    def cryptNumPaste(self, cr):
        rot = random.randint(1, 15)
        tx = self.tabKey[rot - 1]
        txCrypt = ''
        v = 0
        for i, t in enumerate(cr):
            pos = (tx.index(t) + (i + 1) * rot) % len(tx)
            v += ord(tx[pos])
            txCrypt += tx[pos]
        v = self._revBit(v & 255)
        v &= 15
        v ^= rot
        txCrypt += str(hex(v))[2:]
        return txCrypt
 
    def _decryptNumPaste(self, tx2):
        try:
            v = int('0x%s' % tx2[8:], 16)
            tx2 = tx2[:8]
            v1 = sum([ord(x) for x in tx2]) & 255
            v1 = self._revBit(v1)
            v1 &= 15
            rot = v ^ v1
            tx = self.tabKey[rot - 1]
            txdec = ''
            for i, t in enumerate(tx2):
                pos = (tx.index(t) - (i + 1) * rot) % len(tx)
                txdec += tx[pos]
        except:
            txdec = ''
        return txdec
 
    def _cryptDecrypt(self, tx, decal, crypt=1):
        if crypt == 0:
            decal *= -1
        tab = sorted(list(set([x for x in tx])))
        cr = [tab[(tab.index(t) + decal) % len(tab)] for t in tx]
        if not py3:
            return ''.join(cr).encode('utf8')
        return ''.join(cr)
 
    def _decrypt(self, tx, posDecal):
        lignes = [x for x in tx.splitlines() if x]
        if tx[0] == '#':
            return lignes
        tabDecrypt = []
        try:
            for j, ligne in enumerate(lignes):
                if j == 0:
                    ligne = list(ligne)
                    decal = self.s.index(ligne.pop(posDecal))
                    ligne = ''.join(ligne)
                tabDecrypt.append(self._cryptDecrypt(ligne, decal, crypt=0))
        except Exception as e:
            tabDecrypt = []
        return tabDecrypt
 
    def resolveLink(self, numPaste, link, key='', mode=2):
        """mode 0 = alldebrid, mode 1 = realdebrid, 2 = uptobox, 3 = uptostram, 4 = uptobox + uptostream"""
        if not link or (mode > 0 and (not key)):
            return ([], 'err')
        code = link.split('/')[-1]
        url = link.replace(code, '')
        if len(numPaste) == 8:
            num = numPaste
        else:
            num = self._decryptNumPaste(numPaste)
            v1 = sum([ord(x) for x in num]) % len(self.tabKey)
            pos1 = ord(num[0]) % len(self.tabKey[0])
            pos2 = ord(num[1]) % len(self.tabKey[0])
            pos3 = ord(num[2]) % len(self.tabKey[0])
            posRefl = ord(num[3]) % len(self.tabKey[0])
            rot1 = self._swapKey(self.tabKey[v1 % len(self.tabKey)], pos1)
            rot2 = self._swapKey(self.tabKey[(v1 + 1) % len(self.tabKey)], pos2)
            rot3 = self._swapKey(self.tabKey[(v1 + 2) % len(self.tabKey)], pos3)
            rotRefl = self._swapKey(self.tabKey[(v1 + 3) % len(self.tabKey)], posRefl)
            tabRot = [rot1, rot2, rot3]
            reflecteur = {x: rotRefl[-(i + 1)] for i, x in enumerate(rotRefl)}
            code = self._decryptLink(tabRot, reflecteur, code)
        if mode == -1:
            linkF = [(url + code, 'ori', 'ori')]
            status = 'ok'
        elif mode == 0:
            linkF, status = self._linkDownloadAlldebrid(key, url + code)
        elif mode == 1:
            linkF, status = self._linkDownloadRealdebrid(key, url + code)
        else:
            linkF = []
            if mode in [2, 4]:
                links, status = self._linkDownloadUptobox(key, link)
                if links:
                    linkF.extend(links)
            if mode in [3, 4]:
                links, status = self._linkDownloadUptostream(key, link)
                if links:
                    linkF.extend(links)
        return (linkF, status)
 
    def _decryptLink(self, tabRot, reflecteur, link):
        self.numRot = 0
        self.posTable = 0
        fichCr = ''
        alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        for lCr in link:
            for rot in tabRot[::-1]:
                lCr = rot[alpha.index(lCr)]
            lCr = reflecteur[lCr]
            for rot in tabRot:
                lCr = alpha[rot.index(lCr)]
            fichCr += lCr
            tabRot[self.numRot] = self._swapKey(tabRot[self.numRot], 1)
        return fichCr
 
    def _swapKey(self, key, swap):
        self.posTable += 1
        self.posTable %= len(key)
        if self.posTable == 0:
            self.numRot += 1
            self.numRot %= 3
        key = ''.join([key[(i + swap) % len(key)] for i in range(len(key))])
        return key
 
    def _linkDownloadUptobox(self, key, fileCode):
        url1 = 'https://uptobox.link/api/link?token=%s&file_code=%s' % (key, fileCode)
        dlLink = []
        try:
            oRequestHandler = cRequestHandler(url1)
            dict_liens = oRequestHandler.request(jsonDecode=True)
            statusCode = dict_liens['statusCode']
            if statusCode == 0:
                sUrl = dict_liens['data']['dlLink']
                sUrl = sUrl.replace('.com', '.link')
                dlLink = [(sUrl, 'ori', 'ori')]
                status = 'ok'
            elif statusCode == 16:
                status = 'Pas de compte Premium'
            elif statusCode == 7:
                status = dict_liens['data']['message']
                status += ' - ' + dict_liens['data']['data']
            else:
                status = 'Erreur inconnue : ' + str(statusCode)
        except Exception as e:
            dlLink = []
            status = e
        return (dlLink, status)
 
    def _linkDownloadUptostream(self, key, fileCode):
        url1 = 'https://uptobox.link/api/streaming?token=%s&file_code=%s' % (key, fileCode)
        try:
            oRequestHandler = cRequestHandler(url1)
            dict_liens = oRequestHandler.request(jsonDecode=True)
            status = dict_liens['statusCode']
            if status != 0:
                return (None, dict_liens['message'])
            status = 'ok'
            data = dict_liens['data']
            if data['version'] == 1:
                links = data['streamLinks']
                dlLink = [(v1, k, k1) for k, v in links.items() for k1, v1 in v.items()]
            else:
                res = data['max_quality']
                dlLink = [(data['streamLinks']['src'], res, 'ori')]
        except Exception as e:
            dlLink = []
            status = e
        return (dlLink, status)
 
    def _linkDownloadAlldebrid(self, key, lien):
        dlLink = []
        status = 'ok'
        addons = addon()
        urlAD = addons.getSetting('hoster_alldebrid_url')
        if urlAD:
            urlAD = urlAD % (key.strip(), lien)
        else:
            urlAD = 'http://api.alldebrid.com/v4/link/unlock?agent=vStream&apikey=%s&link=%s' % (key.strip(), lien)
        oRequestHandler = cRequestHandler(urlAD)
        dict_liens = oRequestHandler.request(jsonDecode=True)
        try:
            if dict_liens['status'] == 'success':
                dlLink = [(dict_liens['data']['link'], 'ori', 'ori')]
            else:
                status = dict_liens['error']['code']
        except Exception as e:
            status = e
        return (dlLink, status)
 
    def _linkDownloadRealdebrid(self, key, lien):
        headers = {'Authorization': 'Bearer %s' % key}
        data = {'link': lien, 'password': ''}
        r = requests.post('https://api.real-debrid.com/rest/1.0/unrestrict/link', data=data, headers=headers)
        dictData = r.json()
        if 'error' in dictData.keys():
            links, status = ([], 'RealDebrid - ' + dictData['error'].upper().replace('_', ' '))
        else:
            links, status = ([(dictData['download'], 'ori', 'ori')], 'ok')
        return (links, status)