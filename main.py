import UPL
import sys
import os


def main(ending):
    total = 0
    for i in os.listdir():
        if os.path.isdir(i):
            continue
        if ending == "all" or i.endswith(ending):
            data = UPL.Core.file_manager.clean_read(f"{os.getcwd()}/{i}")
            print(f"file '{i}' is {len(data)} lines")
            total += len(data)
            
    print(f"Total Lines: {total} lines (without whitespaces)")
            
if __name__ == "__main__":
    ending = "all"
    if len(sys.argv) > 1:
        ending = sys.argv[1]

    main(ending)
