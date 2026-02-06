import webbrowser
import random

def open():
    websites = ["https://www.google.com", "https://www.github.com", "https://www.python.org"]
    site = random.choice(websites)
    webbrowser.open(site)
    print(f"Opened {site}")
