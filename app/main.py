import sys


def main():

    __pre_built_cmds = dict()

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        cmd = input()
        if cmd not in __pre_built_cmds:
            print("{}: command not found".format(cmd))
            continue




if __name__ == "__main__":
    main()
