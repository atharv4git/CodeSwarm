import tkinter as tk
import socket
import threading

class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((server_ip, server_port))

        self.root = tk.Tk()
        self.text = tk.Text(self.root)
        self.text.pack()
        self.text.bind("<Key>", self.on_key_press)

        threading.Thread(target=self.receive_data).start()
        self.root.mainloop()

    def receive_data(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            data_str = data.decode()
            self.text.insert("end", data_str)
            self.text.see("end")

    def on_key_press(self, event):
        key = event.char
        if key == '\r':
            key = '\n'
        elif key == '\x08':
            key = '\b'
        self.sock.send(key.encode())

client = Client("127.0.0.1", 5000)
