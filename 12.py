#!/usr/bin/env python3
import re

theInput = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 19 c
cpy 11 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

theInput = theInput.split('\n')

cpAMatcher = re.compile('cpy ([a-d]) ([a-d])')
cpBMatcher = re.compile('cpy (.*) ([a-d])')
incMatcher = re.compile('inc ([a-d])')
decMatcher = re.compile('dec ([a-d])')
jnzAMatcher = re.compile('jnz ([a-d]) (.+)')
jnzBMatcher = re.compile('jnz (.*) (.+)')


def execSimulation(cValue):
    regs = {'pc': -1, 'a': 0, 'b': 0, 'c': cValue, 'd': 0}
    while(True):
        regs['pc'] += 1
        # print('pc is now {}'.format(regs['pc']))
        if regs['pc'] == len(theInput):
            break
        instr = theInput[regs['pc']]

        a = cpAMatcher.match(instr)
        b = cpBMatcher.match(instr)
        c = incMatcher.match(instr)
        d = decMatcher.match(instr)
        e = jnzAMatcher.match(instr)
        f = jnzBMatcher.match(instr)
        if (a is None and b is None and c is None and
           d is None and e is None and f is None):
            raise Exception("there's a problem with the regexes")

        if a is not None:
            # copy instruction with two registers
            operandA = a.group(1)
            operandB = a.group(2)
            regs[operandB] = regs[operandA]

        elif b is not None:
            # copy instruction with a literal
            operandA = int(b.group(1))
            operandB = b.group(2)
            regs[operandB] = operandA

        elif c is not None:
            # incrementation
            operandA = c.group(1)
            regs[operandA] += 1

        elif d is not None:
            # decrementation
            operandA = d.group(1)
            regs[operandA] -= 1

        elif e is not None:
            # jump if register a is not equal to zero, be careful because pc++
            operandA = e.group(1)
            operandB = int(e.group(2))
            if regs[operandA] != 0:
                regs['pc'] += operandB-1

        elif f is not None:
            # jump if a is not equal to zero, be careful because pc++
            operandA = int(f.group(1))
            operandB = int(f.group(2))
            if operandA != 0:
                regs['pc'] += operandB-1

    print(regs['a'])


if __name__ == "__main__":
    execSimulation(0)
    execSimulation(1)
