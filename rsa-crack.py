import requests
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
from Crypto.Util.number import inverse, long_to_bytes

BANNER = """
#----------------------------------------------
# 
#               \   $    $   / 
#                \          /
#                 \        /
#                  \      /
#                   \    /
#                    \  /
#                     \/
# RSA cracker tool for CTF's using factordb.com
#             [ Create by t1m0 ]
# 
#----------------------------------------------


"""
print(BANNER)
c = int(input("Enter c : "))
n = int(input("Enter n : "))
e = int(input("Enter e : "))

url = "https://factordb.com/index.php"
params = {"query": n}
r = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
html = r.text
soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")



def function() :
    if len(links) >= 13:
        p = int(links[11].get_text())
        q = int(links[12].get_text())

        phi = (p - 1) * (q - 1)
        d = inverse(e, phi)
        m = pow(c, d, n)
        
        print("\n")
        print("   p =", p,"\n")
        print("   q =", q,"\n")
        print("   d =", d,"\n")
        print("   m =", m,"\n")
        print(Fore.GREEN + "   result =", long_to_bytes(m).decode(),"\n\n")

    else:
        print(Fore.RED + "Error: can't factorize")
  
  
function()
