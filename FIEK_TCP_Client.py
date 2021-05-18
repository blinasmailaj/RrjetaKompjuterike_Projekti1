import socket


def pwdcheck(pwd):
    SpecialSym =['$', '@', '#', '%']
    val = True
    print('\n')
    if len(pwd) < 7:
        print('Passwordi duhet te jete me i gjate se 6 karaktere')
        val = False   
    if len(pwd) > 21:
        print('Passwordi duhet te jete me i shkurte se 20 karaktere')
        val = False
    if not any(char.isdigit() for char in pwd):
        print('Passwordi duhet te permbaje se paku nje numer')
        val = False
    if not any(char in SpecialSym for char in pwd):
        print('Passwordi duhet te kete se paku nje nga simbolet $ @ # %')
        val = False
    if val:
        return val


ok = True
while ok:
    print("[PRESS 1] Default values \n[PRESS 2] Manual Values \n[PRESS 0] Exit")
    cmd = input("Command : ")

    if int(cmd) == 1:
        serverName = 'localhost'
        serverPort = 14000
        print("Default Values: 127.0.0.1:14000")
    elif int(cmd) == 0:
        ok = False
        break
    elif int(cmd) == 2:
        serverName = input("Serveri:")
        serverPort = int(input("Porti :"))
    else:
        print("Invalid Command .Press 0,1 or 2")
        ok=True

    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socketClient.connect((serverName, serverPort))


        while ok:
            cmd = input("\nOperacioni(IP,NRPORTIT,NUMERO,ANASJELLTAS,KOHA,PALINDROM,LOJA,GCF,KONVERTO,HASHPWD,PLATFORM,EXIT)? :")
            print("Pergjigja:", end="")
            if len(cmd) > 128:
                print("Kerkesa eshte me e madhe se 128 bajt!")
                continue
            elif not cmd:
                print("Kerkesa eshte e zbrazet!")
                continue
            elif cmd.lower() == "exit":
                print("Server Socket Disconnected")
                socketClient.close()
                break
            else:
                command = cmd.lower()
                command = command.split(" ")
                try:
                    if command[0] == 'ip':
                        if (len(command) == 1):
                            socketClient.send(str.encode(cmd))
                        else:
                            print("Metoda IP nuk ka parametra")
                            continue
                    elif command[0] == "nrportit":
                        if (len(command) == 1):
                            socketClient.send(str.encode(cmd))
                        else:
                            print("Metoda NrPortit nuk ka parametra")
                            continue
                    elif command[0] == "numero":
                        if (len(command) > 1):
                            if all(char.isalpha() or char.isspace() for char in command):
                                socketClient.send(str.encode(cmd))
                            else:
                                print("Teksti i dhene duhet te permbaje vetem shkronja te alfabetit!")
                                continue
                        else:
                            print("Metoda Numero ka argument tekstin pas saj")
                            continue
                    elif command[0] == "anasjelltas":
                        if (len(command) > 1):
                             if all(char.isalpha() or char.isspace() for char in command):
                                socketClient.send(str.encode(cmd))
                             else:
                                print("Teksti i dhene duhet te permbaje vetem shkronja te alfabetit!")
                                continue
                        else:
                            print("Metoda Anasjelltas ka argument tekstin pas saj")
                            continue
                    elif command[0] == "palindrom":
                        if (len(command) == 2 ):
                            if command[1].isalpha():
                                socketClient.send(str.encode(cmd))
                            else:
                                print("Teksti i dhene duhet te permbaje vetem shkronja te alfabetit!")
                                continue
                        else:
                            print("Metoda Palindrom ka argument tekstin pas saj")
                            continue
                    elif command[0] == "loja":
                        if (len(command) == 1):
                            socketClient.send(str.encode(cmd))
                        else:
                            print("Metoda Loja nuk ka parametra")
                            continue
                    elif command[0] == "gcf":
                        if (len(command) == 3):
                            if command[1].isdecimal() and command[2].isdecimal():
                                socketClient.send(str.encode(cmd))
                            elif command[1].isdecimal() and (not command[2].isdecimal()):
                                print("Argumenti i dyte nuk eshte numer")
                                continue
                            elif (not command[1].isdecimal()) and  command[2].isdecimal():
                                print("Argumenti i pare nuk eshte numer")
                                continue
                            else:
                                print("Asnje nga argumentet nuk eshte numer")
                                continue
                        else:
                            print("Metoda GCF duhet te kete 2 numra si argumenta")
                            continue
                    elif command[0] == "konverto":
                        if (len(command) == 3):
                            if(command[1].isalpha() and command[2].isdecimal()):
                                if(command[1] == 'cmtoinch' or command[1] == 'cmtoinch' or command[1] == 'cmtoinch' or command[1] == 'cmtoinch'):
                                    socketClient.send(str.encode(cmd))
                                else:
                                    print("Konvertimi eshte gabim.Konvertimet :cmToInch  inchToCm  kmToMiles MileToKm")
                                    continue
                            else:
                                print("Argumenti 1 duhet te specifikoje llojin e konvertimit nderse Argumenti 2 shifren")
                                continue
                        else:
                            print("Metoda Konverto merr si parameter vetem llojin e konvertimit dhe vleren perkatese")
                            continue
                    elif command[0] == "koha":
                        if (len(command) == 1):
                            socketClient.send(str.encode(cmd))
                        else:
                            print("Metoda Koha nuk ka parametra")
                            continue
                    elif command[0] == "hashpwd":
                        if(len(command) == 2 ):
                            if pwdcheck(command[1]):
                                socketClient.send(str.encode(cmd))
                            else:
                                continue
                        else:
                            print("Shtypni passwordin pas metodes Hashpwd")
                            continue
                    elif command[0] == "platform":
                        if(len(command) == 1 ):
                            socketClient.send(str.encode(cmd))
                        else:
                            print("Metoda Platform nuk ka parametra")
                            continue
                    else:
                        print("Kerkesa juaj nuk eshte valide")
                        continue
                except Exception as e:
                    print(e)
                    continue

                output=""
                buffer = socketClient.recv(1024)
                output += buffer.decode("utf-8")

                print(buffer)
    except:
        print("\nConnection is not successful\n")
        continue


