import re 
from part1 import read_input, parse_node, parse_input

def nr_of_steps(input_file):
    instructions, nodes = parse_input(input_file)

    current_nodes = [node for node in nodes if node[2] == 'A']
    steps = 0
    instruction_index = 0
    while(any(node[2] != 'Z' for node in current_nodes)): 
        if instruction_index == len(instructions):
            instruction_index = 0
        instruction = instructions[instruction_index]
        instruction_index += 1
        steps += 1

        current_nodes = [nodes[node][instruction] for node in current_nodes]

    return steps

if __name__ == "__main__":
    print(nr_of_steps('input.txt'))


 
    

