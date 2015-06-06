import csvkit as csv

# http://www.gadzmo.com/python/reading-and-writing-csv-files-with-python-dictreader-and-dictwriter/

# Open the data file
test_file = 'puamdata_classification.csv'
csv_file = csv.DictReader(open(test_file, 'r'), delimiter=',', quotechar='"')

# Read the data and put into storage
terms_array = []
term_counter = 0
for line in csv_file:
    for term in ['Term1', 'Term2', 'Term3', 'Term4', 'Term5', 'Term6']:
    	if line[term]:
    		term_counter += 1
	    	terms_array.append( { 'RowID': term_counter, 'ObjectID': line['ObjectID'], 'Term': line[term].strip() } )

# Save the data
fieldnames = ['RowID', 'ObjectID', 'Term']
term_file = open('puamdata_terms.csv', 'w', newline='')
term_writer = csv.DictWriter(term_file, delimiter=',', fieldnames=fieldnames)  # quoting=csv.QUOTE_ALL
term_writer.writeheader()
for term_row in terms_array:
	term_writer.writerow(term_row)
term_file.close()

# Sample:
#
# for line in csv_file:
#     #print(line['RowID'])
#     for term in ['Term1', 'Term2', 'Term3', 'Term4', 'Term5', 'Term6']:
#     	if line[term]:
# 	    	print('{0},{1}'.format(line['ObjectID'],line[term].strip()))

# test_array = []
# test_array.append({'fruit': 'apple', 'quantity': 5, 'color': 'red'});
# test_array.append({'fruit': 'pear', 'quantity': 8, 'color': 'green'});
# test_array.append({'fruit': 'banana', 'quantity': 3, 'color': 'yellow'});
# test_array.append({'fruit': 'orange', 'quantity': 11, 'color': 'orange'});
# fieldnames = ['fruit', 'quantity', 'color']
# test_file = open('test2.csv','w', newline='')
# csvwriter = csv.DictWriter(test_file, delimiter=',', fieldnames=fieldnames)
# csvwriter.writeheader()
# for row in test_array:
#      csvwriter.writerow(row)
# test_file.close()


