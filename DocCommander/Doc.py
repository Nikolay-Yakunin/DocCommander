import os
import shutil

class Doc:
    
    def __init__(self, path):
        self.path = path

    def rename(self, new_name):
        new_path = os.path.join(os.path.dirname(self.path), new_name)
        os.rename(self.path, new_path)
        self.path = new_path
        
    def replace_in_name(self, old_symbols, new_symbols):
        """
        Replace specified characters in the file name.

        Parameters:
        - old_symbols (str): Characters to be replaced.
        - new_symbols (str): Characters to replace with.

        Example:
        doc.replaceInName('_', '-')
        """
        file_dir, file_name = os.path.split(self.path)
        new_file_name = file_name.replace(old_symbols, new_symbols)
        new_path = os.path.join(file_dir, new_file_name)

        # Rename the file
        os.rename(self.path, new_path)
        self.path = new_path

    def replace(self, new_content):
        with open(self.path, 'w') as file:
            file.write(new_content)

    def delete(self):
        os.remove(self.path)

    def copy(self, destination_path):
        shutil.copy2(self.path, destination_path)


