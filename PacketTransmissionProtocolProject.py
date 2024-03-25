class Packet:
    def __init__(self, source_address, destination_address, sequence_number,
                 is_ack=False, data=None):
        self.__source_address = source_address
        self.__destination_address = destination_address
        self.__sequence_number = sequence_number
        self.__is_ack = is_ack
        self.__data = data

    def __repr__(self):
        return ("Packet(Source Address: {self.__source_address}, \n"
                "Destination Address: {}, \n"
                "Sequence Number: {}, \n"
                "Is Ack: {}, \n"
                "Data: {}.)").format(self.__source_address,
                                     self.__destination_address,
                                     self.__sequence_number,
                                     self.__is_ack,
                                     self.__data)

    def get_source_address(self):
        return self.__source_address

    def get_destination_address(self):
        return self.__destination_address

    def get_sequence_number(self):
        return self.__sequence_number

    def set_sequence_number(self, seq_num):
        self.__sequence_number = seq_num

    def get_is_ack(self):
        return self.__is_ack

    def get_data(self):
        return self.__data


class Communicator:
    def __init__(self, address):
        self.__address = address
        self.__num_seq_current = None

    def get_address(self):
        return self.__address

    def get_current_sequence_number(self):
        return self.__num_seq_current

    def set_current_sequence_number(self, seq_num):
        self.__num_seq_current = seq_num

    def send_packet(self, packet):
        print("Packet Seq Num: {} was sent".format(packet.get_sequence_number()))

    def increment_current_seq_num(self):
        if Packet.get_is_ack():
            self.__num_seq_current += 1


class Sender(Communicator):
    def __init__(self, address, num_letters_in_packet):
        super().__init__(address)
        self.__num_letters_in_packet = num_letters_in_packet

    def prepare_packets(self, message, destination_address):
        # TODO: FILL YOU CODE HERE
        pass

    def receive_ack(self, acknowledgment_packet):
        return acknowledgment_packet.get_is_ack()


class Receiver(Communicator):
    def __init__(self, address):
        # TODO: FILL YOU CODE HERE
        super().__init__(address)
        self.__address = address
        self.received_packets = []

    def receive_packet(self, packet):
        # TODO: FILL YOU CODE HERE
        pass

    def get_message_by_received_packets(self):
        # TODO: FILL YOU CODE HERE
        pass


if __name__ == '__main__':
    source_address = "192.168.1.1"
    destination_address = "192.168.2.2"
    message = "What is up?"
    num_letters_in_packet = 3

    sender = Sender(source_address, num_letters_in_packet)
    receiver = Receiver(destination_address)

    packets = sender.prepare_packets(message, receiver.get_address())

    # setting current packet
    start_interval_index = packets[0].get_sequence_number()
    # setting current packet in the sender and receiver
    sender.set_current_sequence_number(start_interval_index)
    receiver.set_current_sequence_number(start_interval_index)

    # setting the last packet
    last_packet_sequence_num = packets[-1].get_sequence_number()
    receiver_current_packet = receiver.get_current_sequence_number()

    while receiver_current_packet <= last_packet_sequence_num:
        current_index = sender.get_current_sequence_number()
        packet = packets[current_index]
        packet = sender.send_packet(packet)

        ack = receiver.receive_packet(packet)

        result = sender.receive_ack(ack)

        if result == True:
            sender.increment_current_seq_num()
            receiver.increment_current_seq_num()

        receiver_current_packet = receiver.get_current_sequence_number()

    full_message = receiver.get_message_by_received_packets()
    print(f"Receiver message: {full_message}")
