import os
path_to_dir = "C://Users//xanderinotoko//Desktop//bible-work//edited-septuagints//eng-codex-search-results"

files_in_dir = os.listdir(path_to_dir)

output_filename = 'list_of_words_searched.txt'

searched_word_arr = []
for filename in files_in_dir:
    found_word = filename[:len(filename) -26]
    print(found_word)
    searched_word_arr = searched_word_arr + [found_word]

len(searched_word_arr)

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

    # NOTE: List of Files is sorted by size

def pull_word_from_filename(filename_str):
    found_word = filename_str[:len(filename_str) - 26]
    return str(found_word)

# print(list_of_files)

ordered_word_list = []

for filename_str in list_of_files:
    pulled_word = pull_word_from_filename(filename_str)
    ordered_word_list = ordered_word_list + [pulled_word]

print(ordered_word_list)


# write information to a file
with open(output_filename, "w", encoding="utf-8") as file:
    file.write("Here are the Words that Have Been Searched: \n\n")
    for line in ordered_word_list:
        # Write each line to the file, adding a newline character
        file.write(line + '\n')
