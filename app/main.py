import sys


def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        cmd = input()
        args = cmd.split(" ")

        # exit
        if args[0] == "exit":
            if args[1] == "0":
                break
        
        # echo
        elif args[0] == "echo":
            print(" ".join(args[1:]))

        else:
            print('{0}: command not found'.format(cmd))

if __name__ == "__main__":
    main()
