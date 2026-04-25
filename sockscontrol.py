import tkinter as tk
import configparser
from tkinter import ttk
from sshtunnel import SSHTunnelForwarder

config = configparser.ConfigParser()
config.read('sockscontrol.conf')

def ssh_tunnel_open():
    with SSHTunnelForwarder(
        (config['ssh']['ssh_host'], 22),
        ssh_username=config['ssh']['ssh_username'],
        ssh_pkey=config['ssh']['ssh_pkey'],
        remote_bind_address=(config['ssh']['remote_bind_address'], int(config['ssh']['remote_bind_port']))
    ) as tunnel:
        print("Tunnel active")
        input("Press enter to close tunnel")

ssh_tunnel_open()

#root = tk.Tk()
#root.title("SOCKS5 Proxy Status")
#root.geometry("300x200")

#frm_top = ttk.Frame(root, padding="20")
#frm_top.grid(columnspan=2)

#frm_bttn = ttk.Frame(root, padding="20")
#frm_bttn.grid()

#ttk.Label(frm_top, text="Connection Status").grid(column=0,row=0)
#ttk.Label(frm_top, text="Connection Time").grid(column=0, row=1)

#ttk.Button(frm_bttn, text="Connect", command=root.destroy).grid(column=0, row=0, pady=5, padx=5)
#ttk.Button(frm_bttn, text="Disconnect", command=root.destroy).grid(column=1, row=0, pady=5, padx=5)

#root.mainloop()
