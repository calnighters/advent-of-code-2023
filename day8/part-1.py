lines = []
input_file = open("input.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

directions = list(lines[0].replace('L', '0').replace('R', '1'))

nodes = {}
for line in lines[2:len(lines)]:
    split = line.split('=')
    node = split[0].strip()
    split_dirs = split[1].replace('(', '').replace(')', '').split(', ')
    left = split_dirs[0].strip()
    right = split_dirs[1].strip()
    nodes[node] = (left, right)

current_node = 'AAA'
dir_index = 0
count_steps = 0

while current_node != 'ZZZ':
    node = nodes[current_node]
    next_node = node[int(directions[dir_index])]
    dir_index = (dir_index + 1) % len(directions)
    current_node = next_node
    count_steps += 1

print(count_steps)