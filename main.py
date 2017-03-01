import sys
import csv
import json
import math

def get_method(args):
	"""
	Parses the command line to find the method.

	Looking for 'xml' or 'json' and directs the program to output the correct format.
	"""
	if len(args)>1:
		method = args[1]
	else:
		method = False

	return method

def json_method(inputFile):
	"""
	Parses '.csv' input and formats into 'json' output.
	"""
	reader = csv.DictReader(inputFile)
	data = list(reader)
	for row in data:
		row['Stupidity'] = find_true_val(row['Stupidity'])
		row['Courage'] = find_true_val(row['Courage'])
	
	return json.dumps(data)

def xml_method(inputFile):
	"""
	Parses '.csv' input and formats into 'xml' output.

	1: Starts with a blank string
	2: Adds necessary xml metadata
	3: Adds every row of data from '.csv' file into an xml object called "Kerban"
	"""
	reader = csv.reader(inputFile)
	data = list(reader)

	outputString = ""
	outputString += '<?xml version="1.0"?>' + "\n"
	outputString += '<Kerban_Data>' + "\n"
	rowNum = 0

	for row in data:
		if rowNum == 0:
			tags = row #this is an array of the headers
		else:
			outputString += '	' + '<Kerban>' + "\n"
			for i in range(0,len(row)):
				if tags[i] == "Courage" or tags[i] == "Stupidity":
					row[i] = find_true_val(row[i])
				outputString += '		' + '<' + str(tags[i]) + '>' + str(row[i]) + '</' + str(tags[i]) + '>' + "\n"
			outputString += '	' + '</Kerban>' + "\n"
		rowNum += 1

	outputString += '</Kerban_Data>' + "\n"
	return outputString

def find_true_val(number):
	number = float(number)
	pi = math.pi
	number = math.atan(number)
	number = number + (pi/2.0)
	return number * 100.0 / pi

def main(args):
	"""
	Routes input to correct parsing function.
	"""
	if (args):
		inputFile = open(args[0], 'r')
		method = get_method(args)

		if method =='json':
			print json_method(inputFile)

		elif method == 'xml':
			print xml_method(inputFile)

		else: #defaults to json
			print json_method(inputFile)

	else: #Provide instructions if no arguments given
		print "Please supply an input file by typing something like \'input.csv\' as the first argument.\n"
		print "Please choose a method by typing \'xml\' or \'json\' as the secong argument."
		print "If no second argument is supplied, \'json\' will be assumed.\n"
		print "A sample input would be something like:"
		print "python main.py kerbals.csv json\n"
		print "If you just want a json output from \'kerbals.csv\' just run \'./main.sh\'"
		print "You may need to run \'chmod 755 main.sh\'"

if __name__ == '__main__':
	main(sys.argv[1:])