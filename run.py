import os
import webbrowser
import time
print("Hey, this is Noah. \nThis SHOULD open up a tab addressed to 'localhost:8000' if not, navigate there manually.\nI'm not sure why it needs a server to run the site properly, so i wrote a little script to do it for you easily!")
print("\n------------------------------------------------------")
os.system("python -m http.server")
webbrowser.open('https://localhost:8000', new=2)
print("yay")