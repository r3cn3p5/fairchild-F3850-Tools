

byte_state = 0;

with open('../data/chess_champion_rom_dump.bin', 'rb') as f:

    bytes_read = f.read()
    print("Bytes read: ", len(bytes_read) )

    for b in bytes_read:
        byte_state |= b
        if byte_state == 255:
            break

    print("Bits set:", byte_state)




