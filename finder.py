import os,sys,requests,json
from termcolor import cprint

os.system('clear')

cprint ('       db888888888db','red')
cprint ('     88            88','red')
cprint ('    88              88','red')
cprint ('   00     Finder     00','red')
cprint ('    11              11','red')
cprint ('      88           88','white')
cprint ('         88     88','white')
cprint ('           8888','white')
cprint ('            db','white')
print
cprint ('        [ Finder ]','yellow')
cprint ('   [ Coded By : RafiXP ]','yellow')
print
ip=raw_input('Input IP Target : ')

url="http://ipwhois.app/json/"

req=requests.get(url+ip)
x = json.loads(req.text)
link ="https://maps.google.com/?q="
lin =x["latitude"]
buj =x["longitude"]

print
print "IP Address    : ", x["ip"]
print "Status        : ", x["success"]
print "IP Type       : ", x["type"]
print "Kontinen      : ", x["continent"]
print "Kode Kontinen : ", x["continent_code"]
print "Negara        : ", x["country"]
print "Wilayah       : ", x["region"]
print "Kota          : ", x["city"]
print "Kode Negara   : ", x["country_code"]
print "Kapital       : ", x["country_capital"]
print "Kode Telepon  : ", x["country_phone"]
print "ASN           : ", x["asn"]
print "Organisasi    : ", x["org"]
print "ISP           : ", x["isp"]
print "Zona Waktu    : ", x["timezone"]
print "GMT           : ", x["timezone_gmt"]
print "Mata Uang     : ", x["currency"]
print "Satuan Uang   : ", x["currency_code"]
print "Simbol        : ", x["currency_symbol"]
print "Garis Lintang : ", x["latitude"]
print "Garis Bujur   : ", x["longitude"]
print "Link Google   : ",link+lin,buj
print
sys.exit(1)
