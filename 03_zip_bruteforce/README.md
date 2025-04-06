# ZIP Brute Forcer

Python script that brute-forces password-protected `.zip` files using full character set.

## Features

- Tries all combinations of passwords up to 10 characters
- Uses letters, digits, and symbols
- Stops when correct password is found

## Warning

This method is extremely slow for long or complex passwords.  
Use only for educational/testing purposes.

## How to use

```bash
python zip_bruteforce.py
```

Then enter the path to the `.zip` file when prompted.

## Requirements

No external libraries required (uses built-in `zipfile`, `itertools`, `string`)
