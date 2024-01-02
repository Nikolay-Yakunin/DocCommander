import os
import shutil
import Doc

class Dir:
    
    def __init__(self, path):
        self.path = path
    
    def get_list_files(self):
        """
        Get a list of all files in the directory.

        Returns:
        - list: List of file names in the directory.
        """
        return [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

    def change_all_files(self, new_name):
        """
        Change all file names in the directory while preserving extensions.

        Parameters:
        - new_name (str): The new name to be used for all files.
        """
        for file_name in os.listdir(self.path):
            file_path = os.path.join(self.path, file_name)
            if os.path.isfile(file_path):
                doc = Doc(file_path)
                base_name, extension = os.path.splitext(file_name)
                new_file_name = f"{new_name}_{base_name}{extension}"
                doc.rename(new_file_name)

    def change_all_files_with(self, old_symbols, new_symbols):
        """
        Change all files in the directory by replacing specified characters in their names.

        Parameters:
        - old_symbols (str): Characters to be replaced.
        - new_symbols (str): Characters to replace with.
        """
        files = self.get_list_files()
        for file_path in files:
            doc = Doc(file_path)
            doc.replace_in_name(old_symbols, new_symbols)

    def copy(self, destination_path):
        """
        Copy the entire directory to a specified destination.

        Parameters:
        - destination_path (str): Path to the destination directory.
        """
        shutil.copytree(self.path, destination_path)



