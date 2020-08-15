#!/usr/bin/python2

# Creator :  MR.CRACKED
# Team : Mahiska Cyber Team( MCT )
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3
# :v

from requests.exceptions import ConnectionError
import requests
import random
import time
import sys
import os

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def banner():
	print(''+C+'''
     _         _         __     ___     _ _             
    / \  _   _| |_ ___   \ \   / (_)___(_) |_ ___  _ __ 
   / _ \| | | | __/ _ \   \ \ / /| / __| | __/ _ \| '__|
  / ___ \ |_| | || (_) |   \ V / | \__ \ | || (_) | |   
 /_/   \_\__,_|\__\___/     \_/  |_|___/_|\__\___/|_|      
                   '''+W+'Creator : Mr.Cracked\n\t\t   YT : MR CRACKED')
                   
def main():
	success = []
	gagal = []
	user_agent = requests.get('https://pastebin.com/raw/zkCXTGcm').text.split('\n')
	wkwk = random.choice(user_agent)
	headers = {
	'User-Agent' : '{wkwk}',
	'Connection' : 'keep-alive',
	'Accept' : 'image/webp,image/apng,image/*,*/*;q=0.8', 
	'Content-Type' : 'text/html; charset=UTF-8',
	'Proxy-Connection' : 'keep-alive',
	'Accept-Encoding' : 'gzip, deflate',
	'X-Requested-With' : 'XMLHttpRequest',
	}
	os.system('clear')
	os.system('xdg-open https://www.youtube.com/channel/UCP_pGBqwyn-Tu2Fh1vh1umQ')
	c = 0
	banner()
	print
	print
	f = raw_input(''+C+'MASUKKAN SITE'+W+' ('+H+' Ex : '+C+'https://www.site.com '+W+') : ')
	u = input(''+C+'JUMLAH VISITOR'+W+' ('+H+' Ex : '+C+'100 '+W+') : ')
	print
	print(''+C+'-------------- '+W+'Starting'+C+' --------------')
	print
	
	for i in range(u):
		try:
			if not f.startswith('http'):
				print(M+'Gunakan Http / Https !')
				break
			k = requests.get('{}'.format(f), headers=headers)
			c += 1
			q = success
			g = gagal
			if k.status_code < 200 or k.status_code <= 201:
				print(''+C+'Visitor Ke ' + W + str(c) + H + ' Success' + C + ' Dikirimkan')
				success.append(q) 
				
			else:
				print(''+C+'Visitor Ke ' + W + str(c) + A + ' Gagal' + C + ' Dikirimkan')
				gagal.append(g)
				
		except ConnectionError:
			print
			print(M+'Koneksi Error / Terjadi Kesalahan !')
			break
	
	print
	print(''+C+'----------- '+W+'Selesai & Hasil'+C+' -----------')
	h = (len(success))
	l = (len(gagal))
	print
	print(''+C+'Hasil Success : '+W+str(h))
	print(''+C+'Hasil Gagal : '+W+str(l))
	
	
	
if __name__ == '__main__':
	main()
			