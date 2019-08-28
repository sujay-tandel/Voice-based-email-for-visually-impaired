import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time

print ("-"*60)
print ("       Project: Voice based Email for visually impaired")
print ("-"*60)

#project name
ts = gTTS(text="Project: Voice based Email for visually impaired", lang='en')
tsname=("path/name.mp3")
ts.save(tsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

#login from os
login = os.getlogin
print ("You are logged In from : "+login())

#choices
print ("1. Composed a mail.")
ts = gTTS(text="option 1. Composed a mail.", lang='en')
tsname=("path/hello.mp3")
ts.save(tsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

print ("2. Check your inbox")
ts = gTTS(text="option 2. Check your inbox", lang='en')
tsname=("hello.mp3")
ts.save(tsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)
#this is for input choices
ts = gTTS(text="Your choice ", lang='en')
tsname=("path/hello.mp3")
ts.save(ttsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

#voice recognition part
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Your choice:")
    audio=r.listen(source)
    print ("ok done!!")

try:
    text=r.recognize_google(audio)
    print ("You said : "+text)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
     
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

#choices details
if int(text) == 1:
    r = sr.Recognizer()                                                                     #recognizer
    with sr.Microphone() as source:
        print ("Your message :")
        audio=r.listen(source)
        print ("ok done!!")
    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        msg = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))    

    mail = smtplib.SMTP('smtp.gmail.com',587)                                               #host and port area
    mail.ehlo()                                                                             #Hostname to send for this command defaults to the FQDN of the local host.
    mail.starttls()                                                                         #security connection
    mail.login('emailID','pswrd')                                                           #login section
    mail.sendmail('emailID','victimID',msg)                                                 #send section
    print ("Congrates! Your mail has been send. ")
    ts = gTTS(text="Congrates! Your mail has been send. ", lang='en')
    tsname=("path/send.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    mail.close()   
    
if int(text) == 2:
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)                                          #this is host and port area.... ssl security
    unm = ('your mail/ victim mail')                                                        #username
    psw = ('pswrd')                                                                         #password
    mail.login(unm,psw)                                                                     #login
    stat, total = mail.select('Inbox')                                                      #total number of mails in inbox
    print ("Number of mails in your inbox :"+str(total))
    ts = gTTS(text="Total mails are :"+str(total), lang='en')                              #voice out
    tsname=("path/total.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    #unseen mails
    unseen = mail.search(None, 'UnSeen')                                                    # unseen count
    print ("Number of UnSeen mails :"+str(unseen))
    ts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
    tsname=("path/unseen.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    #search mails
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)')                                #fetch
    raw_email = email_data[0][1].decode("utf-8")                                            #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    ts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    tsname=("path/mail.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    #Body part of mails
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    ts = gTTS(text="Body: "+txt, lang='en')
    tsname=("path/body.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()
    mail.logout()
