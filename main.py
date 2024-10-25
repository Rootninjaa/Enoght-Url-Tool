import pyshorteners
import qrcode
from tkinter import filedialog

logo = print(""""
 _____                   _     _   
| ____|_ __   ___   __ _| |__ | |_ 
|  _| | '_ \ / _ \ / _` | '_ \| __|
| |___| | | | (_) | (_| | | | | |_ 
|_____|_| |_|\___/ \__, |_| |_|\__|V 1.0
                   |___/
""")
print("Github: https://github.com/Rootninjaa/Enoght")
print("Support: rootlockinc@gmail.com")

# Shortener object
shortener = pyshorteners.Shortener()

while True:
        print("""
    1- TinyUrl
    2- is.gd (Recommended)
    3- TinyUrl + QR code
    4- is.gd + QR code
    """)

        provider = input("Enter the provider number (1/2/3/4): ")
        long_url = input("Enter the URL you want to shorten: ").strip()

        # Check if the URL input is empty
        if len(long_url) == 0:
            print("Invalid URL. Please enter a valid URL.")
            continue  # Ask the user for a new URL

        # Activate the shortening service
        # TinyUrl
        elif provider == '1':
            short_url = shortener.tinyurl.short(long_url)

        # is.gd
        elif provider == '2':
            short_url = shortener.isgd.short(long_url)


        elif provider == '3':
            short_url = shortener.tinyurl.short(long_url)
            codeqr = qrcode.make(short_url)
            kayit = filedialog.asksaveasfile(
                defaultextension=".png",
                filetypes=[("Png Files", "*.png")],
                title="save Tiny QR code"
            )
        
        elif provider == '4':
            short_url = shortener.isgd.short(long_url)
            codeqr = qrcode.make(short_url)
            kayit = filedialog.asksaveasfile(
                defaultextension=".png",
                filetypes=[("Png Files", "*.png")],
                title="save is.gd QR code"
            )


        else:
            print("Invalid provider number. Please try again.")
            continue  # Go back to the start of the loop

        # Display the shortened URL
        print(f"Shortened URL: {short_url}")

        # Prompt the user for a new URL
        input("Press Enter to shorten a new URL or Ctrl+C to exit.")
