# coding: utf-8
from dis import Instruction
from enum import Enum

class Instruction(Enum):
    add = 1
    sub = 2
    mult = 3
    halt = 4
    operating = 5

class Interpreter():

    run_bit = True
    PC = 0
    AC = 0
    m_memory = []

    def interpret(self, memory, starting_adress):
        self.set_memory(memory) # copy of memory
        self.PC = starting_adress

        while(self.run_bit):
            instr = memory[self.PC]
            instr_type = self.get_instr_type(instr)
            data_loc = self.find_data(instr, instr_type)

            if instr_type == Instruction.halt:
                print ("AC equals to " + str(self.AC))
                break

            if (data_loc in range(len(memory))):
                data = memory[data_loc]
                self.execute(instr_type, data)

            self.PC = self.PC + 1


    def set_memory(self, value):
        self.m_memory = value

    def set_ac(self, value):
        self.AC = value

    def get_instr_type(self, address):
        if address == -5:
            return Instruction.halt
        elif address == -10:
            return Instruction.add
        elif address == -15:
            return Instruction.sub
        elif address == -20:
            return Instruction.mult
        return Instruction.operating

    def find_data(self, instr, type):
        for i in range(self.PC, len(self.m_memory)):
            if (self.m_memory[i] == instr and self.get_instr_type(instr) == type):
                return i + 1
        return -1

    def execute(self, type, data):

        if type == Instruction.add:
            self.AC += data
        elif type == Instruction.sub:
            self.AC -= data
        elif type == Instruction.mult:
            self.AC *= data
        elif type == Instruction.halt:
            self.run_bit = False
            print ("AC equals to " + str(self.AC))

    def is_valid(self, instr):
        if instr not in range(10):
            return False
        return True
