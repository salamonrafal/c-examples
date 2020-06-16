import subprocess
import re
import os
from pathlib import Path
import fnmatch
import shutil

__all__ = [
        'BUILD_DIR', 
        'VERSION_DIR', 
        'create_directory', 
        'get_tags', 
        'check_directory_exists', 
        'check_and_create_directory',
        'move_filtered_files'
    ]

def get_tags():
    """Retrive tag from git use shell

    Returns:
        string: git tag
    """
    
    shell = subprocess.run(['git', 'for-each-ref', 'refs/tags', '--sort=-taggerdate', '--format=\'%(refname)\'', '--count=1'], stdout=subprocess.PIPE, text=True)

    return clean_tag(shell.stdout)

def clean_tag(raw_tag: str):
    """Clean string returned from shell

    Args:
        raw_tag (string): String returned from shell

    Returns:
        string: [description]
    """

    reg = re.compile("'(refs/tags/)([^']*)'")
    match = reg.search(raw_tag)

    return match[2]

def create_directory(dir_path: str):
    """ Create directory for specific name

    Args:
        dir_path (string): [description]

    Returns:
        boolean: Is success created directory
    """

    try:
        os.mkdir(dir_path)
    except OSError:
        return True
    else:
        return False

def check_directory_exists(dir_path: str):
    """Check if directory exists
    Args:
        dir_path (str): Path to directory

    Returns:
        [boolean]: True if directory exists. Otherwise False
    """

    if os.path.exists(dir_path):
        return True
    else:
        return False

def check_and_create_directory(dir_path: str):
    """Checking and if directory not exists then creating

    Args:
        dir_path (str): directory path

    Returns:
        [str]: Path to directory
    """

    if (not check_directory_exists(dir_path)):
        create_directory(dir_path)

    return dir_path

def move_filtered_files(src_dir: str, dst_dir: str, pattern: str = "*.exe"):
    """Move matched files to destination folder

    Args:
        src_dir (str): Source directory
        dst_dir (str): Destination directory
        pattern (str, optional): Pattern for filtering files to move. Defaults to "*.exe".

    Returns:
        [boolean]: Return True if move to destination directory finished with success.
    """

    if os.path.isdir(dst_dir):
        for f in fnmatch.filter(os.listdir(src_dir), pattern):
            shutil.move(os.path.join(src_dir, f), os.path.join(dst_dir, f))

        return True
    else:
        return False


BUILD_DIR = 'builds'
VERSION_DIR = get_tags()