# DocCommander Readme

This document provides an overview of the DocCommander App, a Python application designed to perform various file and directory operations. The app is implemented using the Tkinter library for the graphical user interface.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Classes](#classes)
    - [Doc](#doc-class)
    - [Dir](#dir-class)
3. [User Interface](#user-interface)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [Autor](#autor)
7. [Contributing](#contributing)
8. [License](#license)

## Project Structure<a name="project-structure"></a>

The project is organized into three Python files:

1. **Doc.py:** Contains the `Doc` class, which represents individual documents (files) and provides methods for renaming, replacing characters in the name, replacing content, deleting, and copying files.

2. **Dir.py:** Contains the `Dir` class, which represents directories and provides methods for obtaining a list of files, renaming all files in a directory, replacing characters in the names of all files, and copying the entire directory.

3. **FileUtilityUI.py:** Implements the Tkinter-based graphical user interface for the File Utility App.

## Classes<a name="classes"></a>

### Doc Class<a name="doc-class"></a>

The `Doc` class represents individual documents (files) and provides the following methods:

- `__init__(self, path)`: Initializes the Doc object with the specified file path.
- `rename(self, new_name)`: Renames the document with the new specified name.
- `replace_in_name(self, old_symbols, new_symbols)`: Replaces specified characters in the file name.
- `replace(self, new_content)`: Replaces the content of the document with the specified content.
- `delete(self)`: Deletes the document.
- `copy(self, destination_path)`: Copies the document to the specified destination path.

### Dir Class<a name="dir-class"></a>

The `Dir` class represents directories and provides the following methods:

- `__init__(self, path)`: Initializes the Dir object with the specified directory path.
- `get_list_files(self)`: Returns a list of all files in the directory.
- `change_all_files(self, new_name)`: Changes all file names in the directory while preserving extensions.
- `change_all_files_with(self, old_symbols, new_symbols)`: Changes all files in the directory by replacing specified characters in their names.
- `copy(self, destination_path)`: Copies the entire directory to a specified destination.

## User Interface<a name="user-interface"></a>

The graphical user interface (GUI) is implemented using Tkinter and provides the following functionalities:

- Browse for a directory.
- List all files in the selected directory.
- Rename all files in the directory to a specified name.
- Replace characters in the names of all files in the directory.
- Copy the entire directory to a specified destination.

## Usage<a name="usage"></a>

1. Run the main.py script.
2. Use the "Browse" button to select a directory.
3. Perform various file and directory operations using the provided buttons.

## Dependencies<a name="dependencies"></a>

The application relies on the following dependencies:

- **os:** Standard Python module for interacting with the operating system.
- **shutil:** Standard Python module for file operations.
- **tkinter:** Standard Python GUI toolkit.

## Autor<a name="autor"></a>

- Nikolay-Yakunin

## Contributing<a name="contributing"></a>

Contributions to the File Utility App are welcome. If you have any improvements or suggestions, feel free to submit a pull request.

## License<a name="license"></a>

The File Utility App is open-source software licensed under the [MIT License](LICENSE).
