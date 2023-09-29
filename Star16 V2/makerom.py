symbol_table = {}

def parse_operand(operand):
    operand = operand.strip()
    if operand.startswith('R'):
        return int(operand[1:])
    elif operand.isnumeric():
        return int(operand)
    else:
        return operand  # Return the operand as is (treat it as a label)


def assemble(assembly_filename):
    mnemonics = {
        'LDI': 4,
        'ADD': 0,
        'SUB': 1,
        'MULT': 2,
        'DIV': 3,
        'JMP': 5,
        'BEQ': 6,
        'BNE': 7,
        'BGT': 8,
        'BLT': 9,
        'BGE': 10,
        'BLE': 11,
        'HALT': 0xFFFFFFFF
    }

    instructions = []
    memory_address = 0  # Initialize memory address

    try:
        with open(assembly_filename, 'r') as assembly_file:
            for line in assembly_file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                # Check for labels
                if line.endswith(':'):
                    label = line[:-1]  # Remove the colon
                    symbol_table[label] = memory_address  # Associate label with memory address
                    continue

                parts = line.split()
                mnemonic = parts[0]

                # Check if mnemonic is in the mnemonics dictionary
                if mnemonic in mnemonics:
                    opcode = mnemonics[mnemonic]

                    # Check if mnemonic is HALT
                    if mnemonic == 'HALT':
                        instruction = opcode  # HALT doesn't have operands
                    else:
                        operands = [parse_operand(operand) for operand in parts[1:]]
                        if mnemonic == 'LDI':
                            if len(operands) == 2:
                                register = operands[0]
                                value = operands[1]
                                instruction = (opcode << 24) | (register << 16) | value
                            else:
                                print(f"Error: Invalid number of operands in '{line}'")
                                continue
                        elif mnemonic == 'JMP':
                            if len(operands) == 1:
                                operand = operands[0]

                                # Check if the operand is a label in the symbol table
                                if operand in symbol_table:
                                    address = symbol_table[operand]
                                    instruction = (opcode << 24) | address
                                else:
                                    # If the operand is not in the symbol table, it's treated as a numeric address
                                    try:
                                        address = int(operand)
                                        instruction = (opcode << 24) | address
                                    except ValueError:
                                        print(f"Error: Invalid operand or undefined label '{operand}'")
                                        continue
                            else:
                                print(f'Error: Invalid number of operands in "{line}"')

                        elif mnemonic == 'BEQ' or mnemonic == 'BNE' or mnemonic == 'BGT' or mnemonic == 'BLT' or mnemonic == 'BGE' or mnemonic == 'BLE':
                            if len(operands) == 3:
                                if operands[2] in symbol_table:
                                    address = symbol_table[operands[2]]
                                    instruction = (opcode << 24) | (operands[0] << 16) | (operands[1] << 8) | address
                                    print(opcode)
                                    print(operands[0])
                                    print(operands[1])
                                    print(address)
                                    print(instruction)
                                else:
                                    try:
                                        address = int(operand)
                                        instruction = (opcode << 24) | (operands[0] << 16) | (operands[1] << 8) | address
                                        print(opcode)
                                        print(operands[0])
                                        print(operands[1])
                                        print(address)
                                        print(instruction)
                                    except ValueError:
                                        print(f"Error: Invalid operand or undefined label '{operand}'")
                                        continue
                            else:
                                print(f"Error: Invalid number of operands in '{line}'")
                                continue

                        else:
                            if len(operands) == 3:
                                instruction = (opcode << 24) | (operands[0] << 16) | (operands[1] << 8) | operands[2]
                            else:
                                print(f"Error: Invalid number of operands in '{line}'")
                                continue
                    instructions.append(instruction)
                    memory_address += 1  # Increment memory address for the next instruction
                else:
                    print(f"Error: Unknown mnemonic '{mnemonic}'")
    except FileNotFoundError:
        print(f"Error: Assembly file '{assembly_filename}' not found")

    return instructions

# Rest of your code remains the same


# Example assembly code file: program.asm
# Contents:
# LDI R1 5
# LDI R2, 3  ; Note the comma
# LDI R3 2
# ADD R0 R1 R2
# MULT R0 R0 R3
# HALT

# Assemble the code from the file "program.asm"
instructions = assemble("program.asm")

if instructions:
    # Write the binary ROM file
    with open('program.rom', 'wb') as rom_file:
        for instruction in instructions:
            print(instruction)
            rom_file.write(instruction.to_bytes(4, byteorder='big'))

    print("Assembly code assembled successfully.")
