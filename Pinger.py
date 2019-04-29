```
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
```
#!/usr/bin/python3

import os
import time

loop = True

print('''
Personal  Copyright (C) 2018  Tom
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; Please see the licence document.
''')


def main(loop):
    while loop == True:
        print("Welcome to the application. This will simply ping the desired IP address provided.")
        ip_address = input("Please input the IP address: ")
        print(" ")
        response = os.system("ping -c 1 " + ip_address)
        if response == 0:
            print(" ")
            print("The host is up.")
        else:
            print(" ")
            print("The host is down.")

        loop_check = input("Would you like to check another IP address? (Y/N): ")
        if loop_check == "Y":
            loop = True
        elif loop_check == "N":
            loop = False
        else:
            print("That was not a response i was expecting. (I am going to quit you now.)")


if __name__ == '__main__':
    main(loop)

os.exit()
