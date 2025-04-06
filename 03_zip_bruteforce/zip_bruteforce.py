import zipfile
import itertools
import string
import time

# full charset (letters, digits, symbols)
charset = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?/\\|\""

# ask user for zip file path
zip_path = input("Enter path to ZIP file: ")

# open the zip file
try:
    zip_file = zipfile.ZipFile(zip_path)
except:
    print("Could not open zip file.")
    exit()

found = False
start_time = time.time()

# try all password lengths from 1 to 10
for length in range(1, 11):
    print(f"[*] Trying passwords of length {length}...")

    for pwd in itertools.product(charset, repeat=length):
        password = ''.join(pwd)

        try:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            print(f"[+] Password found: {password}")
            found = True
            break
        except:
            pass

    if found:
        break

end_time = time.time()
duration = round(end_time - start_time, 2)

if not found:
    print("[-] Password not found.")
else:
    print(f"[✓] Finished in {duration} seconds")
