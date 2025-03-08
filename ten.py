def is_file_closed(file):
    
    return file.closed

file_path = "example.txt"

file = open(file_path, "w")

print(f"Is the file closed before closing? {is_file_closed(file)}") 

file.close()

print(f"Is the file closed after closing? {is_file_closed(file)}") 
