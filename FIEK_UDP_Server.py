import random
import socket
from datetime import datetime
import random
import hashlib , os , binascii
import platform

serverName = ''
serverPort=14000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print('Serveri eshte ekzekutuar ne 127.0.0.1:' + str(serverPort))

def IP():
    return str(address[0])


def NRPORTIT():
    return str(address[1])


def NUMERO(text):
    vowels = ['A', 'a', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    v = 0
    c = 0
    for i in str(text):
        if i in vowels:
            v += 1
        elif (i >= 'a' and i <= 'z') or (i > 'A' and i <= "Z"):
            c += 1

    return "Teksti ka " + str(v) + " zanore dhe " + str(c) + " bashketingellore"


def LOJA():
    arr = (random.sample(range(1, 35), 5))
    arr.sort()
    return str(arr)


def ANASJELLTAS(str):
    s = str.strip()
    reversed = ""
    indeksi = len(s)
    while indeksi > 0:
        reversed += s[indeksi - 1]
        indeksi = indeksi - 1
    return reversed


def PALINDROM(text):
    if (text == text[::-1]):
        return "Fjala " + text.lower() + " eshte palindrom "
    else:
        return "Fjala " + text.lower() + " nuk eshte palindrom "


def GCF(a, b):
    if a % b == 0:
        return b
    return GCF(b, a % b)


def KONVERTO(s, gjatesia):

    s=s.lower()
    if (s == "cmtoinch"):
        return round(gjatesia * 0.393701,2)
    elif (s == "inchtocm"):

        return round(gjatesia * 2.54,2)
    elif (s == "kmtomiles"):

        return round(gjatesia * 0.621371,2)
    elif (s == "milestokm"):
        return round(gjatesia * 1.60934,2)
    else:
        return "Lloji i konvertimit eshte gabim. Termat e sakte : cmtoinch, inchtocm ,kmtomiles dhe milestokm"



def HASHPWD(password):
   
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    string="Salted Hash Paswword "
    return {string: (salt + pwdhash).decode('ascii')}
 

def PLATFORM():

    platformdetails = platform.platform()
    systemname = platform.system()
    proccesorname = platform.processor()
    architecturedetails = platform.architecture()

    return{'platform details':platformdetails,
           'system name':systemname,
           'proccesor name':proccesorname,
           'architecture details':architecturedetails}




def sendRequest(request, conn, addr):
    requestarray = request.upper()
    requestarray = requestarray.split(" ")
    kerkesa1 = request.split(" ")
    if (requestarray[0] == 'IP'):
        if len(requestarray) == 1:
            var = IP()
            serverSocket.sendto(str.encode('IP Adresa e klientit eshte:' + var),addr)
        else:
            serverSocket.sendto(str.encode("Metoda IP nuk ka parametra"),addr)
    elif (requestarray[0] == 'NRPORTIT'):
        if len(requestarray) == 1:
            var = NRPORTIT()
            serverSocket.sendto(str.encode("Klienti eshte duke perdorur portin " + NRPORTIT()),addr)
        else:
            serverSocket.sendto(str.encode("Metoda NRPORTIT nuk ka parametra"),addr)
    elif (requestarray[0] == 'NUMERO'):
        if len(requestarray) == 1:
            serverSocket.sendto(str.encode("Metoda Numero ka argument tekstin pas saj"),addr)
        else:
            s = requestarray[1:]
            serverSocket.sendto(str.encode(str(NUMERO(s))),addr)
    elif (requestarray[0] == 'ANASJELLTAS'):
        if len(requestarray) == 1:
            serverSocket.sendto(str.encode("Metoda Anasjelltas ka argument tekstin pas saj"),addr)
        else:
            s = request[len(requestarray[0]):]
            serverSocket.sendto(str.encode((ANASJELLTAS(str(s)))),addr)
    elif (requestarray[0] == 'GCF'):
        if len(requestarray) == 1:
            serverSocket.sendto(str.encode("Metoda GCF duhet te permbaje 3 argumente"),addr)
        elif len(requestarray) == 3:
            if requestarray[1].isdigit() and requestarray[2].isdigit():
                nr1 = int(requestarray[1])
                nr2 = int(requestarray[2])
                serverSocket.sendto(str.encode(str(GCF(nr1, nr2))),addr)
            else:
                serverSocket.sendto(str.encode("Metoda GCF duhet te permbaje ne 2 argumentet e fundit vetem numra"),addr)

        else:
            serverSocket.sendto(str.encode("Metoda GCF duhet te kete 2 numra si argumenta"),addr)
    elif (requestarray[0] == 'PALINDROM'):
        if len(requestarray) != 2:
            serverSocket.sendto(str.encode("Metoda Palindrom ka argument tekstin pas saj"),addr)
        else:
            s = requestarray[1]
            k = PALINDROM(s)
            serverSocket.sendto(str.encode(str(k)),addr)
    elif (requestarray[0] == 'KOHA'):
        if len(requestarray) == 1:
            time = datetime.now().strftime('%d.%m.%Y %H:%M:%S %p')
            serverSocket.sendto(str.encode(time),addr)
        else:
            serverSocket.sendto(str.encode("Metoda Koha nuk ka parametra"),addr)
    elif (requestarray[0] == 'LOJA'):
        if len(requestarray) == 1:
            serverSocket.sendto(str.encode(str(LOJA())),addr)
        else:
            serverSocket.sendto(str.encode("Metoda Loja nuk ka parametra"),addr)
    elif requestarray[0] == 'KONVERTO':
        convert = "Konvertimet :\ncmToInch  \ninchToCm  \nkmToMiles \nMileToKm";

        try:
            s = kerkesa1[1]
            n = float(kerkesa1[2])
            serverSocket.sendto(str.encode(str(KONVERTO(s, n))),addr)
        except IndexError:
            serverSocket.sendto(str.encode("Shenoni fillimisht llojin e konvertimit dhe me pas vleren \n" + convert),addr)
        except ValueError:
            serverSocket.sendto(str.encode("Shenoni fillimisht llojin e konvertimit dhe me pas vleren \n" + convert),addr)
    elif requestarray[0]=='HASHPWD':
        if len(requestarray) == 2:
            s=kerkesa1[1]
            serverSocket.sendto(str.encode(str(HASHPWD(s))),addr)
        else:
            conn.send(str.encode("Shtypni passwordin pas metodes HASHPWD"),addr)
    elif requestarray[0]=='PLATFORM':
        if len(requestarray) == 1:
           serverSocket.sendto(str.encode(str(PLATFORM())),addr)
        else:
            serverSocket.sendto(str.encode("Metoda Platform nuk ka parametra"),addr)
    else:
        serverSocket.sendto(str.encode("Nuk keni shtypur asnje nga kerkesat e dhena!"),addr);



while True:
    request, address = serverSocket.recvfrom(1024)
    print('Klienti eshte lidhur me serverin ne %s  ne portin %s' % address)
    request = request.decode('utf-8')
    requestarray = request.split()
    sendRequest(request, serverSocket, address)
