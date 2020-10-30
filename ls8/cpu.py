"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.pc = 0       
        self.ram = [0] * 256       

    def ram_read(self, MAR): 
        # accept address to read & rtn value        
        return self.ram[MAR]            

    def ram_write(self, MDR):
        # accept a value to write & address to write it to
        return self.ram[MDR] 

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1
        # print(sys.argv)
        # memory = []
        # if len(sys.argv) != 2:
        #     print('wrong # of arguments')
        #     sys.exit(1)
        # with open(sys.argv[1]) as f:
        #     for line in f:
        #         line_split = line.split('#')
        #         command = line_split[0].strip()
        #         if command == '':
        #             continue
        #         command_num = int(command, 10)
        #         memory.append(command_num)
        #         address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""       
        isRunning = True
        
        # look to see what instructions have been recieved
        # execute them in order while none are hlt
        # decorators? 
        while isRunning: 

            # create Instruction Registry to read the memory address
            # stored in PC             
            ir = self.ram_read(self.pc)

            # use ram_read to read bytes & assign to var
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)

            # commands
            HLT = 0b00000001
            LDI = 0b10000010
            PRN = 0b01000111

            # if/else block to run CPU                        
            if ir == HLT:
                isRunning = False
                self.pc += 0

            # sets specified reg to specifid value
            elif ir == LDI:
                # value = operand_a
                # reg_address = operand_b
                # self.reg[reg_address] = value
                self.reg[operand_a] = operand_b
                self.pc += 3

            # print the file 
            elif ir == PRN:
                print(self.reg[operand_a])
                self.pc += 2

            

# create a list of all instructions
# INST = [
#     HLT  = 0b00000001,
#     LDI  = 0b10000010,
#     PRN  = 0b01000111,
#     MUL  = 0b10100010,
#     ADD  = 0b10100000,
#     SUB  = 0b10100001,
#     DIV  = 0b10100011,
#     PUSH = 0b01000101,
#     POP  = 0b01000110,
#     CALL = 0b01010000,
#     RET  = 0b00010001,
#     CMP  = 0b10100111,
#     JMP  = 0b01010100,
#     JEQ  = 0b01010101,
#     JNE  = 0b01010110,
# ]
