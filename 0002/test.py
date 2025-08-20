print("pi os 0.0.0.2")

import time
time.sleep(0.5)
print("the key ")
time.sleep(0.35)
print(".")
time.sleep(0.35)
print("..")
time.sleep(0.35)
print("...")
time.sleep(0.35)
print(".")
time.sleep(0.35)
print("..")
time.sleep(0.35)
print("...")
time.sleep(0.35)
print(".")
time.sleep(0.35)
print("..")
time.sleep(0.35)
print("...")
time.sleep(0.35)
print(".")
time.sleep(0.35)
print("..")
time.sleep(0.35)
print("...")
time.sleep(5)
import subprocess

script_to_run = "pihomescreen.py"
subprocess.run(["python", pihomescreen])
print(" ok")

from tkinter import Tk, StringVar, entry

 def on_text_changed(event):
     text_input = Entr.get()
     if text_input == "Hi"
        entry.delete(0, END)
        entry.insert(0, "Hello ,I am the first gen of the PI AI(PIai 3f163g7)")
        
root = Tk()

entry = Entry(root, widht=50)

entry.bind("<KeyRelease>", on_text_changed)

entry.pack()

root.mainloop()