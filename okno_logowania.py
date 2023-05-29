import customtkinter
from PIL import Image
import os

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
        
        self.textbox1.insert("0.0","tekst")
    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame
        

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame
    def button_password():
        print()
            
    def button_location():
        print()
    def button_brutforce():
        print()

if __name__ == "__main__":
    app = App()
    app.mainloop()
