import sys


def main():

    # __pre_built_cmds = {
    #     "exit 0" : True,

    # }

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        cmd = input()

        # Break
        if cmd == "exit 0":
            break
    
        print("{}: command not found".format(cmd))
        continue
        




if __name__ == "__main__":
    main()
