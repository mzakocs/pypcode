from pypcode import Context, PcodePrettyPrinter
import binascii

ctx = Context("hexagon:LE:32:default")
asm = binascii.unhexlify("401CF4EB0C5EEF5B152A106C")
dx = ctx.disassemble(asm)

for ins in dx.instructions:
    print(f"{ins.addr.offset:#x}/{ins.length}: {ins.mnem} {ins.body}")