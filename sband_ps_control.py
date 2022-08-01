'''
 * Copyright (C) 2022  University of Alberta
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
'''
'''
 * @file sband_ps_control.py
 * @author Charles Nokes
 * @date 2022-06-22
'''
import serial
import time
import tkinter as tk

window = tk.Tk()
window.configure(background="gray")
window.geometry("220x160")
window.title("SWITCH CTRL - PYTHON GUI")

megaBoard = serial.Serial('/dev/tty.usbmodem14201',9600)

def switch_control():
    print(">>> SWITCH CTRL PROGRAM <<<<\n")
    def lhcp():
        print("CTRL -> LHCP port -> ON")
        megaBoard.write(b'L')

    def rhcp():
        print("CTRL -> RHCP port -> ON")
        megaBoard.write(b'R')

    def uplink():
        print("CTRL -> UPLINK -> ON")
        megaBoard.write(b'U')

    def downlink():
        print("CTRL -> DOWNLINK -> ON")
        megaBoard.write(b'D')

    def quit():
        print("\n** END OF PROGRAM **")
        megaBoard.write(b'Q')
        megaBoard.close()
        window.destroy()

    b1 = tk.Button(window, text="LHCP", command=lhcp, bg="firebrick2", fg="ghost white", font=("Comic Sans MS", 15))

    b2 = tk.Button(window, text="RHCP", command=rhcp, bg="forest green", fg="gray7", font=("Comic Sans MS", 15))

    b3 = tk.Button(window, text="UPLINK", command=uplink, bg="yellow", fg="gray7", font=("Comic Sans MS", 15))

    b4 = tk.Button(window, text="DOWNLINK", command=downlink, bg="blue", fg="ghost white", font=("Comic Sans MS", 15))

    b5 = tk.Button(window, text="EXIT", command=quit, bg="gold", fg="gray7", font=("Comic Sans MS", 15))

    b1.grid(row=1, column=0, padx=5, pady=10)
    b2.grid(row=1, column=1, padx=5, pady=10)
    b3.grid(row=2, column=0, padx=5, pady=10)
    b4.grid(row=2, column=1, padx=5, pady=10)
    b5.grid(row=3, column=0, padx=5, pady=10)

    window.mainloop()

time.sleep(2)
switch_control()
