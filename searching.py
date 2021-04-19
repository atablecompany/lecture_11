import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as f:
        seq = json.load(f)
        if field in seq.keys():
            return seq[field]
        else:
            return None


def linear_search(sequential_data, number):
    number_pos = 0
    number_count = 0
    result = {"positions": [], "count": []}
    for element in sequential_data:
        number_pos += 1
        if element == number:
            number_count += 1
            result["positions"].append(number_pos)
            result["count"] = number_count

    return result


def pattern_search(sequential_data, pattern):
    result = {"positions": [], "count": []}
    pattern_len = len(pattern)
    # middle_idx = int(len(pattern)/2) + 1
    i = 0
    pattern_count = 0
    for element in sequential_data:
        if sequential_data[i:i+pattern_len] == pattern:
            pattern_count += 1
            result["positions"].append(i+1)
            result["count"] = pattern_count
        i += 1

    return result



def main():
    sequential_data = read_data(file_name='sequential.json', field="dna_sequence")
    print(sequential_data)

    print(linear_search(sequential_data, 0))

    print(pattern_search(sequential_data, pattern="TAG"))


if __name__ == '__main__':
    main()
