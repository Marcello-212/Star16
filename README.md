 # Introduction # 

 Hi! My name is Marcello and this is the guide to using my simulator of my computer.

 # The specs #

 My computer has got 8 general-purpose registers, R0-R7. They can be used as imputs or outputs.
 The built-in clock runs at 2 Hz, but you are free to run my computer as fast as you want. Just change the values in the time.sleep()-s
 There isn't much else, but it can add, substract, multiply and divide(no floating point). 
 
 # Assembly code #

 The assembly is very simple. Here are the operations

**nop**: does nothing  
**ld**: Loads a value into a register. Example: ld R0 2: Loads the register R0 with (you guessed it) 2  
**{operation}**: Does the specified operation on the input registers and stores the result in the output register.  
Example: add R0 R1 R2: Adds the contents of R0 and R1 and stores the result in R2.  
Replace operation with add, sub, mult or div based on the operation you want to do.

Once you know what to write, put it in assemblyCode.as16.

# How To Assemble #

Assembling is easy. Just run assemble.py.

# Simulate #

This is split for users of Logisim and Python.

### Logisim ###

Keep assemble.py on. In case you messed up, there's the machineCode.mach16 file. Open the pc.circ file and put your generated hex values into the ROM. Then just run it.

### Python ###

You are free to close assemble.py off. Run star16 sim.py and get the result!

##### How to speed up Python #####

You can take a peek at the star16 sim.py. I added delays so that the processor doesn't run at max speed. Feel free to edit the values of the delays.
