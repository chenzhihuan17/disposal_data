    
import codecs
import csv
import operator
import time

file_name = '板子_2019-05-22_16-47-28.log'
file_path = './'


xiaoshun_1_num = 0
xiaoshun_0_num = 0
xiaoshun_num = 0

other_1_num = 0
other_0_num = 0
other_num = 0

dialogue_success = 0
dialogue_failure = 0
dialogue_num = 0

all_num = 0


def dispose(csvfile):
    line = csvfile.readline()
    while len(line):
        file_seek = csvfile.tell()
        line = line.strip('\n')
        row = line.split(',')
        print(row, file_seek)
        line = csvfile.readline()
        # if(operator.eq(row[0], '小顺 小顺') and operator.eq(row[2], '1')):
        #     while True:
        #         row = asr_reader();
        #     print(row)
        # else:

    #all_num = all_num + 1

def main():
    csvfile =  open(file_name[0 : -4] + '.csv', mode='r')
    dispose(csvfile)
    csvfile.close


if __name__ == "__main__":
    # execute only if run as a script
    main()