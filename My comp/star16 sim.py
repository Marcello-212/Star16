import time

def hex_to_binary(hex_values): 
    binary_results = []

    for hex_value in hex_values:
        try:
            cleaned_hex = hex_value.strip()  # Remove leading/trailing whitespace
            if cleaned_hex:  # Check if there's still content after stripping
                int_value = int(cleaned_hex, 16)  # Convert cleaned hex to int
                binary_value = bin(int_value)[2:]  # Convert int to binary string
                binary_results.append(binary_value.zfill(16))  # Pad with zeros to 16 bits
        except ValueError:
            print(f"Invalid hexadecimal value: {hex_value}")

    concatenated_binary = ''.join(binary_results)

    # Split the concatenated binary string into 16-bit chunks
    chunks = [concatenated_binary[i:i+16] for i in range(0, len(concatenated_binary), 16)]

    return chunks

# Read the hex values from the file
input_hex_values = []
with open("machineCode.mach16", "r") as file:
    for line in file:
        input_hex_values.append(line.strip())

# Convert, concatenate, and split the hex values to 16-bit chunks
binary_chunks = hex_to_binary(input_hex_values)

# Process each binary chunk and perform operations based on conditions
for i, binary_chunk in enumerate(binary_chunks, start=1):
    top_bit = binary_chunk[0]  # Top bit indicating operation (0 or 1)
    
    # Check if all bits are 1 in the binary chunk except for the top bit
    if all(bit == "1" for bit in binary_chunk[1:]):
        print("Sucessfully did nothing")
        time.sleep(0.25)
        continue  # Move to the next chunk without further processing
        
    if top_bit == "1":
        register_number = int(binary_chunk[3:6], 2)  # 3-bit register number
        value_to_load = int(binary_chunk[12:16], 2)  # 4-bit value to load
        
        if 0 <= register_number <= 7:
            variable_name = f"R{register_number}"
            
            if variable_name == "R0":
                R0 = value_to_load
            elif variable_name == "R1":
                R1 = value_to_load
            elif variable_name == "R2":
                R2 = value_to_load
            elif variable_name == "R3":
                R3 = value_to_load
            elif variable_name == "R4":
                R4 = value_to_load
            elif variable_name == "R5":
                R5 = value_to_load
            elif variable_name == "R6":
                R6 = value_to_load
            elif variable_name == "R7":
                R7 = value_to_load

            print(f"Loaded {variable_name} with value: {value_to_load}")
            
        else:
            print(f"Invalid register number in chunk {i}")
    else:
        operation_bits = binary_chunk[1:3]  # 2 bits for operation
        input_register1_num = int(binary_chunk[9:12], 2)  # First input register number
        input_register2_num = int(binary_chunk[6:9], 2)  # Second input register number
        
        if operation_bits == "00":
            operation = "Addition"
        elif operation_bits == "01":
            operation = "Subtraction"
        elif operation_bits == "10":
            operation = "Multiplication"
        elif operation_bits == "11":
            operation = "Integer Division"
        
        if 0 <= input_register1_num <= 7 and 0 <= input_register2_num <= 7:
            input_register1 = locals()[f"R{input_register1_num}"]
            input_register2 = locals()[f"R{input_register2_num}"]
            
            if operation == "Addition":
                result = input_register1 + input_register2
            elif operation == "Subtraction":
                result = input_register1 - input_register2
            elif operation == "Multiplication":
                result = input_register1 * input_register2
            elif operation == "Integer Division":
                result = input_register1 // input_register2
            
            output_register_num = int(binary_chunk[3:6], 2)  # Output register number
            if 0 <= output_register_num <= 7:
                output_variable_name = f"R{output_register_num}"
                locals()[output_variable_name] = result
                
                print(f"Stored result {result} in {output_variable_name}")
                
            else:
                print(f"Invalid output register number in chunk {i}")
        else:
            print(f"Invalid input register numbers in chunk {i}")
    time.sleep(0.5)

while True:
    time.sleep(0.5)
