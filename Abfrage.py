#!usr/bin/python3
# -*- coding: utf-8 -*-
#########################
#      Server Status    #
#         V.0.01        #
#########################

# Form implementation generated from reading ui file 'ServerStatus.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!



def abfrage():
    import socket

    # Augustinus
    try:
        url1 = "www.gs-staugustinus.de"
        port1 = 80
        port2 = 443
        socket.create_connection((url1, port1))
        socket.create_connection((url1, port2))
        try:
            augustinus = open("Mike.txt", "w")
            augustinus.write("#         DOMAINS:             #\n")
            augustinus.write("################################\n")
            augustinus.write("# GS Augustinus:        Online #\n")
            augustinus.close()
        except FileNotFoundError:
            pass
    except OSError:
        try:
            augustinus = open("Mike.txt", "w")
            augustinus.write("#         DOMAINS:             #\n")
            augustinus.write("################################\n")
            augustinus.write("# GS Augustinus:       Offline #\n")
            augustinus.close()
        except FileNotFoundError:
            pass
        pass

    # GS-Galgenmoor
    try:
        url2 = "www.gs-galgenmoor.de"
        socket.create_connection((url2, port1))
        socket.create_connection((url2, port2))
        try:
            gsgalgenmoor = open("Mike.txt", "a+")
            gsgalgenmoor.write("#------------------------------#\n")
            gsgalgenmoor.write("# GS Galgenmoor:        Online #\n")
            gsgalgenmoor.close()
        except FileNotFoundError:
            pass
    except OSError:
        try:
            gsgalgenmoor = open("Mike.txt", "a+")
            gsgalgenmoor.write("#------------------------------#\n")
            gsgalgenmoor.write("# GS Galgenmoor:       Offline #\n")
            gsgalgenmoor.close()
        except FileNotFoundError:
            pass
        pass

    # OBS Galgenmoor
    try:
        url3 = "www.obs-pag.de"
        socket.create_connection((url3, port1))
        socket.create_connection((url3, port2))
        try:
            obsgalgenmoor = open("Mike.txt", "a+")
            obsgalgenmoor.write("#------------------------------#\n")
            obsgalgenmoor.write("# OBS Galgenmoor:       Online #\n")
            obsgalgenmoor.close()
        except FileNotFoundError:
            pass
    except OSError:
        try:
            obsgalgenmoor.write("#------------------------------#\n")
            obsgalgenmoor.write("# OBS Galgenmoor:      Offline #\n")
            obsgalgenmoor.close()
            obsgalgenmoor = open("Mike.txt", "a+")
        except FileNotFoundError:
            pass
        pass

    # Johann Comenius
    try:
        url4 = "www.jcoclp.de"
        socket.create_connection((url4, port1))
        socket.create_connection((url4, port2))
        try:
            johanncomenius = open("Mike.txt", "a+")
            johanncomenius.write("#------------------------------#\n")
            johanncomenius.write("# Johann Comenius:      Online #\n")
            johanncomenius.close()
        except FileNotFoundError:
            pass
    except OSError:
        try:
            johanncomenius = open("Mike.txt", "a+")
            johanncomenius.write("#------------------------------#\n")
            johanncomenius.write("# Johann Comenius:     Offline #\n")
            johanncomenius.close()
        except FileNotFoundError:
            pass
        pass

    # Paul Gerhard
    try:
        url5 = "www.pgs-clp.de"
        socket.create_connection((url5, port1))
        socket.create_connection((url5, port2))
        try:
            paulgerhard = open("Mike.txt", "a+")
            paulgerhard.write("#------------------------------#\n")
            paulgerhard.write("# Paul Gerhard:         Online #\n")
            paulgerhard.close()
        except FileNotFoundError:
            pass
    except OSError:
        try:
            paulgerhard = open("Mike.txt", "a+")
            paulgerhard.write("#------------------------------#\n")
            paulgerhard.write("# Paul Gerhard:        Offline #\n")
            paulgerhard.close()
        except FileNotFoundError:
            pass
        pass

    # Gs Bethen
    try:
        url6 = "www.gs-avp.de"
        socket.create_connection((url6, port1))
        socket.create_connection((url6, port2))
        try:
            gsbethen = open("Mike.txt", "a+")
            gsbethen.write("#------------------------------#\n")
            gsbethen.write("# GS Bethen:            Online #\n")
            gsbethen.close()
        except FileNotFoundError:
            pass
    except OSError:
        try:
            gsbethen = open("Mike.txt", "a+")
            gsbethen.write("#------------------------------#\n")
            gsbethen.write("# GS Bethen:           Offline #\n")
            gsbethen.close()
        except FileNotFoundError:
            pass
        pass

    # OBS Pingel Anton
    try:
        url7 = "www.obs-pa.de"
        socket.create_connection((url7, port1))
        socket.create_connection((url7, port2))
        try:
            pingelanton = open("Mike.txt", "a+")
            pingelanton.write("#------------------------------#\n")
            pingelanton.write("# OBS Pingel Anton:     Online #\n")
            pingelanton.close()
        except FileNotFoundError:
            pass
    except OSError:
        pingelanton = open("Mike.txt", "a+")
        pingelanton.write("#------------------------------#\n")
        pingelanton.write("# OBS Pingel Anton:    Offline #\n")
        pingelanton.close()
        pass

    # GS Emstekerfeld
    try:
        url8 = "www.gs-efeld.de"
        socket.create_connection((url8, port1))
        socket.create_connection((url8, port2))
        try:
            emstekerfeld = open("Mike.txt", "a+")
            emstekerfeld.write("#------------------------------#\n")
            emstekerfeld.write("# GS Emstekerfeld:      Online #\n")
            emstekerfeld.close()
        except FileNotFoundError:
            pass
    except OSError:
        emstekerfeld = open("Mike.txt", "a+")
        emstekerfeld.write("#------------------------------#\n")
        emstekerfeld.write("# GS Emstekerfeld:     Offline #\n")
        emstekerfeld.close()
        pass

    # GS Wallschule
    try:
        url9 = "www.wallschule-clp.de"
        socket.create_connection((url9, port1))
        socket.create_connection((url9, port2))
        try:
            wallschule = open("Mike.txt", "a+")
            wallschule.write("#------------------------------#\n")
            wallschule.write("# GS Wallschule:        Online #\n")
            wallschule.close()
        except FileNotFoundError:
            pass
    except OSError:
        wallschule = open("Mike.txt", "a+")
        wallschule.write("#------------------------------#\n")
        wallschule.write("# GS Wallschule:       Offline #\n")
        wallschule.close()
        pass

    # GS St.-Andreas
    try:
        url10 = "www.gs-sta.de"
        socket.create_connection((url10, port1))
        socket.create_connection((url10, port2))
        try:
            andreas = open("Mike.txt", "a+")
            andreas.write("#------------------------------#\n")
            andreas.write("# GS St.-Andreas:       Online #\n")
            andreas.write("################################\n")
            andreas.close()
        except FileNotFoundError:
            pass
    except OSError:
        andreas = open("Mike.txt", "a+")
        andreas.write("#------------------------------#\n")
        andreas.write("# GS St.-Andreas:      Offline #\n")
        andreas.write("################################\n")
        andreas.close()
        pass

if __name__ == '__main__':
    import time
    import os

    while True:
        abfrage()
        os.system("cls")
        print()
        print()
        print()
        dat = open("Mike.txt", "r")
        show = dat.read()
        print(show)
        time.sleep(15)
