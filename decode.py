import opcodes

with open('data/chess_champion_rom_dump.bin', 'rb') as f:

    bytes_read = f.read()
    print("Bytes read: ", len(bytes_read) )

    position = 0
    while position < len(bytes_read):

        found = False
        for o in opcodes.opcodes:
            mask = 0xff << o[2]
            maskedOpcode = o[1] & mask
            maskedByte = bytes_read[position] & mask

            if maskedByte == maskedOpcode:

                opcode = o[0]
                operands = o[4]
                operandMask = 0x00

                if o[2] > 0:
                    mask = 0xff >> (8 - o[2])
                    operandMask = bytes_read[position] & mask

                if o[3] == 1:
                    memoryBytes = "0x{:02X}".format(bytes_read[position])
                    operands = operands.format(operandMask)
                elif o[3] == 2:
                    memoryBytes = "0x{:02X} 0x{:02X}".format(bytes_read[position], bytes_read[position+1])
                    if o[2] > 0:
                        operands = operands.format(operandMask,bytes_read[position + 1])
                    else:
                        operands = operands.format(bytes_read[position+1])
                elif o[3] == 3:
                    memoryBytes = "0x{:02X} 0x{:02X} 0x{:02X}".format(bytes_read[position], bytes_read[position+1], bytes_read[position+2])
                    operands = operands.format(((bytes_read[position+1] << 8) + bytes_read[position+2]) )

                memoryAddress = "0x{:04X}".format(position)

                print("{:<10}{:<16}{:<8}{:<12}{:<20}".format(memoryAddress, memoryBytes, opcode, operands, o[5]))
                position += o[3]
                found = True
                break

        if not found:
            opcodeByte = "0x{:02X}".format(bytes_read[position])
            memoryAddress = "0x{:04X}".format(position)

            print("{:<10}{:<16}Not found".format(memoryAddress, opcodeByte))
            position += 1

