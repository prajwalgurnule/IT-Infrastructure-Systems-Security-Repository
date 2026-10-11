#!/bin/bash

while true; do
    echo "1. Make a file"
    echo "2. Display contents"
    echo "3. Copy the file"
    echo "4. Rename the file"
    echo "5. Delete the file"
    echo "6. Exit"
    read -p "Enter your option: " choice

    case $choice in
        1)
            # Option 1: Make a file
            read -p "Enter file name to create: " filename
            if [ -e "$filename" ]; then
                echo "Error: File '$filename' already exists!"
            else
                echo "Enter contents for '$filename' (Press Enter when done):"
                read data
                echo "$data" > "$filename"
                echo "File '$filename' created and saved successfully."
            fi
            ;;

        2)
            # Option 2: Display contents
            read -p "Enter file name to display: " filename
            if [ -f "$filename" ]; then
                echo -e "\n--- Contents of '$filename' ---"
                cat "$filename"
                echo -e "-----------------------------------\n"
            else
                echo "Error: File '$filename' does not exist!"
            fi
            ;;

        3)
            # Option 3: Copy the file
            read -p "Enter source file name: " src
            if [ -e "$src" ] && [ -r "$src" ]; then
                read -p "Enter target file name: " target
                if [ -e "$target" ]; then
                    echo "Error: Target file '$target' already exists! Returning to menu."
                else
                    cp "$src" "$target"
                    echo "File copied successfully from '$src' to '$target'."
                fi
            else
                echo "Error: Source file '$src' does not exist or is not readable!"
            fi
            ;;

        4)
            # Option 4: Rename the file
            read -p "Enter source file name: " src
            if [ -e "$src" ] && [ -r "$src" ]; then
                read -p "Enter target file name: " target
                if [ -e "$target" ]; then
                    echo "Error: Target file '$target' already exists! Returning to menu."
                else
                    mv "$src" "$target"
                    echo "File renamed successfully from '$src' to '$target'."
                fi
            else
                echo "Error: Source file '$src' does not exist or is not readable!"
            fi
            ;;

        5)
            # Option 5: Delete the file
            read -p "Enter file name to delete: " filename
            if [ -e "$filename" ] && [ -w "$filename" ]; then
                read -p "Are you sure you want to delete '$filename'? (y/n): " confirm
                if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
                    rm "$filename"
                    echo "File '$filename' deleted successfully."
                else
                    echo "Deletion cancelled."
                fi
            else
                echo "Error: File '$filename' does not exist or is not writable!"
            fi
            ;;

        6)
            # Option 6: Exit
            echo "Exiting program. Goodbye!"
            exit 0
            ;;

        *)
            echo "Invalid option! Please select between 1 and 6."
            ;;
    esac
    echo ""
done
