import UPL
import sys
import os


def main(ending):
    total = 0
    for i in os.listdir():
        if os.path.isdir(i):
            continue
        if ending == "all" or i.endswith(ending):
            data = len(UPL.Core.file_manager.read_file(f"{os.getcwd()}/{i}"))
            print(f"file '{i}' is {data} lines")
            total += data
    print(f"Total Lines: {total} lines")
            
if __name__ == "__main__":
    ending = "all"
    if len(sys.argv) > 1:
        ending = sys.argv[1]

    main(ending)