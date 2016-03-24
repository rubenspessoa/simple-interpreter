# coding: utf-8

from interpreter import Instruction, Interpreter

if __name__ == "__main__":

    interpreter = Interpreter()
    memory = []

    print ("For utilizing this interpreter, provide input in the format:\n" +
           "<INSTRUCTION> <OPERATING> <INSTRUCTION> <OPERATING>\n" +
           "EXAMPLE: \n" +
           "ADD 1 ADD 2 HALT\n" +
           "INSTRUCTIONS ARE 'ADD', 'SUB', 'MULT' AND 'HALT'")


    # Inserting instructions to memory.
    memory_input = input("Insert the instruction: ").split()
    print (memory_input)

    # We must have a HALT instruction.

    for instr in memory_input:
        if instr == "HALT":
            memory.append(-5)
        elif instr == "ADD":
            memory.append(-10)
        elif instr == "SUB":
            memory.append(-15)
        elif instr == "MULT":
            memory.append(-20)
        else:
            if (interpreter.is_valid(int(instr))):
                memory.append(int(instr))
            else:
                memory.append(-9)


    if (memory[0] is -20):
        interpreter.set_ac(1)
        
    interpreter.interpret(memory, 0)







