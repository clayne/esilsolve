from esilsolve import ESILSolver
import z3

# open in debug mode to exec concrete at first
esilsolver = ESILSolver("r200", flags=["-d", "-2"], lazy=True)

esilsolver.r2pipe.cmd("wa ret @ sym.imp.ptrace") # nop antidebug
esilsolver.r2pipe.cmd("db 0x004008fa; dc;") # setup the linked list 

state = esilsolver.call_state(0x0040074d)

addr = 0x1000000
state.registers["rdi"] = addr
flag = z3.BitVec("flag", 6*8)
state.memory[addr] = flag

# this one takes a whil-- NOT ANYMORE ITS FAST AF NOW
state = esilsolver.run(0x00400843, 
    avoid=[0x00400832], merge=[0x004007fd])

print("FLAG: %s " % state.evaluate_string(flag))