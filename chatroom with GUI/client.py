from socket import *
from tkinter import ttk
import tkinter as tk
import threading
from _thread import *

host ="127.0.0.1"
port =2770

client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect((host,port))

username=input("your name:")
client_socket.send(username.encode())

def send_msg():
    data=input_entry.get()
    chat_listbox.insert(tk.END,f"{username}:{data}")
    client_socket.send(data.encode())
    input_entry.delete(0,tk.END)

def recv_msg():
    while True:
        recv_data=client_socket.recv(2048).decode()
        chat_listbox.insert(tk.END,recv_data)
    

window=tk.Tk()
window.title(f"{username}")

window.resizable(False,False)

mainframe = ttk.Frame(window, style='TFrame')
mainframe.grid(column=0, row=0)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

chat_listbox = tk.Listbox(mainframe, width=50, height=20, font=('algerian', 12))
chat_listbox.grid(column=1, row=1, padx=10, pady=10)

input_entry = ttk.Entry(mainframe, width=50)
input_entry.grid(column=1, row=2, padx=10, pady=10)

send_button = ttk.Button(mainframe, style="TButton", text="Send", command=send_msg)
send_button.grid(column=1, row=3, padx=10, pady=10)

window.mainloop()

client_socket.close()