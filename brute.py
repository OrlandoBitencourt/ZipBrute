import zipfile
from itertools import permutations
import itertools
import re
import datetime
from time import gmtime, strftime, localtime
import ctypes
import shutil

#setando full screen
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_MAXIMIZE = 3
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE)
#pegando tamanho da tela para o print sair centralizado
columns = shutil.get_terminal_size().columns

print('')
print('--------------------------------------------'.center(columns))
print('-------------ORLANDO BITENCOURT-------------'.center(columns))
print('------------------DCRIPT--------------------'.center(columns))
print('--------------------------------------------'.center(columns))


z1 = input("Nome do arquivo caminho+nome.zip: ".center(columns))
z = zipfile.ZipFile(z1)
validador = 0

for info in z.infolist():
    print ('Informações do Arquivo: ')
    print (info.filename)
    print ('\tComment:\t', info.comment)
    print ('\tModified:\t', datetime.datetime(*info.date_time))        
    print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
    print ('\tZIP version:\t', info.create_version)
    print ('\tCompressed:\t', info.compress_size, 'bytes')
    print ('\tUncompressed:\t', info.file_size, 'bytes')
    print ('------------------------------------------')

o = input("Aperte Y para começar a extrair: Y:")
if (str(o) == 'Y'):
    dataHoraStart = strftime("%a, %d %b %Y %H:%M:%S", localtime())
    caracteres2 = list(itertools.product("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", repeat=2))

    for i in caracteres2: 
        if (validador == 1):
            i=(caracteres2[-1])
            password = re.sub(r'\W',"",str(i))
        else:
            password = re.sub(r'\W',"",str(i))
            print(('Tentando combinações: '+password).center(columns))
        
            with zipfile.ZipFile(z1, 'r') as myzip:
                try:
                    myzip.extractall(pwd=(password.encode()))
                    dataHoraEnd = strftime("%a, %d %b %Y %H:%M:%S", localtime())
                    print(('----------------------------------').center(columns))
                    print(('Senha localizada: '+str(password)).center(columns))
                    print(('----------------------------------').center(columns))
                    print(('Inicio da execução: '+dataHoraStart).center(columns))
                    print(('Fim da execução: '+dataHoraEnd).center(columns))
                    print(('----------------------------------').center(columns))
                    for info in z.infolist():
                        print ('Informações do Arquivo: ')
                        print (info.filename)
                        print ('\tComment:\t', info.comment)
                        print ('\tModified:\t', datetime.datetime(*info.date_time))
                        print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
                        print ('\tZIP version:\t', info.create_version)
                        print ('\tCompressed:\t', info.compress_size, 'bytes')
                        print ('\tUncompressed:\t', info.file_size, 'bytes')
                    print('Senha do zip: '+str(password)+"\n")
                    validador = 1
                    ctypes.windll.user32.MessageBoxW(0, "Senha localizada: "+password, "Brute APP", 1).center(columns) #exit(0)
                except Exception:
                    pass
    else:
        if (validador == 1):
            print()
        else:
            caracteres3 = list(itertools.product("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", repeat=3))

            for i in caracteres3: 
                password = re.sub(r'\W',"",str(i))
                print(password)
                with zipfile.ZipFile(z1, 'r') as myzip:
                    try:
                        myzip.extractall(pwd=(password.encode()))
                        dataHoraEnd = strftime("%a, %d %b %Y %H:%M:%S", localtime())
                        print(('----------------------------------').center(columns))
                        print(('Senha localizada: '+str(password)).center(columns))
                        print(('----------------------------------').center(columns))
                        print(('Inicio da execução: '+dataHoraStart).center(columns))
                        print(('Fim da execução: '+dataHoraEnd).center(columns))
                        print(('----------------------------------').center(columns))
                        for info in z.infolist():
                            print ('Informações do Arquivo: ')
                            print (info.filename)
                            print ('\tComment:\t', info.comment)
                            print ('\tModified:\t', datetime.datetime(*info.date_time))
                            print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
                            print ('\tZIP version:\t', info.create_version)
                            print ('\tCompressed:\t', info.compress_size, 'bytes')
                            print ('\tUncompressed:\t', info.file_size, 'bytes')
                        print('Senha do zip: '+str(password)+"\n")
                        validador = 1
                        ctypes.windll.user32.MessageBoxW(0, "Senha localizada: "+password, "Brute APP", 1).center(columns) #exit(0)
                    except Exception:
                        pass
            else:
                if (validador == 1):
                    print()
                else:
                    caracteres4 = list(itertools.product("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", repeat=4))

                    for i in caracteres4: 
                        password = re.sub(r'\W',"",str(i))
                        print(password)
                        with zipfile.ZipFile(z1, 'r') as myzip:
                            try:
                                myzip.extractall(pwd=(password.encode()))
                                dataHoraEnd = strftime("%a, %d %b %Y %H:%M:%S", localtime())
                                print(('----------------------------------').center(columns))
                                print(('Senha localizada: '+str(password)).center(columns))
                                print(('----------------------------------').center(columns))
                                print(('Inicio da execução: '+dataHoraStart).center(columns))
                                print(('Fim da execução: '+dataHoraEnd).center(columns))
                                print(('----------------------------------').center(columns))
                                for info in z.infolist():
                                    print ('Informações do Arquivo: ')
                                    print (info.filename)
                                    print ('\tComment:\t', info.comment)
                                    print ('\tModified:\t', datetime.datetime(*info.date_time))
                                    print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
                                    print ('\tZIP version:\t', info.create_version)
                                    print ('\tCompressed:\t', info.compress_size, 'bytes')
                                    print ('\tUncompressed:\t', info.file_size, 'bytes')
                                print('Senha do zip: '+str(password)+"\n")
                                validador = 1
                                ctypes.windll.user32.MessageBoxW(0, "Senha localizada: "+password, "Brute APP", 1).center(columns) #exit(0)
                            except Exception:
                                pass
                    else:
                        if (validador == 1):
                            print()
                        else:
                            caracteres5 = list(itertools.product("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", repeat=5))

                            for i in caracteres5: 
                                password = re.sub(r'\W',"",str(i))
                                print(password)
                                with zipfile.ZipFile(z1, 'r') as myzip:
                                    try:
                                        myzip.extractall(pwd=(password.encode()))
                                        dataHoraEnd = strftime("%a, %d %b %Y %H:%M:%S", localtime())
                                        print(('----------------------------------').center(columns))
                                        print(('Senha localizada: '+str(password)).center(columns))
                                        print(('----------------------------------').center(columns))
                                        print(('Inicio da execução: '+dataHoraStart).center(columns))
                                        print(('Fim da execução: '+dataHoraEnd).center(columns))
                                        print(('----------------------------------').center(columns))
                                        for info in z.infolist():
                                            print ('Informações do Arquivo: ')
                                            print (info.filename)
                                            print ('\tComment:\t', info.comment)
                                            print ('\tModified:\t', datetime.datetime(*info.date_time))
                                            print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
                                            print ('\tZIP version:\t', info.create_version)
                                            print ('\tCompressed:\t', info.compress_size, 'bytes')
                                            print ('\tUncompressed:\t', info.file_size, 'bytes')

                                        print('Senha do zip: '+str(password)+"\n")
                                        validador = 1
                                        ctypes.windll.user32.MessageBoxW(0, "Senha localizada: "+password, "Brute APP", 1).center(columns) #exit(0)
                                    except Exception:
                                        pass
                            else:
                                if (validador == 1):
                                    print()
                                else:
                                    caracteres6 = list(itertools.product("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", repeat=6))

                                    for i in caracteres6: 
                                        password = re.sub(r'\W',"",str(i))
                                        print(password)
                                        with zipfile.ZipFile(z1, 'r') as myzip:
                                            try:
                                                myzip.extractall(pwd=(password.encode()))
                                                dataHoraEnd = strftime("%a, %d %b %Y %H:%M:%S", localtime())
                                                print(('----------------------------------').center(columns))
                                                print(('Senha localizada: '+str(password)).center(columns))
                                                print(('----------------------------------').center(columns))
                                                print(('Inicio da execução: '+dataHoraStart).center(columns))
                                                print(('Fim da execução: '+dataHoraEnd).center(columns))
                                                print(('----------------------------------').center(columns))
                                                for info in z.infolist():
                                                    print ('Informações do Arquivo: ')
                                                    print (info.filename)
                                                    print ('\tComment:\t', info.comment)
                                                    print ('\tModified:\t', datetime.datetime(*info.date_time))
                                                    print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
                                                    print ('\tZIP version:\t', info.create_version)
                                                    print ('\tCompressed:\t', info.compress_size, 'bytes')
                                                    print ('\tUncompressed:\t', info.file_size, 'bytes')
                                                print('Senha do zip: '+str(password)+"\n")
                                                validador = 1
                                                ctypes.windll.user32.MessageBoxW(0, "Senha localizada: "+password, "Brute APP", 1).center(columns) #exit(0)
                                            except Exception:
                                                pass
else:
    print('bye')