import json


def read_file_multiple_lines(year, filename):
    filepath = '../' + year + '/input/' + filename + '.txt'
    lines = list()
    with open(filepath, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def read_file_single_line(year, filename):
    filepath = '../' + year + '/input/' + filename + '.txt'
    line = list()
    with open(filepath, 'r') as f:
        line = f.read().strip()
        f.close()
    return line


def read_json_file(year, filename):
    filepath = '../' + year + '/input/' + filename + '.json'
    data = dict()
    with open(filepath) as json_file:
        data = json.load(json_file)
    return data
