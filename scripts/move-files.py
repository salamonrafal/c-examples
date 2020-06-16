import libs


def move_build_files():
    """Move builds files to correct version
    """
    src = libs.BUILD_DIR
    dst = src + '/' + libs.VERSION_DIR

    if not libs.move_filtered_files(src, dst):
        print("Error during move files")

    return

move_build_files()