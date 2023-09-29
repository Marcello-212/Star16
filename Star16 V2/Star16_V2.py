import time

class MultiCycleProcessor:
    def __init__(self):
        self.registers = [0] * 8  # 8 general-purpose registers
        self.memory = [0] * 1024  # 1 KB of memory
        self.pc = 0  # Program counter

    def fetch(self):
        if self.pc < len(self.memory):
            instruction = self.memory[self.pc]
            return instruction
        else:
            return 0  # Return 0 if PC is out of bounds

    def decode(self, instruction):
        opcode = (instruction >> 24) & 0xFF
        operand1 = (instruction >> 16) & 0xFF
        operand2 = (instruction >> 8) & 0xFF
        operand3 = instruction & 0xFF
        return opcode, operand1, operand2, operand3



    def execute(self, opcode, operand1, operand2, operand3):
        if opcode == 0:  # ADD
            result = self.registers[operand1] + self.registers[operand2]
            print(f"Výledok {result} uložený do registra {operand3}.")
            self.registers[operand3] = result
            self.pc += 1
        elif opcode == 1:  # SUB
            result = self.registers[operand1] - self.registers[operand2]
            print(f"Výledok {result} uložený do registra {operand3}.")
            self.registers[operand3] = result
            self.pc += 1
        elif opcode == 2:  # MULT
            result = self.registers[operand1] * self.registers[operand2]
            print(f"Výledok {result} uložený do registra {operand3}.")
            self.registers[operand3] = result
            self.pc += 1
        elif opcode == 3:  # DIV
            result = self.registers[operand1] / self.registers[operand2]
            print(f"Výledok {result} uložený do registra {operand3}.")
            self.registers[operand3] = result
            self.pc += 1
        elif opcode == 4:  # LDI
            if 0 <= operand1 < 8:
                self.registers[operand1] = operand3  # Load immediate value into register
                print(f"{operand3} uložené do registra {operand1}.")
                self.pc += 1
            else:
                print("Zlé číslo registra v inštrukcii LDI.")
                self.pc = len(self.memory)  # Halt the processor
        elif opcode == 5:  # JMP (Unconditional Jump)
            print(f"Skočené na adresu {operand3}.")
            self.pc = operand3  # Jump to the specified address
        elif opcode == 6:  # BEQ (Branch if Equal)
            if self.registers[operand1] == self.registers[operand2]:
                print(f"Register {operand1} je rovnaký ako {operand2}, skáčem na adresu {operand3}.")
                self.pc = operand3  # Jump to the specified address if equal
            else:
                self.pc += 1
        elif opcode == 7:  # BNE (Branch if not Equal)
            if self.registers[operand1] != self.registers[operand2]:
                print(f"Register {operand1} nie je rovnaký ako {operand2}, skáčem na adresu {operand3}.")
                self.pc = operand3  # Jump to the specified address if not equal
            else:
                self.pc += 1
        elif opcode == 8:  # BGT (Branch if Greater)
            if self.registers[operand1] > self.registers[operand2]:
                print(f"Register {operand1} je väčší ako {operand2}, skáčem na adresu {operand3}.")
                self.pc = operand3  # Jump to the specified address if greater
            else:
                self.pc += 1
        elif opcode == 9:  # BLT (Branch if Less)
            if self.registers[operand1] < self.registers[operand2]:
                print(f"Register {operand1} je menší ako {operand2}, skáčem na adresu {operand3}.")
                self.pc = operand3  # Jump to the specified address if less
            else:
                self.pc += 1
        elif opcode == 10:  # BGE (Branch if Greater or Equal)
            if self.registers[operand1] >= self.registers[operand2]:
                print(f"Register {operand1} je väčší alebo rovnaký ako {operand2}, skáčem na adresu {operand3}.")
                self.pc = operand3  # Jump to the specified address if greater or equal
            else:
                self.pc += 1
        elif opcode == 11:  # BLE (Branch if Less or Equal)
            if self.registers[operand1] <= self.registers[operand2]:
                print(f"Register {operand1} je menší alebo rovnaký ako {operand2}, skáčem na adresu {operand3}.")
                self.pc = operand3  # Jump to the specified address if less or equal
            else:
                self.pc += 1
        elif opcode == 0xFF:  # HALT
            self.pc += 1
            return  # Halt the processor
        else:
            print("Zlý opkód:", opcode)
            self.pc += 1
            return  # Halt the processor


    def run(self):
        while True:
            instruction = self.fetch()
            if instruction == 0xFFFFFFFF:
                print("Nájdené zastavenie procesora, zastavovanie...")
                time.sleep(3)
                break  # Stop execution if an explicit halt instruction is encountered

            opcode, operand1, operand2, operand3 = self.decode(instruction) 

            self.execute(opcode, operand1, operand2, operand3)

            print(processor.registers)

            time.sleep(0.5)


    def load_rom(self, rom_filename):
        try:
            with open(rom_filename, 'rb') as rom_file:
                rom_contents = rom_file.read()
                for i in range(min(len(rom_contents) // 4, len(self.memory))):
                    instruction_bytes = rom_contents[i * 4 : (i + 1) * 4]
                    instruction = int.from_bytes(instruction_bytes, byteorder='big')
                    self.memory[i] = instruction
        except FileNotFoundError:
            print(f"ROM file '{rom_filename}' not found")

processor = MultiCycleProcessor()
processor.load_rom("program.rom")
processor.run()


