import sys


def main() -> None:
    print("=== Command Quest ===")

    print(f"Program name: {sys.argv[0]}")

    total_args = len(sys.argv)

    if total_args == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_args - 1}")

        user_args = sys.argv[1:]

        i = 1
        while i <= len(user_args):
            print(f"Argument {i}: {user_args[i-1]}")
            i += 1

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
