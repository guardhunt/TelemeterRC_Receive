import struct

def decode(frame):
    """do stuff with frame, generate output"""
    #payload.decode('utf-8')
    print ("Frame Recieved (Len: " + str(len(frame)) + ")")
    print ("Destination IP: " + str(int.from_bytes(frame[0:5], byteorder='little')))
    print ("SourceIP:" + str(int.from_bytes(frame[6:11], byteorder="little")))
    print ("Packet Type: "  + str(int.from_bytes(frame[12:14], byteorder='little')))
    print ("Payload Content: " + str(int.from_bytes(frame[15:], byteorder="little")))
    print ('\n')


def encode():
    """encode payload from sensors"""

    payload = ("payload").encode("utf-8")
    return payload
