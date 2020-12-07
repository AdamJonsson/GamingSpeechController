#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:27:51 2019

Example use of tkinter with python threading.

@author: Benedict Wilkins AI
"""
import tkinter as tk
from threading import Thread 
import time
    
def run():
    global finish
    x = -200
    while not finish:
        time.sleep(0.5)
        canvas.delete('all')
        canvas.create_rectangle(x,0,x+200,200, fill='red')
        x += 10
        if x > 400:
            x = -200

def quit():
    global finish
    finish = True
    root.destroy()

root = tk.Tk()

root.title("Test")
root.protocol("WM_DELETE_WINDOW", quit)

canvas = tk.Canvas(root, width=400, height=200, bd=0,
                   highlightthickness=0, bg='white')
canvas.pack()

global finish
finish = False

control_thread = Thread(target=run, daemon=True)
control_thread.start()

root.mainloop()
control_thread.join()
  