import numpy as np


def get_valid_reports(possible_reports):
    valid_reports = 0
    print("Possible Reports:", possible_reports [0][:])
    for reports in possible_reports:
        if all(1 <= reports[i] - reports[i - 1] <= 3 for i in range(1, len(reports))):
            valid_reports += 1
        elif all(-1 >=reports[i] - reports[i - 1] >= -3 for i in range(1, len(reports))):
            valid_reports += 1
    return valid_reports


def less_dirty_reports(possible_reports):
    valid_reports = 0
    for reports in possible_reports:
        new_reports = []
        for i in range(len(reports)):
            new_report = reports[:i] + reports[i + 1:]
            new_reports.append(new_report)
            print("New Reports:", new_reports)
        if get_valid_reports(new_reports)>0:#
            valid_reports += 1
            print("One valid report found")
    return valid_reports

data = [[*map(int, l.split())] for l in open('C:\\Users\\Julian\\Desktop\\AOC24\\02\\input.txt')]

def good(d, s=0):
    for i in range(len(d)-1):
        if not 1 <= d[i]-d[i+1] <= 3:
            return s and any(good(d[j-1:j] + d[j+1:]) for j in (i,i+1))
    return True

for s in 0, 1: print("END", sum(good(d, s) or good(d[::-1], s) for d in data))



try:
    #reading 2 lists from file
    with open(r'C:\\Users\\Julian\\Desktop\\AOC24\\02\\input.txt', 'r') as input_file:
        lines = [line.strip() for line in input_file]
        possible_reports = [line.split() for line in lines]

    # convert to int
    possible_reports = [[int(num) for num in row] for row in possible_reports]

    #outputs
    valid_reports = get_valid_reports(possible_reports)
    all_valid_reports = less_dirty_reports(possible_reports)
    print("Valid Reports:", valid_reports)
    print("Valid Reports + dirty Reports", all_valid_reports)
except FileNotFoundError as e:
    print(f"Error: File not found. {e}")