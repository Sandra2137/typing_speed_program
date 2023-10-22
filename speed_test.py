from tkinter import *
import csv
import time


def start(event):
    global start_time
    start_time = time.time()
    return start_time


def check(event):
    end_time = time.time()
    global now2 
    now2 = end_time - start_time
    popupmsg()
    return now2

def popupmsg():
    popup = Tk()
    popup.config(padx=50, pady=50, bg='beige')
    popup.wm_title("Result")
    popup_label = Label(popup, text=f'Your typing speed is: {now2:.2f}s \n save your result in the CSV file', font=("Courier", 30), fg='#e20040', bg='beige', highlightthickness=0)
    popup_button = Button(popup, text="Save result", command=save_result, bg='beige', highlightthickness=0)
    close = Button(popup, text="Close program", command=window.destroy, bg='beige', highlightthickness=0)
    popup_label.pack()
    popup_button.pack()
    close.pack()
    popup.mainloop()


def save_result():
    with open('results.csv', 'a', newline='') as file:
        result = csv.writer(file)
        result.writerow([now2])
        print(f'Your typing speed is: {now2:.2f}s and was saved in csv file')


window = Tk()
window.title("Writing speed test")
window.config(padx=100, pady=80, bg='beige')


title_label = Label(text="Type the text and click enter \n to check your typing speed ", font=("Courier", 30,), fg='#AEAEE8', bg='beige', )
title_label.grid(column=1, row = 0)


input = Entry(window, width=50, highlightthickness=0)
input.grid(column=1, row=3)

input.bind("<FocusIn>", start) 
input.bind('<Return>', check)
window.mainloop()




