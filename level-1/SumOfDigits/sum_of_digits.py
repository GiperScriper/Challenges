import sys, os

def main(input_file):    
    with open(input_file, 'r') as data:
        for line in data:
            sum_of_digits(line)


def sum_of_digits(digit):
    return sum([ int(ch) for ch in str(digit) ])

if __name__ == "__main__":
    # first argument must be a text file
    try:
        main(os.path.abspath(sys.argv[1]))
    except Exception:
        print os.path.abspath(sys.argv[1])              
        print 'First argument must be a text file!'