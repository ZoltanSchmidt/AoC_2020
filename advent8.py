import re

def replace_command(commands, arg, ind, exec_pos):
    commands_copy = commands.copy()

    while True:
        if commands_copy[exec_pos[ind]] == 'jmp':
            commands_copy[exec_pos[ind]] = 'nop'
            return commands_copy, arg, ind
        elif commands_copy[exec_pos[ind]] == 'nop' and not arg[exec_pos[ind]]:
            commands_copy[exec_pos[ind]] = 'jmp'
            return commands_copy, arg, ind
        else:
            ind -= 1

def fix_code(comms_in, args_in):
    comms = comms_in
    args = args_in
    accumulator = 0
    cur_pos = 0
    swap_index = 0
    executed_pos = []
    while True:
        if cur_pos in executed_pos:
            accumulator = 0
            cur_pos = 0
            swap_index -= 1
            comms, args, swap_index = replace_command(comms_in,args_in,swap_index,executed_pos)
            executed_pos.clear()

        command, arg = comms[cur_pos], args[cur_pos]
        executed_pos.append(cur_pos)

        if command == 'nop':
            cur_pos += 1
        elif command == 'acc':
            accumulator += arg
            cur_pos += 1
        elif command == 'jmp':
            cur_pos += arg

        if cur_pos >= len(comms):
            return accumulator

def get_accumulator(comm_with_arg):
    accumulator = 0
    cur_pos = 0
    executed_pos = []
    while True:
        command, arg = comm_with_arg[cur_pos]

        if cur_pos in executed_pos:
            print('break')
            return accumulator
        executed_pos.append(cur_pos)

        if command == 'nop':
            cur_pos += 1
        elif command == 'acc':
            accumulator += arg
            cur_pos += 1
        elif command == 'jmp':
            cur_pos += arg


if __name__ == '__main__':
    with open("advent8.txt") as f:
        text = f.read()

    lines = text.split('\n')

    commands_list = [re.search(r'jmp|acc|nop', line).group() for line in lines]
    arg_list = [int(re.search(r'[-+]?[0-9]+', line).group()) for line in lines]
    commands_with_arg_lst = list(zip(commands_list,arg_list))

    print(get_accumulator(commands_with_arg_lst))

    print(fix_code(commands_list,arg_list))
