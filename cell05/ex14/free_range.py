import sys
def main():
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        if num1 <= num2:
            result_range = list(range(num1, num2 + 1))
        else:
            result_range = list(range(num2, num1 + 1))
            
        print(result_range)
    except ValueError:
        print("none") 
if __name__ == "__main__":
    main()