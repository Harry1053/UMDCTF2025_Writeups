# Deobfuscation
## category: Reverse Engineering
## author: unsure

## Description
the chall is not that complex. the key is to read ASSEMBLY!

## Attachments
"flag" (ELF 64-bit LSB executable)

## Overview
This binary implements a password check by XOR-ing user input with a hardcoded key and comparing it against an encrypted password. The solution was found through static analysis alone using Ghidra, without dynamic execution.

## Approach / Solution
1) Decompiled file in Ghidra (for full file check "./decompiled_entry_flag")
Interesting chunk:
```c
for (lVar1 = 0; (&DAT_0040209c)[lVar1] != 10; lVar1 = lVar1 + 1) {
  (&DAT_0040211c)[lVar1] = (&DAT_0040209c)[lVar1] ^ (&BYTE_00402034)[lVar1];
}
if (lVar1 == 0x34) {
  // ... comparison happens here ...
}
```

**Findings from the code above:**
- XOR operation is performed between **user input** (`DAT_0040209c`) and a **key** (`BYTE_00402034`).
- Password length is checked to ensure **52 bytes** (`0x34` in hexadecimal).
- After XOR-ing, the result is compared against a **hardcoded encrypted value** at `DAT_00402000`.

---

2) **Static Extraction of Data**  
   We statically retrieved the following:
   - The encrypted bytes (`DAT_00402000`)
   - The XOR key bytes (`BYTE_00402034`)

Both of these were **manually obtained** by inspecting the Ghidra decompiler output.

The `xor_key` bytes we recovered are:
```
75 6f 64 65 61 71 6f 75 75 76 69 45 60 70 7f 65 54 77 63 74 68 42 53 54 45 03 3d 7f 31 58 75 46 75 44 60 78 6a 74 51 4f 1c 5f 76 79 0b 2d 75 45 4b 55 66 78 45 6e 74 65 72 20 74 68 65 20 70 61 73 73 77 6f 72 64 3a 20 00 43 6f 72 72 65 63 74 21 20 00 57 72 6f 6e 67 20 70 61 73 73 77 6f 72 64 2e 20 20 20 00
```
The `encrypted flag` bytes were:
```
20 22 20 26 35 37 14 07 46 00 5A 17 44 35 52 0C 70 28 37 1C 5B 1D 70 16 76 50 69 5C 6E 6C 1B 12 54 69 2D 38 06 23 11 3D 2F 00 02 4A 68 45 3B 64 1A 20 55 05
```


3) Getting the flag:
Given the ciphertext (encrypted flag) and the xor key, the flag is a simple decryption away:

(script used is available below and in the repo, ./solve.py)

```py
encrypted = bytes.fromhex("20 22 20 26 35 37 14 07 46 00 5A 17 44 35 52 0C 70 28 37 1C 5B 1D 70 16 76 50 69 5C 6E 6C 1B 12 54 69 2D 38 06 23 11 3D 2F 00 02 4A 68 45 3B 64 1A 20 55 05")
xor_key = bytes.fromhex("75 6f 64 65 61 71 6f 75 75 76 69 45 60 70 7f 65 54 77 63 74 68 42 53 54 45 03 3d 7f 31 58 75 46 75 44 60 78 6a 74 51 4f 1c 5f 76 79 0b 2d 75 45 4b 55 66 78 45 6e 74 65 72 20 74 68 65 20 70 61 73 73 77 6f 72 64 3a 20 00 43 6f 72 72 65 63 74 21 20 00 57 72 6f 6e 67 20 70 61 73 73 77 6f 72 64 2e 20 20 20 00")

flag_bytes = [e ^ k for e, k in zip(encrypted, xor_key)]
flag = bytes(flag_bytes).decode('utf-8', errors='ignore').split('\x00')[0]

print(flag)
```

`python solve.py`/`python3 solve.py` outputs the flag.

## Flag
UMDCTF{r3v3R$E-i$_Th3_#B3ST#_4nT!-M@lW@r3_t3chN!Qu3}
