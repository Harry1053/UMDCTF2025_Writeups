encrypted = bytes.fromhex("20 22 20 26 35 37 14 07 46 00 5A 17 44 35 52 0C 70 28 37 1C 5B 1D 70 16 76 50 69 5C 6E 6C 1B 12 54 69 2D 38 06 23 11 3D 2F 00 02 4A 68 45 3B 64 1A 20 55 05")
xor_key = bytes.fromhex("75 6f 64 65 61 71 6f 75 75 76 69 45 60 70 7f 65 54 77 63 74 68 42 53 54 45 03 3d 7f 31 58 75 46 75 44 60 78 6a 74 51 4f 1c 5f 76 79 0b 2d 75 45 4b 55 66 78 45 6e 74 65 72 20 74 68 65 20 70 61 73 73 77 6f 72 64 3a 20 00 43 6f 72 72 65 63 74 21 20 00 57 72 6f 6e 67 20 70 61 73 73 77 6f 72 64 2e 20 20 20 00")

flag_bytes = [e ^ k for e, k in zip(encrypted, xor_key)]
flag = bytes(flag_bytes).decode('utf-8', errors='ignore').split('\x00')[0]

print(flag)