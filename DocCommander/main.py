from tkinter import Tk
from FileUtilityUI import FileUtilityUI


def main():
    root = Tk()
    app = FileUtilityUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()