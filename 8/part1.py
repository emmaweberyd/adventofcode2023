import re 

def read_input(file_name):
    with open(file_name) as f:
        return [line for line in f.read().splitlines() if line]

def parse_node(node):
    name, left, right = re.findall(r'[A-Z]{3}', node)
    return name, {'R': right, 'L': left}

def parse_input(input_file):
    lines = read_input(input_file)

    nodes = {}
    for line in lines[1:]:
        key, value = parse_node(line)
        nodes[key] = value

    return lines[0], nodes

def nr_of_steps(input_file):
    instructions, nodes = parse_input(input_file)

    node = 'AAA'
    steps = 0
    instruction_index = 0
    while(node != 'ZZZ'):
        if instruction_index == len(instructions):
            instruction_index = 0
        instruction = instructions[instruction_index]
        instruction_index += 1
        steps += 1
        node = nodes[node][instruction]

    return steps

if __name__ == "__main__":
    print(nr_of_steps('input.txt'))

 
    

