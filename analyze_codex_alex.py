import time
import io
##########################################################################################
################### The Following Alphabet Can Be Used to Search: ########################
##########################################################################################
###  ALPHABET:
### λ, B, Γ, Ε, C, Υ, Χ, ι, Ο, Θ, Η, Ρ, λ, Δ, Τ, Ξ, Ζ, K, ψ, Ν, Φ, ω
###
### The only characters available to use for flex searches are below:
### FLEX ALPHABET:
### B, Γ, Υ, ι(Also MARK INDICATOR), Ο(C, E, Θ), Η(N), Ρ, λ(α, Δ), Τ, Ξ, Ζ, K, ψ, Φ, ω, Χ
###########################################################################################
###########################################################################################

# Stores 2 version of values to search for
# NOTE: THE SECOND VALUE MUST BE INCLUDED OR YOU CAN MAKE AN EMPTY "" in place
word_search_str1 = "CλΤ"

# Values where CAT or CHT were found
word_arr = []

# Counter for determining location in array
count = 0

# stores location where data was found for relative printing
word_loc_arr = []

# You can change the name of this file to use the code on different files.
# NOTE: All files must be in the same directory
# This must be the full name of file
bible_filename = 'best-codec-ocr-stripped.txt'

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
print("word_loc_arr value", str(word_loc_arr))

# print lines where CAT and KYCAT were found
for line in word_arr:
    print(line)

# Take a slice of a timestamp for filename
slice_time = str(time.time())[:10]

# Create filename that will be used for exporting data
output_filename = output_filename + slice_time + ".txt"

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

            # Create
            section1 = str(index_tup_arr[counter_tup - 4][1])
            section2 = str(index_tup_arr[counter_tup - 3][1])
            section3 = str(index_tup_arr[counter_tup - 2][1])
            section4 = str(index_tup_arr[counter_tup - 1][1])
            section5 = str(index_tup_arr[counter_tup - 0][1])
            section6 = str(index_tup_arr[counter_tup + 1][1])
            section7 = str(index_tup_arr[counter_tup + 2][1])
            section8 = str(index_tup_arr[counter_tup + 3][1])
            section9 = str(index_tup_arr[counter_tup + 4][1])
            section10 = str(index_tup_arr[counter_tup + 5][1])

            concat_str_entry = section1 + section2 + section3 + section4 + section5 + section6 + section7 + section8 + section9 + section10
            print(concat_str_entry)

    counter_tup = counter_tup + 1
