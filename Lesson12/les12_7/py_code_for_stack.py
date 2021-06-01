import os

try:
    os.remove("output.txt")
except FileNotFoundError:
    pass


class Stack:
    def __init__(self):
        self.stack_lst = []
        self.use_input = -1

    def del_two_last(self):
        self.stack_lst = self.stack_lst[:len(self.stack_lst) - 2]

    def push(self, value):
        self.stack_lst.append(value)

    def pop(self):
        return self.stack_lst.pop()

    def add(self):
        top_el_add = int(self.stack_lst[-1]) + int(self.stack_lst[-2])
        self.del_two_last()
        self.stack_lst.append(top_el_add)

    def sub(self):
        top_el_sub = int(self.stack_lst[-1]) - int(self.stack_lst[-2])
        self.del_two_last()
        self.stack_lst.append(top_el_sub)

    def mul(self):
        top_el_mul = int(self.stack_lst[-1]) * int(self.stack_lst[-2])
        self.del_two_last()
        self.stack_lst.append(top_el_mul)

    def div(self):
        top_el_div = int(self.stack_lst[-1]) // int(self.stack_lst[-2])
        self.del_two_last()
        self.stack_lst.append(top_el_div)

    def print(self):
        top_el_curr = self.stack_lst[-1]
        with open('output.txt', 'a+') as out:
            out.write(str(top_el_curr) + '\n')

    def input(self):
        input_copy = []

        with open('input.txt', 'r') as inp:
            for line in inp:
                spl = line.split()
                input_copy.append(int(spl[0]))
        inp_top = input_copy[self.use_input + 1]
        self.use_input = input_copy.index(inp_top)
        self.stack_lst.append(inp_top)

    def print_chr(self):
        top_el_chr = chr(self.stack_lst[-1])
        with open('output.txt', 'a+', encoding='utf-8') as out:
            out.write(top_el_chr + '\n')

    def cmpj(self, ind1, ind2, ind3):
        if self.stack_lst[-1] > self.stack_lst[-2]:
            return int(ind1)
        if self.stack_lst[-1] == self.stack_lst[-2]:
            return int(ind2)
        if self.stack_lst[-1] < self.stack_lst[-2]:
            return int(ind3)


def define_commands():
    lines_coms = ''
    with open('code.stack', 'r') as com:
        for command in com:
            lines_coms += command
    commands = lines_coms.splitlines()
    return commands


def run_stack(exam):
    exec_com = define_commands()
    index_command = 0
    used_vars = {}
    while index_command < len(exec_com):
        if 'push' in exec_com[index_command]:
            split_com = exec_com[index_command].split()
            if split_com[1].lstrip('-').isdigit():
                exam.push(int(split_com[1]))
            else:
                push_key = split_com[1]
                push_value = used_vars.get(push_key)
                exam.push(int(push_value))
        if 'pop' in exec_com[index_command]:
            pop_split = exec_com[index_command].split()
            pop_key = pop_split[1]
            pop_value = exam.pop()
            used_vars[pop_key] = pop_value
        if exec_com[index_command] == 'add':
            exam.add()
        if exec_com[index_command] == 'sub':
            exam.sub()
        if exec_com[index_command] == 'mul':
            exam.mul()
        if exec_com[index_command] == 'div':
            exam.div()
        if exec_com[index_command] == 'print':
            exam.print()
        if exec_com[index_command] == 'input':
            exam.input()
        if exec_com[index_command] == 'print_chr':
            exam.print_chr()
        if 'cmpj' in exec_com[index_command]:
            split_cmpj = exec_com[index_command].split()
            in1 = split_cmpj[1]
            in2 = split_cmpj[2]
            in3 = split_cmpj[3]
            index_command = exam.cmpj(in1, in2, in3) - 1
            continue
        index_command += 1


s = Stack()
run_stack(s)
