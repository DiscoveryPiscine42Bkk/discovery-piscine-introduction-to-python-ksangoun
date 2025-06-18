import sys
args = sys.argv[1:]
if len(args) != 1:
    print("none")
else:
    input_string = args[0]
    z_count = input_string.count('z')
    
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)