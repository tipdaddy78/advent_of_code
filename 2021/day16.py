from util.FileHelper import read_file_single_line
from functools import reduce

class HexDecoder:
    def __init__(self, hex_string):
        self.version_sum = 0
        self.hex_string = hex_string
        self.bin_string = ''
        for x in self.hex_string:
            self.bin_string += self.convert_hex_to_bin(x)
        self.i = 0

    def convert_hex_to_bin(self, x_str):
        return (bin(int(x_str, 16))[2:]).rjust(4, '0')

    def process_packet(self):
        version = self.bin_string[self.i:self.i + 3]
        self.version_sum += int(version, 2)
        typ = self.bin_string[self.i + 3: self.i + 6]
        int_typ = int(typ, 2)
        self.i += 6
        if int_typ == 4:  # Dealing w/ literal value
            # For literal values, we want to grab groups of 5 digits
            # First digit represents if we keep going
            # Remaining 4 get added to a binary string
            more_nums = True
            num_str = ''
            while more_nums:
                more_nums = self.bin_string[self.i] == '1'
                num_str += self.bin_string[self.i+1:self.i+5]
                self.i += 5
            return int(num_str, 2)
        else:  # Dealing with an operator packet
            # Need to check length type id
            length_type_id = self.bin_string[self.i]
            sub_packet_vals = list()
            if length_type_id == '0':  # Grab the next 15 bits
                # That represents how long the sub-packets are
                len_sub_packets = int(self.bin_string[self.i+1:self.i+16], 2)
                self.i += 16
                sub_start = self.i
                while True:
                    sub_packet_vals.append(self.process_packet())
                    if self.i - sub_start == len_sub_packets:
                        break
            else:  # Grab next 11 bits
                # That represents the number of sub-packets
                num_sub_packets = int(self.bin_string[self.i+1:self.i+12], 2)
                self.i += 12
                for n in range(num_sub_packets):
                    sub_packet_vals.append(self.process_packet())
            if int_typ == 0:
                return sum(sub_packet_vals)
            elif int_typ == 1:
                return reduce((lambda x, y: x * y), sub_packet_vals)
            elif int_typ == 2:
                return min(sub_packet_vals)
            elif int_typ == 3:
                return max(sub_packet_vals)
            elif int_typ == 5:
                return 1 if sub_packet_vals[0] > sub_packet_vals[1] else 0
            elif int_typ == 6:
                return 1 if sub_packet_vals[0] < sub_packet_vals[1] else 0
            elif int_typ == 7:
                return 1 if sub_packet_vals[0] == sub_packet_vals[1] else 0


data = read_file_single_line('2021', 'day16')
hx = HexDecoder(data)
print(hx.process_packet())
print("Version:", hx.version_sum)
