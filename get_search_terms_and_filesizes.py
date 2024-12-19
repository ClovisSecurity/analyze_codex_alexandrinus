import os

# Folder where search results are stored. FQDN...
path_to_dir = "C://Users//xanderinotoko//Desktop//SearchCompilation"

# Get list of filenames in directory
files_in_dir = os.listdir(path_to_dir)

# This should be changed every time you print
# This is the name of the file that the program produces
other_output_filename = 'words_with_sizes_longer.txt'

searched_word_arr = []
for filename in files_in_dir:
    found_word = filename[:len(filename) -26]
    print(found_word)
    searched_word_arr = searched_word_arr + [found_word]

def pull_word_from_filename(filename_str):
    found_word = filename_str[:len(filename_str) - 26]
    return str(found_word)


# Storing list of all files 
# in the given directory in list_of_files 
list_of_files = filter(lambda x: os.path.isfile
(os.path.join(path_to_dir, x)),
                       os.listdir(path_to_dir))

# Sort list of file names by size  
list_of_files = sorted(list_of_files,
                       key=lambda x: os.stat
                       (os.path.join(path_to_dir, x)).st_size)

# Iterate over sorted list of file  
# names and print them along with size one by one  
for name_of_file in list_of_files:
    path_of_file = os.path.join(path_to_dir, name_of_file)
    size_of_file = os.stat(path_of_file).st_size
    print(size_of_file, ' -->', name_of_file)


count_again = 1
list_of_files_set = set(list_of_files)

# write information to a file
with open(other_output_filename, "w", encoding="utf-8") as file:
    file.write("Words Searched For By File Size: \n\n")
    for name_of_file in list_of_files_set:
        path_of_file = os.path.join(path_to_dir, name_of_file)
        size_of_file = os.stat(path_of_file).st_size
        file.write(
            str(count_again) + '. ~~ ' + pull_word_from_filename(name_of_file) + '  Size: ' + str(size_of_file) + '\n')
        count_again = count_again + 1
        print(size_of_file, ' -->', name_of_file)

        # NOTE: List of Files is sorted by size
