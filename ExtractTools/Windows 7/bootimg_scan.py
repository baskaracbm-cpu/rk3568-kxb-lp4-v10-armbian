#!/usr/bin/env python3

import os
import struct

FDT_MAGIC = b'\xd0\x0d\xfe\xed'

def find_all(data, sub):
    start = 0
    while True:
        pos = data.find(sub, start)
        if pos == -1:
            return
        yield pos
        start = pos + 1

def extract_dtb(filename):
    with open(filename, "rb") as f:
        blob = f.read()

    found = list(find_all(blob, FDT_MAGIC))

    if not found:
        print("[-] No DTB found")
        return

    print("[+] Found %d DTB(s)\n" % len(found))

    for index, off in enumerate(found):

        totalsize = struct.unpack(">I", blob[off+4:off+8])[0]

        print("DTB %d" % index)
        print(" Offset : 0x%08X" % off)
        print(" Size   : %d bytes" % totalsize)

        dtb = blob[off:off+totalsize]

        out = "dtb_%d.dtb" % index

        with open(out, "wb") as o:
            o.write(dtb)

        print(" Saved  :", out)
        print()

if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage:")
        print(" python bootimg_scan.py boot.img")
        sys.exit(1)

    extract_dtb(sys.argv[1])
