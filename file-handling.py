# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file and write some lines to it
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("Here is the second line with some numbers: 12345.\n")
            file.write("This is the third line.\n")
        print("File created and initial content written.")
    except Exception as e:
        print(f"An error occurred while creating or writing to the file: {e}")
    finally:
        print("File creation and writing process is complete.")

def read_file():
    try:
        # Read and display the contents of the file
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("You do not have permission to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("File reading process is complete.")

def append_to_file():
    try:
        # Open the file in append mode and add more lines
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line to the file.\n")
            file.write("Here is another appended line.\n")
            file.write("This is the third line appended.\n")
        print("Additional lines appended to the file.")
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("You do not have permission to write to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File appending process is complete.")

if __name__ == "__main__":
    create_file()  # Step 1: Create the file and write initial content
    read_file()    # Step 2: Read and display the file content
    append_to_file()  # Step 3: Append additional lines to the file
    read_file()    # Optionally read and display the file content again to see the appended lines
