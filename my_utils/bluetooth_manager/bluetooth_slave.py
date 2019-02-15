from bluetooth import *


class bluetooth_slave():

    def __init__(self, uuid, name):
        """
            init bluetooth slave
        :param uuid: uuid of the master host
        :param name: name of the master host
        """
        self.uuid = uuid
        self.name = name

        self.port = None
        self.name = None
        self.host = None

        self.sock = None

    def connect(self, verbose=False):
        """
            connect to master
        :param verbose: show prints or not?
        :return:
        """
        service_matches = find_service(uuid=self.uuid, name=self.name)

        first_match = service_matches[0]
        self.port = first_match["port"]
        self.name = first_match["name"]
        self.host = first_match["host"]

        if verbose:
            print('Connected to {} -> {}.'.format(self.name, self.host))

        self.sock = BluetoothSocket(RFCOMM)
        self.sock.connect((self.host, self.port))

        return True

    def send_datas(self, datas, verbose=False):
        """
            to send datas to master
        :param datas: data to send
        :param verbose:
        :return:
        """
        if self.sock != None:
            self.sock.send(datas)
            if verbose:
                print('Sent datas: {}'.format(datas))
            return True
        return False

    def get_recv_datas(self, verbose=False):
        """
            to receive data from client
        :param verbose:
        :return:
        """
        if self.sock != None:
            data = self.sock.recv(1024)
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
        if self.sock != None:
            self.sock.close()
            if verbose:
                print('Connection closed.')
            return True
        return False


if __name__ == '__main__':

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    bt = bluetooth_slave(uuid, 'Test_name')

    bt.connect(verbose=True)

    while True:
        data = input()
        if len(data) == 0: break
        bt.send_datas(data, verbose=True)

    bt.close_connection(verbose=True)
