
import codecs
import csv
import operator
import time

file_name = '板子_2019-05-22_16-47-28.log'
file_path = './'

def asr_result(str_result, value_result, asr_writer):
    str_result = str_result.strip()
    value_result = value_result.strip()
    #print(str_result + '   ' + value_result)
    if operator.eq(str_result, '小顺 小顺'):
        if float(value_result) >= -15.8:
            bool_result = '1'
        else:
            bool_result = '0'
    else:
        if float(value_result) >= -9.5:
            bool_result = '1'
        else:
            bool_result = '0'
    print(str_result + ' ' + value_result + ' ' + bool_result)
    asr_writer.writerow([str_result, value_result, bool_result])


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def dispose(fp, asr_writer):
    ret = 0
    while True:
        line = fp.readline()
        if not line:
            break
        if(line.find('Asr Result[L]') != -1):
            str_asr = line[line.find('_>') + 2:line.find('</')]
            value_asr = fp.readline()
            if(operator.eq(value_asr[value_asr.find(']') + 2], '-')):
                value_asr = value_asr[value_asr.find(']') + 1: value_asr.find(']') + 7]
            else:
                value_asr = value_asr[value_asr.find(']') + 1: value_asr.find(']') + 6]
            #print(value_asr)
            if(is_number(value_asr)):
                asr_result(str_asr, value_asr, asr_writer)
                ret = ret + 1
            else:
                continue

    print(ret)
    return ret

def main():    
    csvfile =  open(file_name[0 : -4] + '.csv', mode='w+', newline='', errors='ignore')
    asr_writer = csv.writer(csvfile, dialect='excel')
    fp =  open(file_path + file_name, mode='r', encoding='utf-16-le')

    ret = dispose(fp, asr_writer)
    csvfile.flush
    csvfile.close
    fp.close

    

if __name__ == "__main__":
    # execute only if run as a script
    main()