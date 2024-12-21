import time
import io
import os
####################################################################################################################
##################### The Following Alphabet Can Be Used to Search Greek Docs: #####################################
####################################################################################################################
#####  ALPHABET:                                                                                               #####
#####  λ, B, Γ, Ε, C, Υ, Χ, ι, Ο, Θ, Η, Μ, Ρ, λ, Δ, Τ, Ξ, , K, ψ, Ν, Φ, ω, ΚΥ, Π, N                            #####
#####                                                                                                          #####
##### The only characters available to use for flex searches are below:                                        #####
##### FLEX ALPHABET:                                                                                           #####
##### B, Γ, Υ, ι(Also MARK INDICATOR), Ο(C, E, Θ), Η(N), Ρ, Μ, λ(α, Δ), Τ, Ξ, Ζ, K, ψ, Φ, ω, Χ, Π              #####
#####                                                                                                          #####
##### English Search Alphabet:                                                                                 #####
##### A, B, Q, E, D, F, I, J, K, λ, L (for Theta),R (rho), P (pi), M, N, T, Z, PS, O (omega), @ (omicron), X,  #####
####################################################################################################################
####################################################################################################################

# Stores value to search for λλRλREUT
word_search_str1 = 'PAIAE'

# Values where CAT or CHT were found
word_arr = []

# Counter for determining location in array
count = 0

# stores location where data was found for relative printing
word_loc_arr = []

# You can change the name of this file to use the code on different files.
# NOTE: All files must be in the same directory
# This must be the full name of file
bible_filename = 'codex-12-19-5AM.txt'

# All results stored in same directory
output_dest_dir = './eng-codex-search-results/'


# The Bible you import will be stored here
bible_lines_arr = []

# This filename will be changed based on the timestamp
# This should not be the full name of file
output_filename = 'search_bible'

# Open file and store lines in array
with open(bible_filename,'r',encoding='utf8') as file:
    for item in file:
        if len(item) != 0:
            bible_lines_arr = bible_lines_arr + [item]

index_tup_arr = []
filtered_index_tup_arr = []

# Loop through line by line and find values we're looking for and then add them to array
for line in bible_lines_arr:
    index_tup_arr = index_tup_arr + [(count, line)]
    if word_search_str1 in line:
        word_arr = word_arr + [line]
        word_loc_arr = word_loc_arr + [count]
        filtered_index_tup_arr = filtered_index_tup_arr + [(count, line)]

    count = count + 1

print("length of word_arr is", len(word_arr))

# This should contain location of index where value was found
# print("word_loc_arr value", str(word_loc_arr))

# print lines where CAT and KYCAT were found
#for line in word_arr:
#    print(line)



goal_arr = []
counter_tup = 0


# trying to access text surrounding the pattern matches that
# we detected during the word search
for larger_text in index_tup_arr:
    # print(larger_text[0]) # all indices
    for smaller_text in filtered_index_tup_arr:
        if smaller_text[0] == larger_text[0]:
            # these return the same value so.. we can use the counter_tup for relative printing
            #            |                   |
            #            v                   v
            # print(larger_text + index_tup_arr[counter_tup])

            # get lines surrounding the word the users searched for   
            try:
                section0 = str(index_tup_arr[counter_tup - 5][1])  
            except IndexError:
                pass
            try:
                section1 = str(index_tup_arr[counter_tup - 4][1])  
            except IndexError:
                pass
            try:
                section2 = str(index_tup_arr[counter_tup - 3][1])  
            except IndexError:
                pass
            try:
                section3 = str(index_tup_arr[counter_tup - 2][1])  
            except IndexError:
                pass
            try:
                section4 = str(index_tup_arr[counter_tup - 1][1])  
            except IndexError:
                pass
            try:
                section5 = str(index_tup_arr[counter_tup][1])  
            except IndexError:
                pass
            try:
                section6 = str(index_tup_arr[counter_tup + 1][1])  
            except IndexError:
                pass
            try:
                section7 = str(index_tup_arr[counter_tup + 2][1])  
            except IndexError:
                pass
            try:
                section8 = str(index_tup_arr[counter_tup + 3][1])  
            except IndexError:
                pass
            try:
                section9 = str(index_tup_arr[counter_tup + 4][1])  
            except IndexError:
                pass
            try:
                section10 = str(index_tup_arr[counter_tup + 5][1])  
            except IndexError:
                pass
            try:
                section11 = str(index_tup_arr[counter_tup + 6][1])  
            except IndexError:
                pass           
            
            
            

            # Concatenates fields near the field where the value searched for was found.
            concat_str_entry = section0 + section1 + section2 + section3 + section4 + section5 + section6 + section7 + section8 + section9 + section10 + section11

            # print(concat_str_entry)

            goal_arr = goal_arr + [concat_str_entry]

    counter_tup = counter_tup + 1

# print(goal_arr)

# Replace all occurences of search string with string surrounded by spaces.
replace_str = ' **' + word_search_str1 + '** '

new_arr = []

for item in goal_arr:
    replaced_str = item.replace(word_search_str1, replace_str)
    if word_search_str1 in item:
        new_arr = new_arr + [replaced_str]
    else:
        new_arr = new_arr + [item]
        
# Take a slice of a timestamp for filename
slice_time = str(time.time())[:10]

if os.path.isdir(output_dest_dir):
    print(f"Directory '{output_dest_dir}' exists.\n\nSaving Search Results...\n\nResults Saved")
else:
    os.mkdir(output_dest_dir)
 

# Create filename that will be used for exporting data
output_filename = output_dest_dir + word_search_str1 + output_filename + slice_time + ".txt"

# Include helpful information in output
top_of_doc = '\nHere are the Search Results for ' + word_search_str1 + ' in ' + bible_filename + '\n\n'
count_line = 'There were ' + str(len(goal_arr)) + ' occurences of ' + word_search_str1 + ' in the document\n\n'
top_line = top_of_doc + count_line

# write information to a file
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(top_line)
    for line in new_arr:
        # Write each line to the file, adding a newline character
        file.write(line + "\n" + "\n*****************************************************\n**********************************************************\n\n")

print(word_search_str1)
