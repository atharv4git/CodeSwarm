import tkinter as tk
import socket
import threading

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(1)
        self.connections = []

        self.root = tk.Tk()
        self.text = tk.Text(self.root)
        self.text.pack()
        self.text.bind("<Key>", self.on_key_press)

        threading.Thread(target=self.accept_connections).start()
        self.root.mainloop()

    def accept_connections(self):
        while True:
            conn, addr = self.sock.accept()
            self.connections.append(conn)
            threading.Thread(target=self.receive_data, args=(conn,)).start()

    def receive_data(self, conn):
        while True:
            data = conn.recv(1024)
            if not data:
                self.connections.remove(conn)
                conn.close()
                break
            data_str = data.decode()
            for c in self.connections:
                if c != conn:
                    c.send(data)
            if data_str == '\b':
                self.text.delete("end-2c", "end-1c")
            else:
                self.text.insert("end", data_str)
            self.text.see("end")

    def on_key_press(self, event):
        key = event.char
        if key == '\r':
            key = '\n'
        elif key == '\x08':
            key = '\b'
        for c in self.connections:
            c.send(key.encode())

server = Server("127.0.0.1", 5000)
