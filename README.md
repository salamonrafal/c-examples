# C-EXAMPLES

This is template for Visual code with configured ```task.json``` for build C/C++ code.

## REQUIRAMENTS

* Installed MinGW
* Python ^3.7.X
* Visual Studio Code

## Tasks

* Single tasks:
  * _pre:builds_dir - Create builds directories
  * _build:env:production - Execute compiler for production configuration and create .exe file in build directory
  * _build:env:development - Execute compiler for development configuration and create .exe file in build directory
  * _post:move_files - Move .exe files to correct version directory
* Grouped tasks:
  * build:development - building devewlopment .exe file
  * build:production - building production .exe file
