
"""
    Pinger, This is a application that pings a network node.
    Copyright (C) 2019 Thomas Scott
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. 
    
    If you need to contact me for any reason please Email me at 2e0eej@gmx.com
"""
#!/usr/bin/python3

import sys
import os
import socket
import time


print('''
Personal  Copyright (C) 2018  Tom
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; Please see the licence document.
''')


def main():
    total = 1024
    i = 0
    port = 0
    address = input("Please input the IP address: ")
    address = str(address)
    while port < 1024:
        open_ports = []
        closed_ports = []
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((address, port))

        if result == 0:
            #    print("Port", port, "is open.")
            port = str(port)
            open_ports.append(port)
        else:
            #    print("Port", port, "is closed.")
            port = str(port)
            closed_ports.append(port)
        port = int(port)
        port = port + 1
        sock.close()
        while i != 1024:
            progress(i, total, status="Scanning the ports.")
        i += 1
        open_length = len(open_ports)
        closed_length = len(closed_ports)
        if i == 1024:
            print("There are", open_length, "open ports.")
            #open_ports_clean = ' '.join(open_ports)
            print("The open ports are:", open_ports)
            print("There are", closed_length, "closed ports.")
            #closed_ports_clean = ' '.join(closed_ports)
            print("The closed ports are:", closed_ports)
            file = open("data.tdf", "w")
            file.write("The open ports are: \n")
            open_ports = str(open_ports)
            file.write(open_ports)
            file.write("\n")
            file.write("The closed ports are: \n")
            closed_ports = str(closed_ports)
            file.write(closed_ports)
            file.close()
        else:
            print("An issue occured!")
            time.sleep(1)
            print("Programming enterd panic mode and will exit in 2 seconds.")
            print("All data gatherd from the scan will be dunped into the data.tdf file.")
            file = open("data.tdf", "w")
            file.write("The open ports are: \n")
            open_ports = str(open_ports)
            file.write(open_ports)
            file.write("\n")
            file.write("The closed ports are: \n")
            closed_ports = str(closed_ports)
            file.write(closed_ports)
            file.close()
            time.sleep(2)
            sys.exit()


def loop():
    main()


def progress(count, total, status=''):
    os.system("clear")
    bar_len = 100
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('\r[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


if __name__ == '__main__':
    main()
