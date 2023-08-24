def dec_to_hex(n):
    result = ""
    base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    while n > 0:
        result = base[n % 16] + result
        n //= 16
    return result

instruct = 0x0000

#Registers

R0 = 0b000
R1 = 0b001
R2 = 0b010
R3 = 0b011
R4 = 0b100
R5 = 0b101
R6 = 0b110
R7 = 0b111

#Operations

add = 0b00
sub = 0b01
mult = 0b10
div = 0b11

def Assemble(instruction):
    assembled_instruction = 0x0000  # Initialize the assembled instruction
    instructs = instruction.split()
    
    if instructs[0] == "ld":
        assembled_instruction += 0x8000
        
        if instructs[1] == "R0":
            assembled_instruction += R0 << 10
            
        elif instructs[1] == "R1":
            assembled_instruction += R1 << 10
            
        elif instructs[1] == "R2":
            assembled_instruction += R2 << 10
        
        elif instructs[1] == "R3":
            assembled_instruction += R3 << 10

        elif instructs[1] == "R4":
            assembled_instruction += R4 << 10

        elif instructs[1] == "R5":
            assembled_instruction += R5 << 10

        elif instructs[1] == "R6":
            assembled_instruction += R6 << 10

        elif instructs[1] == "R7":
            assembled_instruction += R7 << 10
        
        assembled_instruction += int(instructs[2])  # Convert the immediate value to int

    elif instructs[0] == "add" or instructs[0] == "sub" or instructs[0] == "mult" or instructs[0] == "div":
        if instructs[0] == "add":
            assembled_instruction += add << 13          # Opcodes

        elif instructs[0] == "sub":
            assembled_instruction += sub << 13

        elif instructs[0] == "mult":
            assembled_instruction += mult << 13

        elif instructs[0] == "div":
            assembled_instruction += div << 13

        #Registers - input 1

        if instructs[1] == "R0":
            assembled_instruction += R0 << 4
            
        elif instructs[1] == "R1":
            assembled_instruction += R1 << 4
            
        elif instructs[1] == "R2":
            assembled_instruction += R2 << 4
        
        elif instructs[1] == "R3":
            assembled_instruction += R3 << 4

        elif instructs[1] == "R4":
            assembled_instruction += R4 << 4

        elif instructs[1] == "R5":
            assembled_instruction += R5 << 4

        elif instructs[1] == "R6":
            assembled_instruction += R6 << 4

        elif instructs[1] == "R7":
            assembled_instruction += R7 << 4

        #Registers - input 2
            
        if instructs[2] == "R0":
            assembled_instruction += R0 << 7
            
        elif instructs[2] == "R1":
            assembled_instruction += R1 << 7
            
        elif instructs[2] == "R2":
            assembled_instruction += R2 << 7
        
        elif instructs[2] == "R3":
            assembled_instruction += R3 << 7

        elif instructs[2] == "R4":
            assembled_instruction += R4 << 7

        elif instructs[2] == "R5":
            assembled_instruction += R5 << 7

        elif instructs[2] == "R6":
            assembled_instruction += R6 << 7

        elif instructs[2] == "R7":
            assembled_instruction += R7 << 7

        #Registers - output

        if instructs[3] == "R0":
            assembled_instruction += R0 << 10
            
        elif instructs[3] == "R1":
            assembled_instruction += R1 << 10
            
        elif instructs[3] == "R2":
            assembled_instruction += R2 << 10
        
        elif instructs[3] == "R3":
            assembled_instruction += R3 << 10

        elif instructs[3] == "R4":
            assembled_instruction += R4 << 10

        elif instructs[3] == "R5":
            assembled_instruction += R5 << 10

        elif instructs[3] == "R6":
            assembled_instruction += R6 << 10

        elif instructs[3] == "R7":
            assembled_instruction += R7 << 10

    elif instructs[0] == "nop": assembled_instruction = 0xffff
    else:
        print("Invalid instruction: giving nop")
        assembled_instruction = 0xffff
    
    return dec_to_hex(assembled_instruction)

out = open("machineCode.mach16", "w")
assemblyFile = open("assemblyFile.as16", "r")
for line in assemblyFile.readlines():
    Machine_line = Assemble(line)
    out.write(Machine_line + "\n")
    print(Machine_line)

out.close()
assemblyFile.close()
        
while True:
    pass
