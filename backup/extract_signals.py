# 1/27/2022
import sys
import re

try:
    ifile = open("misc_9_21_21.avc", 'r')
    ofile = open("single.avc", 'w')
except:
    print("Failed to open file.")

sig_wanted = " pad_n_spi_cs_ pad_n_spi_sdi pad_n_spi_sdo"
debug = 1
read_line = 1
dict_sig = {}
sig_value = []
while read_line:
    in_str = ifile.readline()
    # if line is empty, end of file is reached
    if not in_str:
        break
    if in_str != "\n":
        # avc header FORMAT
        if bool(re.match("FORMAT", in_str)):
            in_str = in_str.replace(";\n","")
            in_str = in_str.replace("FORMAT ", "")
            if 0: # debug
                ofile.writelines(in_str)
                print(in_str,end="")
            x_str = re.split(" ",in_str)
            count = 0
            for i in x_str:
                dict_sig[i] = count
                count += 1
            if 0: # debug
                for key, value in dict_sig.items():
                    print(key, value)
        else:
            in_str = in_str.replace(";\n", "")
            x_str = re.split(" ", in_str)
            single_bit = re.findall('\w',x_str[2])
            sdo = single_bit[dict_sig[sig_wanted]]
            s_str = "%s %s %s\n" %(x_str[0],dict_sig[sig_wanted],sdo)

            if debug:
                print(s_str,end="")






