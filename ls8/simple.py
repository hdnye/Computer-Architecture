# OPERATION PRINT HELLO WORLD
# give the computer a value
import sys
PRINT_WORLD     = 1
HALT            = 2
PRINT_NUM       = 3
SAVE            = 4
PRINT_REGISTER  = 5
ADD              =6 
# memory stores binary values
memory = [
    PRINT_WORLD,
    PRINT_NUM, # PRINT 5
    5,    
    SAVE, # SAVE 42 TO R2
    42, 
    2,
    SAVE,   # SAVE 37 to R3
    37, 
    3,
    ADD,   # ADD R3 + R2 store result in R1
    3,
    2,
    PRINT_REGISTER, #PRINT RESULT IN R3
    3,
    HALT

    
]

# Program Counter(PC) Register starts reading from location zero
# keeps track of where to start reading from memory
pc = 0
registers = [0] * 8
# read commands into computer from memory
running = True
while running:

    command = memory[pc]
    
    if command == PRINT_WORLD:
        print('Hello World')
        pc += 1
        
    elif command == HALT:
        running = False
        pc += 1

    elif command == PRINT_NUM:
        # look at the next line in memory
        value = memory[pc + 1]
        # print that value
        print(value)
        pc += 2
    
    elif command == SAVE:
        value = memory[pc + 1]
        reg_address = memory[pc + 2]
        registers[reg_address] = value
        pc += 3

    elif command == PRINT_REGISTER:
        reg_address = memory[pc + 1]
        print(registers[reg_address])
        pc += 2
    
    elif command == ADD:
        reg_addr_1 = memory[pc + 1]
        reg_addr_2 = memory[pc + 2]
        # retrieve values in both registers
        val1 = registers[reg_addr_1]
        val2 = registers[reg_addr_2]
        # add & store results in reg_add_1
        registers[reg_addr_1] = val1 + val2
        # move to next command
        pc += 3

# load a program into memory
# reads files & uses an argument to get specific info
print(sys.argv)
memory = []
if len(sys.argv) != 2:
    print('wrong # of arguments')
    sys.exit(1)
with open(sys.argv[1]) as f:
    for line in f:
        # split the comments on the # char
        line_split = line.split('#')
        command = line_split[0].strip()
        if command == '':
            continue
        command_num = int(command, 2)
        memory.append(command_num)