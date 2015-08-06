import re
import sys
import os

def get_coord_matches(data):
    pattern = "(?s)Color:\\s*\\S+\\s*\\((\w+)\\).*?X=(\\S+)\\s+Y=(\\S+)"
    matches = re.finditer(pattern, data, )
    matches = [match for match in matches]

    return matches

def get_formatted_coords(data):
    matches = get_coord_matches(data)
    lines = []
    for match in matches:
        groups = match.groups()
        line = "{} {},{}".format(groups[0], groups[1], groups[2])
        lines.append(line)
    formatted = "\n".join(lines)
    
    return formatted

def get_data():
    done = False
    lines = []
    empty_count = 0
    while not done:
        line = sys.stdin.readline()
        if line.strip() == "":
            empty_count = empty_count + 1
        else:
            empty_count = 0
        if empty_count > 1:
            done = True
        if not done:
            lines.append(line)
    return "".join(lines)

def output_data(data):
    home = os.path.expanduser("~")
    output_path = os.path.join(home, 'coords.txt')
    with open(output_path, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    data = get_data()
    print(data)
    formatted = get_formatted_coords(data)
    output_data(formatted)
