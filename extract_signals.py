# 1/28/2022 Rev 1.0 First Git Checkin
# 1/28/2022 Rev 1.1 Second Git Checkin
# replace split(" ",x) with split("\s+",x)
# Ignore '#' comment lines in evcd file
# Third Git Checkin : change to match ^R\d for vectors, remove print(,end="") for linux

import sys
import re

try:
    ifile = open(sys.argv[1], 'r')
    ofile = open(sys.argv[2], 'w')
except:
    print("Failed to open file.")

sig_wanted = ["pad_n_spi_cs_", "pad_n_spi_sdi", "pad_n_spi_sdo"]

debug = 0
dict_sig = {}

while True:
    in_str = ifile.readline()
    # if line is empty, end of file is reached
    if not in_str:
        break
    if in_str != "\n":
        # avc header FORMAT
        if bool(re.match("FORMAT", in_str)):
            in_str = in_str.replace(";\n","")
            in_str = in_str.replace("FORMAT ", "")
            if debug: # debug
                print(in_str)
            x_str = re.split("\s+",in_str)
            count = 0
            for i in x_str:
                dict_sig[i] = count
                count += 1
            if debug: # debug
                for key, value in dict_sig.items():
                    print(key, value)
        # if bool(re.search("WFT", in_str) or re.search("ts1", in_str)):
        if bool(re.match("^R\d", in_str)):
            in_str = in_str.replace(";\n", "")
            x_str = re.split("\s+", in_str)
            single_bit = re.findall('\w',x_str[2])
            signals_extracted = " "
            for i in sig_wanted:
                signals_extracted = signals_extracted + single_bit[dict_sig[i]]
                #print(dict_sig[i])
            #sdo = single_bit[dict_sig[sig_wanted]]
            #s_str = "%s %s %s\n" %(x_str[0],dict_sig[sig_wanted],sdo)
            s_str = "%s %s\n" % (x_str[0],signals_extracted)
            ofile.writelines(s_str)
            if debug:
                print(s_str)



ifile.close()
ofile.close()



