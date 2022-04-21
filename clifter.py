#!usr/bin/env python3

import sys
import subprocess

iota_counter = 0


def iota(reset=False):
    global iota_counter
    if reset:
        iota_counte = 0
    result = iota_counter
    iota_counter += 1

    return result


OP_PUSH = iota(True)
OP_POP = iota()
OP_PLUS = iota()
OP_MINUS = iota()
OP_DUMP = iota()
COUNT_OPS = iota()


def push(x):
    return (OP_PUSH, x)


def plus():
    return (OP_PLUS,)


def minus():
    return (OP_MINUS,)


def dump():
    return (OP_DUMP,)


def simulate_program(program):
    stack = []
    for op in program:
        assert COUNT_OPS == 5, "exaustive handling of operations in simulation"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        else:
            assert False, "unreachable"


def compile_program(program, out_file_path):
    with open(out_file_path, "w") as out:
        out.write("segment .text\n")
        out.write("dump:\n")
        out.write("    mov r9,-3689348814741910323\n")
        out.write("    sub rsp, 40\n")
        out.write("    mov BYTE [rsp+31], 10\n")
        out.write("    lea rcx, [rsp+30]\n")
        out.write(".L2:\n")
        out.write("    mov rax, rdi\n")
        out.write("    lea r8, [rsp+32]\n")
        out.write("    mul r9\n")
        out.write("    mov rax, rdi\n")
        out.write("    sub r8, rcx\n")
        out.write("    shr rdx, 3\n")
        out.write("    lea rsi, [rdx+rdx*4]\n")
        out.write("    add rsi, rsi\n")
        out.write("    sub rax, rsi\n")
        out.write("    add eax, 48\n")
        out.write("    mov BYTE [rcx], al\n")
        out.write("    mov rax, rdi\n")
        out.write("    mov rdi, rdx\n")
        out.write("    mov rdx, rcx\n")
        out.write("    sub rcx, 1\n")
        out.write("    cmp rax, 9\n")
        out.write("    ja .L2\n")
        out.write("    lea rax, [rsp+32]\n")
        out.write("    mov edi, 1\n")
        out.write("    sub rdx, rax\n")
        out.write("    xor eax, eax\n")
        out.write("    lea rsi, [rsp+32+rdx]\n")
        out.write("    mov rdx, r8\n")
        out.write("    mov rax, 1\n")
        out.write("    syscall\n")
        out.write("    add rsp, 40\n")
        out.write("    ret\n")
        out.write("global _start:\n")
        out.write("_start:\n")
        for op in program:
            assert COUNT_OPS == 5, "exaustive handling of operations in compilation"
            if op[0] == OP_PUSH:
                out.write("    ;; -- push --\n")
                out.write("    push %d\n" % op[1])
            elif op[0] == OP_PLUS:
                out.write("   ;; -- plus--\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    add rax, rbx\n")
                out.write("    push rax\n")
            elif op[0] == OP_MINUS:
                out.write("   ;; -- minus --\n")
                out.write("    pop rax\n")
                out.write("    pop rbx\n")
                out.write("    sub rbx, rax\n")
                out.write("    push rbx\n")
            elif op[0] == OP_DUMP:
                out.write("    ;;-- dump --\n")
                out.write("    pop rdi\n")
                out.write("    call dump\n")
            else:
                assert False, "unreachable"
        out.write("    mov rax, 60\n")
        out.write("    mov rdi, 0\n")
        out.write("    syscall\n")


def parse_word_as_op(word):
    assert COUNT_OPS == 5, "exaustive handling of operations in parsing"
    if word == "+":
        return plus()
    elif word == "-":
        return minus()
    elif word == ".":
        return dump()
    else:
        return push(int(word))


def load_program_from_file(file_path):
    with open(file_path, "r") as f:
        return [parse_word_as_op(word) for word in f.read().split()]


def usage(program):
    print(f"Usage: {str(program)} clifter <SUBCOMMAND> [ARGS]")
    print("SUBCOMMAND:")
    print("    sim = simulate the program")
    print("    com = compile the program")


def call_cmd(cmd):
    subprocess.call(cmd)


def uncons(xs):
    return (xs[0], xs[1:])


# program = [
#     push(30),
#     push(35),
#     plus(),
#     dump(),
#     push(500),
#     push(80),
#     minus(),
#     dump(),
# ]

if __name__ == "__main__":
    argv = sys.argv
    assert len(argv) >= 1
    (program_name, argv) = uncons(argv)
    if len(argv) < 2:
        usage(program_name)
        print("Error: no subcommand given")
        exit(1)
    (subcommand, argv) = uncons(argv)

    if subcommand == "sim":
        if len(argv) < 1:
            usage(program_name)
            print("error: no input file is provide to the simulation")
            exit(1)
        (program_path, argv) = uncons(argv)
        program = load_program_from_file(program_path)
        simulate_program(program)
    elif subcommand == "com":
        compile_program(program, "output.asm")
        call_cmd(["nasm", "-felf64", "output.asm"])
        call_cmd(["ld", "-o", "output", "output.o"])
        call_cmd(["rm", "output.o"])
        call_cmd(["./output"])
    else:
        # usage()
        print("Error!: unknown subcommand {}".format(str(command)))
        exit(1)
