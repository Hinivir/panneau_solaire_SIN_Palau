# creer par Viktor
import smtplib
import time
import os


def mail(x):
    # pour google :
    serveur = smtplib.SMTP('smtp.google.com', '587')
    serveur.starttls()
    serveur.login('viktor.bruggeman@gmail.com', 'g3$IXTil#I2q')
    serveur.sendmail("viktor.bruggeman@gmail.com",
                     "viktor.bruggeman@gmail.com", str(x))
    serveur.quit()
    exit()


mail(Yolo)
