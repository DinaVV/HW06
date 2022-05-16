# Task 1
def transform_to_row(infile, outfile):
    # open infile with read-mode
    with open(infile, 'r') as reader:
        contents = reader.readlines()
        # open outfile with write-mode
        with open(outfile, 'w') as writer:
            for line in contents:
                contents = line.rsplit(',')  # build-in split-function with ',' as separator
                for ele in contents:
                    writer.write(ele + '\n')  # to start new line character: \n


transform_to_row("resources/task1/infile.txt", "resources/task1/outfile.txt")


# Task 2
def add_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.readlines()
        with open(outfile, 'w') as writer:
            for line in contents:
                # adding Hello to the front of each line
                modified_line = "Hello " + line  # to add a greeting
                writer.write(modified_line)


# the out-file of task 1 is the in-file for task2
add_greeting("resources/task1/outfile.txt", "resources/task2/outfile.txt")


# Task 3
def strip_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.readlines()
        with open(outfile, 'w') as writer:
            for line in contents:
                stripped_line = line.strip("Hello ")  # to delete a greeting
                writer.write(stripped_line)


# the out-file of task 2 is the in-file for task3
strip_greeting("resources/task2/outfile.txt", "resources/task3/outfile.txt")


# Task 4
def combine_files(file1, file2, outfile):
    with open(file1, 'r') as reader_file1:
        with open(file2, 'r') as reader_file2:
            contents_file1 = reader_file1.readlines()  # read lines of file 1 into a python list "contents_file1"
            contents_file2 = reader_file2.readlines()  # read lines of file 2 into a python list "contents_file2"
            # check if the two input files have the same number of lines
            if len(contents_file1) != len(contents_file2):  # number of lines is not equal
                # if they don't have the same number of lines, print info to the console and return out of function
                print("support files with the same amount of lines only!")
                return
            # if they do have the same number of lines, combine the corresponding lines of each file to an output line
            with open(outfile, 'w') as writer:
                for i in range(len(contents_file1)):
                    # strip the "new line"-character of file1's line, add a space and append file2's line
                    combined_line = contents_file1[i].strip("\n") + " " + contents_file2[i]
                    writer.write(combined_line)


# the out-file of task 2 is the in-file for task 4
combine_files("resources/task2/outfile.txt", "resources/task4/infile.txt", "resources/task4/outfile.txt")
