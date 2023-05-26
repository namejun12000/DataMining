

# Global variables. Could be used as config params
IN_FILE="../Shellscriptexample/browsing-data.txt"
OUT_FILE ="./output.txt"


# Sample file reading
def read_input():
	with open(IN_FILE, "r") as text_file:
		all_lines = text_file.readlines()
	# print(all_lines[:10])

	return all_lines

# Sample file dumping
def dump_output():
	with open(OUT_FILE, "w") as text_file:
		text_file.write("OUTPUT A\n")
		text_file.write("FRO11987 FRO12685 0.4325\n")
		text_file.write("FRO11987 ELE11375 0.4225\n")
		text_file.write("FRO11987 GRO94758 0.4125\n")
		text_file.write("FRO11987 SNA80192 0.4025\n")
		text_file.write("FRO11987 FRO18919 0.4015\n")
		text_file.write("OUTPUT B\n")
		text_file.write("FRO11987 FRO12685 DAI95741 0.4325\n")
		text_file.write("FRO11987 ELE11375 GRO73461 0.4225\n")
		text_file.write("FRO11987 GRO94758 ELE26917 0.4125\n")
		text_file.write("FRO11987 SNA80192 ELE28189 0.4025\n")
		text_file.write("FRO11987 FRO18919 GRO68850 0.4015\n")
	return

# Entry funtion for the algorithm
def main():
	all_lines = read_input()
	dump_output()

if __name__ == '__main__':
	main()
