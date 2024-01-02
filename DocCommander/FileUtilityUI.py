from tkinter import Tk, Label, Button, Entry, filedialog
from Dir import Dir
import os

class FileUtilityUI:
    def __init__(self, master):
        self.master = master
        master.title("File Utility App")

        self.label = Label(master, text="Directory Path:")
        self.label.grid(row=0, column=0)

        self.directory_path_entry = Entry(master)
        self.directory_path_entry.grid(row=0, column=1)

        self.browse_button = Button(master, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2)

        self.list_files_button = Button(master, text="List Files", command=self.list_files)
        self.list_files_button.grid(row=1, column=0)

        self.rename_files_button = Button(master, text="Rename Files", command=self.rename_files)
        self.rename_files_button.grid(row=1, column=1)

        self.replace_chars_button = Button(master, text="Replace Characters", command=self.replace_chars)
        self.replace_chars_button.grid(row=1, column=2)

        self.copy_directory_button = Button(master, text="Copy Directory", command=self.copy_directory)
        self.copy_directory_button.grid(row=2, column=1)

    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        self.directory_path_entry.delete(0, 'end')
        self.directory_path_entry.insert(0, directory_path)

    def list_files(self):
        directory_path = self.directory_path_entry.get()
        if os.path.exists(directory_path):
            directory = Dir(directory_path)
            files_list = directory.get_list_files()
            for file in files_list:
                print(file)
        else:
            print("Directory not found.")

    def rename_files(self):
        directory_path = self.directory_path_entry.get()
        new_name = "new_name"
        if os.path.exists(directory_path):
            directory = Dir(directory_path)
            directory.change_all_files(new_name)
            print(f"All files in the directory have been renamed to '{new_name}'.")
        else:
            print("Directory not found.")

    def replace_chars(self):
        directory_path = self.directory_path_entry.get()
        old_symbols = "_"
        new_symbols = "-"
        if os.path.exists(directory_path):
            directory = Dir(directory_path)
            directory.change_all_files_with(old_symbols, new_symbols)
            print(f"All files in the directory have been renamed by replacing '{old_symbols}' with '{new_symbols}'.")
        else:
            print("Directory not found.")

    def copy_directory(self):
        directory_path = self.directory_path_entry.get()
        destination_path = filedialog.askdirectory()

        try:
            if not os.path.exists(directory_path):
                raise FileNotFoundError(f"Source directory not found: {directory_path}")

            

            directory = Dir(directory_path)
            directory.copy(destination_path)
            print(f"The directory has been copied to '{destination_path}'.")

        except FileNotFoundError as e:
            print(f"Error: {e}")

        except FileExistsError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    root = Tk()
    app = FileUtilityUI(root)
    root.mainloop()