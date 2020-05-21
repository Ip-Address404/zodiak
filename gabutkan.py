try:
	import requests, os, json
except ModuleNotFoundError:
	print("\033[1;31m\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

os.system('clear')
banner=("""\033[1;36m
     _  _
   _| || |_  \033[1;32mINFO TANGGAL LAHIR & ZODIAK\033[1;36m
  |_  ..  _|
  |_      _| \033[1;31mEmail =>saputra230622@gmail.com\033[1;36m
    |_||_|   \033[1;31mGithub=>https://github.com/Ip-Address404
  \033[1;36mFDM:  \033[1;31mBastianSaputra
""")
def no():
	try:
		print(banner)
		nama = input("\033[1;37mNama Anda =>\033[1;32m")
		tgl = input("\033[1;37mTanggal Lahir(ex:23 06 2002) =>\033[1;32m").replace(' ','-')
		r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama='+nama,'&tanggal='+tgl)
		jsn = json.loads(r.text)
		a = jsn['data']
		print('''
	****************************************
	Nama kamu      : {}
	Tanggal lahir  : {}
	Umur           : {}
	Ultahmu kurang : {}
	Zodiak         : {}
	****************************************
	'''.format(a['nama'],a['lahir'],a['usia'],a['ultah'],a['zodiak']))
	except:
		exit("\033[1;31mFormat Yang Anda Masukan Salah\n")
tanya = 'y'
while (tanya != 'n'):
	no()
	tanya=input("[?] Lagi (y/n) ")
	if tanya == 'n':
		print("oke, sampai jumpa:* ")
