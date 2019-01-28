from bluetooth import *


class bluetooth_master():

    def __init__(self, uuid, name):
        """
            init bluetooth master
        :param uuid: uuid of the bluetooth
        :param name: name of the bluetooth
        """
        self.uuid = uuid
        self.name = name

        self.server_sock = BluetoothSocket(RFCOMM)
        self.server_sock.bind(("", PORT_ANY))
        self.server_sock.listen(1)

        self.port = self.server_sock.getsockname()[1]

        self.client_sock = None
        self.client_info = None

    def wait_and_connect(self, verbose=False):
        """
            wait client and connect
        :param verbose: show prints or not?
        :return:
        """
        advertise_service(self.server_sock, self.name,
                          service_id=self.uuid,
                          service_classes=[self.uuid, SERIAL_PORT_CLASS],
                          profiles=[SERIAL_PORT_PROFILE],
                          #                   protocols = [ OBEX_UUID ]
                          )

        if verbose:
            print('Waiting for connection on RFCOMM channel {}.'.format(self.port))

        self.client_sock, self.client_info = self.server_sock.accept()

        if verbose:
            print('Accepted connection from ', self.client_info)

        return True

    def get_recv_datas(self, verbose=False):
        """
            to receive data from client
        :param verbose:
        :return:
        """
        if self.client_sock != None:
            data = self.client_sock.recv(1024)
            if len(data) == 0:
                return None
            else:
                if verbose:
                    print('Received _{}_'.format(data))
                return data
        return None

    def close_connection(self, verbose=False):
        """
            to close the connection
        :param verbose:
        :return:
        """
        if self.client_sock != None:
            self.client_sock.close()
            self.server_sock.close()
            if verbose:
                print("Connection closed.")
            return True
        return False


if __name__ == '__main__':

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    bt = bluetooth_master(uuid, 'Test_name')

    bt.wait_and_connect(verbose=True)

    while True:
        try:
            if bt.get_recv_datas(verbose=True) == None:
                break
        except:
            print('connection fail.')

    bt.close_connection(verbose=True)
