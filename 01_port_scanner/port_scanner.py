import socket
import threading
import time

# list to store open ports
open_ports = []

# lock for writing to file from threads
lock = threading.Lock()

# scan one port
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))

        if result == 0:
            with lock:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
                with open("results.txt", "a") as f:
                    f.write(f"Port {port} is OPEN\n")

        s.close()
    except:
        pass

# main function
def main():
    ip = input("Enter IP address: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    print(f"\n[~] Scanning {ip} from port {start} to {end}...\n")

    with open("results.txt", "w") as f:
        f.write(f"Scan results for {ip}\n\n")

    start_time = time.time()

    threads = []

    for port in range(start, end + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    print(f"\n[✓] Done in {duration} seconds")
    print(f"[✓] Open ports: {len(open_ports)}")
    print("[✓] Results saved to results.txt")

    with open("results.txt", "a") as f:
        f.write(f"\nScan finished in {duration} seconds\n")
        f.write(f"Open ports: {len(open_ports)}\n")

if __name__ == "__main__":
    main()
