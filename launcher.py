#!/bin/env python3
import Net
import os
import sys

def main():
    print("Suduko GameServer Start")
    port = os.getenv("SUDO_PORT")
    if port == None:
        port = 8052
    Net.listen(port)

_arg = sys.argv
if _arg[0]=="--help":
    print("Game will listen at port 8052(DEFAULT), or use the env SUDO_PORT")
else:
    main()

