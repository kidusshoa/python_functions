def combine_files(file1_path, file2_path, output_file):
    try:        
        with open(file1_path, "r") as file1, open(file2_path, "r") as file2, open(output_file, "w") as output:
            for line1, line2 in zip(file1, file2):
                combined_line = line1.strip() + " " + line2.strip() + "\n"
                
                output.write(combined_line)
        
        print(f"Combined file has been saved as: {output_file}")

    except FileNotFoundError:
        print("Error: One or both input files do not exist.")

file1_path = "file1.txt"
file2_path = "file2.txt"
output_file = "combined_output.txt"

combine_files(file1_path, file2_path, output_file)
