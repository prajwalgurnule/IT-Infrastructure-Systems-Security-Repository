#!/bin/bash
while true; do
  echo "1. Add User"
  echo "2. List number of items"
  echo "3. Check Permission"
  echo "4. List Processes"
  echo "5. Exit"
  read -p "Enter Your choice - " ch
  case "$ch" in
    1) 
          read -p "Enter username to add - " user
          useradd "$user" && echo "User $user add successfully."
          ;;
    2)
          read -p "Enter directory path - " dir
          if [ -d "$dir" ]; then
                    count=$(ls -1 "$dir" | wc -l)
                    echo "Total number of items in $dir - $count"
            else
                    echo "Invalid Directory"
            fi
            ;;
    3)
            read -p "Enter the file or path to check permission - " file
            if [ -e "$file" ]; then
                    ls -ld "$file"
            else
                    echo "Path does not exist"
            fi
            ;;
    4)
            echo "Current running process: "
            ps aux | head -n 15
            ;;
    5)
            echo "Exiting program. Goodbye !!"
            exit 0
            ;;
    *)
            echo "Invalid Input by you.. Try Again"
            ;;
  esac
done
