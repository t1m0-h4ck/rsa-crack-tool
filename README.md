# rsa-crack-tool
My first RSA cracking tool in python  

Recently, I used a Python tool that allowed me to break weak RSA, which is very useful in CTFs (Capture The Flag).  
The main limitation of RSA is that it cannot be broken unless the modulus N is small enough to be factored.  
While modern computers can perform millions of arithmetic operations, factoring large integers is computationally infeasible.  
However, CTF challenges usually provide RSA instances with a weak or malformed modulus, making them crackable in a few seconds.

So I decided to create my first Python tool designed to break weak RSA.  
It uses the Requests library to send HTTP requests to factordb.com, a site capable of factoring vulnerable RSA moduli.  
The script also uses PyCryptodome for all mathematical operations, and BeautifulSoup to parse the HTML response and extract the values of p and q.

How to run the script:

1. Make sure you have installed the required libraries:
   requests, colorama, beautifulsoup4, and pycryptodome:
   pip install requests colorama beautifulsoup4 pycryptodome

2. Open your terminal and navigate to the folder where the script is located.

3. Run the script using:
   python rsa-crack.py
   or
   python3 rsa-crack.py

You're now ready for your CTFs!

