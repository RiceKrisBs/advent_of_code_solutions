from copy import copy

def parse_input(file, part):
    responses = []
    with open(file, 'r') as f:
        group_response = set() if part == 1 else []
        for line in f:
            line = line.strip()
            if line == '':
                temp = copy(group_response)
                responses.append(temp)
                group_response.clear()
                continue
            if part == 1:
                for char in line:
                    group_response.add(char)
            elif part == 2:
                group_response.append(line)
        # add last group responses into list
        temp = copy(group_response)
        responses.append(temp)
        group_response.clear()
    return responses


if __name__ == '__main__':
    input_file = '.\\inputs\\day_06_input.txt'
    part_one_responses = parse_input(input_file, 1)
    part_two_responses = parse_input(input_file, 2)

    total_yes = sum(len(x) for x in part_one_responses)
    print(f"Part one solution: {total_yes}") #correct answer: 6335

    total_all_yes = 0
    for group in part_two_responses:
        for char in group[0]:
            total_all_yes += all(char in response for response in group)
    print(f"Part two solution: {total_all_yes}") #correct answer: 3392
