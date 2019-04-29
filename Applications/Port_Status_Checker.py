
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

import os
import socket

host = "192.168.1.152"
port = 81
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('''
Personal  Copyright (C) 2018  Tom
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; Please see the licence document.
''')
sock.settimeout(2)
result = sock.connect_ex((host, port))
if result == 0:
    print("The port is open.")
else:
    print("The port is closed.")
