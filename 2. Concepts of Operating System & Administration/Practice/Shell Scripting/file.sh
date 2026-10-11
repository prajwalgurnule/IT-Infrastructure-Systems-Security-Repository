#!/bin/bash

while true; do
	echo "1. Create Directory"
	echo "2. Create file"
	echo "3. view file content"
	echo "4. Search file"
	echo "5. Change permission"
	echo "6. Exit"
	read -p "Enter option (!-5) : " ch
	case $ch in
		1)
			read -p "enter the directory name- " dir
			mkdir -p "$dir" && echo "Directory '$dir' created successfully"
			;;
		2)
			read -p "Enter file name- " name
			read -p "Enter initial text- " content
			echo "$content" > "$name" && echo "File '$name' is created successfully"
			;;
		3)
			read -p "Enter file name- " file
			if [ -f "$file" ]; then
				nl "$file"
			else
				echo "File does not exist"
			fi
			;;
		4)
			read -p " Enter the search pattern- " sh
			read -p "Enter target file path- " file
			if [ -f "$file" ]; then
				grep -n --color=auto "$sh" "$file" || echo "Filedoes not exist"
			else
				echo "File does not exist"
			fi
			;;
		5)
			read -p "Enter the file to change its permission - " f
			read -p "Enter the numeric permission - " n
			if [ -e "$file" ]; then
				chmod "$n" "$file" && echo "Permission Updated"
			else
				echo "Path does not exist."
			fi
			;;
		6)
			echo "Exit"
			exit 0;
			;;
		*)
			echo "Invalid Option"
			;;
	esac
done
