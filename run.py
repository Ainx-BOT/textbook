import os,sys,time,requests,json
from time import sleep
from colorama import init, Fore, Back
B = Fore.BLUE
W = Fore.WHITE
C = Fore.CYAN
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
M = Fore.MAGENTA
BL = Fore.BLACK
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def back():
    input(W+"["+Y+" Press Enter To Back"+W+" ]")
    sleep(1)
    os.system("python run.py")
def failed():
    print(R+"[×]"+W+" No Output"+R+"!!"+W)
    back()
def baner():
    print(f"""
{M}╔╦╗{W}┌─┐─┐ ┬┌┬┐{M}╔╦╗{W}┌─┐{M}╦{W}┌┬┐┌─┐┌─┐┌─┐
{M} ║ {W}├┤ ┌┴┬┘ │ {M} ║ {W}│ │{M}║{W}│││├─┤│ ┬├┤ 
{M} ╩ {W}└─┘┴ └─ ┴ {M} ╩ {W}└─┘{M}╩{W}┴ ┴┴ ┴└─┘└─┘""")
    print(Back.WHITE+BL+"      Creator : Fahmi Dev       \033[00m")
def tulis(kata):
    data={"text":kata}
    req=requests.get("https://ainxbot-id.herokuapp.com/api/nulis",params=data).text
    if "Success" in req:
        print(W+"["+G+"✓"+W+"]Tulisan Berhasil Di Convert Ke Gambar Buku")
        js=json.loads(req)
        url=js["result"]["url_image"]
        os.system("termux-open "+x)
    else:
        failed()
if __name__=="__main__":
     clear()
     baner()
     kata=input(W+"["+M+"?"+W+"]Tulisan : "+M)
     tulis(kata)
     back()
