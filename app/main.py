import sys


def main():

    __pre_built_cmds = ('echo', 'exit', 'type')

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

        # type
        elif args[0] == "type":
            if args[1] in __pre_built_cmds:
                print('{0} is a shell builtin'.format(args[1]))
            else:
                print('{0} not found'.format(args[1]))

        else:
            print('{0}: command not found'.format(cmd))

if __name__ == "__main__":
    main()
