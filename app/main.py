import sys


def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_input = input()
        args = user_input.split(" ")

        # exit
        if args[0] == "exit":
            if args[1] == "0":
                break
        
        # echo
        elif args[0] == "echo":
            print(" ".join(args))

if __name__ == "__main__":
    main()
