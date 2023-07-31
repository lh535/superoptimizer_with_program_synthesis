# base class for arithmetic RISC V assembly instructions
from typing import Tuple


# Representation for Registers in RISC V. Does not consider floating point registers because we never use those
class Reg:
    num: int
    const_regs = [5, 6, 7, 28, 29, 30, 31]

    def __init__(self, num: int):
        self.num = num
        assert num in self.const_regs

    def __repr__(self):
        return "x" + str(self.num)


class Var(Reg):
    var_regs = list(range(2, 8))

    def __init__(self, num: int):
        self.num = num
        assert num in self.var_regs

    def __repr__(self):  # TODO: include check that number is valid
        return "a" + str(self.num)


class Zero(Reg):
    def __init__(self):
        self.num = 0


# Representation of instructions with a variable number of arguments. Only represents instructions with a destination
class Instr:
    __match_args__ = ("instr", "args")
    instr: str
    # args: Tuple[Reg | int]  # register or immediate

    def __init__(self, instr: str, *args: Reg | int):
        self.instr = instr.lower()
        self.args = args

    def __repr__(self):
        return self.instr + " " + ", ".join(repr(a) for a in self.args)


class Assign(Instr):

    def __init__(self, reg: Reg, num: int):
        self.instr = "addi"
        self.args = (reg, Zero(), num)