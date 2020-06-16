import libs

def create_build_directories():
    currentPathToBuild =libs.check_and_create_directory(libs.BUILD_DIR)
    currentPathToBuild = libs.check_and_create_directory(libs.BUILD_DIR + '/' + libs.VERSION_DIR) 

    return currentPathToBuild

print(create_build_directories())