import sys
import os

def main():
    # Define built-in commands
    builtin_cmds = ["echo", "exit", "type"]

    # Get the system PATH environment variable
    PATH = os.environ.get("PATH")

    while True:
        # Prompt for user input
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input()

        # "exit 0"
        if user_input == "exit 0":
            break

        # "echo" command
        if user_input.startswith("echo"):
            content = user_input.split(" ", 1)
            if len(content) > 1:
                sys.stdout.write(content[1] + "\n")
            else:
                sys.stdout.write("\n")
            sys.stdout.flush()
            continue

        # "type" command
        if user_input.startswith("type"):
            cmd = user_input.split(" ")[1]
            cmd_path = None
            paths = PATH.split(":")

            # Search for the command in the system PATH
            for path in paths:
                if os.path.isfile(f"{path}/{cmd}"):
                    cmd_path = f"{path}/{cmd}"
                    break

            if cmd in builtin_cmds:
                sys.stdout.write(f"{cmd} is a shell builtin\n")
            elif cmd_path:
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
            else:
                sys.stdout.write(f"{cmd} not found\n")
            sys.stdout.flush()
            continue

        sys.stdout.write(f"{user_input}: command not found\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
