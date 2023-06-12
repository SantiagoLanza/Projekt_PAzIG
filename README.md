# Projekt_PAzIG
Edukacyjna aplikacja bezpieczeństwa w sieci 
Instrukcja obsługi aplikacji
1.	Uruchomienie aplikacji:
•	Upewnij się, że posiadasz zainstalowaną bibliotekę tkinter, customtkinter, PIL, pandas, matplotlib, numpy, subprocess, re, smtplib, email, PIL.ExifTags oraz webbrowser.
•	Uruchom plik nazwa_pliku.py w środowisku uruchomieniowym Python.
2.	Logowanie:
•	Wprowadź swoje dane logowania (nazwa użytkownika i hasło) w odpowiednie pola tekstowe.
•	Kliknij przycisk "Login" ("Zaloguj się").
3.	Wybór funkcji:
•	Po zalogowaniu się pojawi się główne okno aplikacji z trzema przyciskami.
•	Przyciski odpowiadają kolejno za:
•	Hakowanie hasła,
•	Hakowanie lokalizacji,
•	Atak bruteforce.
4.	Hakowanie hasła:
•	Kliknij przycisk "Password Hacking Start" ("Rozpocznij hakowanie hasła").
•	Wprowadź swoje dane logowania (email) w odpowiednie pole tekstowe.
•	Kliknij przycisk "OK".
•	Aplikacja przeszuka dostępne sieci WiFi na twoim komputerze i wyśle zebrane nazwy sieci wraz z hasłami na podany adres email.
5.	Hakowanie lokalizacji:
•	Kliknij przycisk "Location Hacking Start" ("Rozpocznij hakowanie lokalizacji").
•	Aplikacja sprawdzi dostępne obrazy w folderze "./images".
•	Jeśli obrazy zawierają dane exif z informacjami o lokalizacji, aplikacja wyświetli URL do Google Maps z oznaczoną pozycją geograficzną dla każdego obrazu.
6.	Atak bruteforce:
•	Kliknij przycisk "Bruteforce Attack Start" ("Rozpocznij atak bruteforce").
•	Wprowadź hasło składające się z 10 znaków w oknie dialogowym.
•	Kliknij przycisk "OK".
•	Aplikacja przeprowadzi atak bruteforce, próbując odgadnąć wprowadzone hasło.
7.	Powrót do logowania:
•	Aby powrócić do ekranu logowania, kliknij przycisk "Back" ("Powrót").
Wymagane biblioteki
Aby uruchomić aplikację, wymagane jest zainstalowanie następujących bibliotek Pythona:
•	tkinter - do tworzenia interfejsu graficznego,
•	customtkinter - do dostosowywania wyglądu interfejsu,
•	PIL - do manipulacji obraz.

