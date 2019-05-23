    
import codecs
import csv
import operator
import time

file_name = '板子_2019-05-22_16-47-28.log'
file_path = './'
    
def main():
    csvfile =  open(file_name[0 : -4] + '.csv', mode='r')
    asr_reader = csv.reader(csvfile)

    i = 0
    for row in asr_reader:
        print(row)
        i= i + 1
    print(i)

    csvfile.close


if __name__ == "__main__":
    # execute only if run as a script
    main()