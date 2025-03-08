def read_file_line_by_line(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        
file_name = "software.txt"
read_file_line_by_line(file_name)
