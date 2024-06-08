import sys


def main():

    __pre_built_cmds = dict()

    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    cmd = input()

    if cmd not in __pre_built_cmds:
        print("{}: command not found".format(cmd))



if __name__ == "__main__":
    main()
