
import csv
import sys

src_file = 'my_test_result.csv'
index_0 = 'http_req_duration' # data present in cell index 0 - first cell from left in csv
index_9_link1 = 'https://webadd/address_1' # data present in cell index 9 - the tenth cell from left in csv
index_9_link2 = 'https://webadd/address_2'

sys.stdout = open('output.csv', 'w') # output file
with open(src_file, newline = '') as infh:  # src file
    reader = csv.reader(infh)
    for row in reader:
        if row[0] == index_0 and row[9] == index_9_link1:
            # print(row[0], row[1], row[2], row[3]) # prin row by index: index 0 is cell 1, index 1 is cell 2, index 2 is cell 3 and so on ...
            print(",".join(row))
        if row[0] == index_0 and row[9] == index_9_link2:
            print(",".join(row))
sys.stdout.close()
