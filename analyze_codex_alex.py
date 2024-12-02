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

# Stores values to search for
ky_search_str1 = "ΚΥCΗΤ"
ky_search_str2 = "ΚΥCλΤ"
sat_search_str1 = "CλΤ"
sat_search_str2 = "CΗΤ"

# Values were CAT or CHT were found
sat_arr = []
# Values where KYCAT or KYCHT were found
kysat_arr = []
count = 0

# stores location where data was found for relative printing
sat_loc_arr = []
kysat_loc_arr = []

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

# Loop through line by line and find values we're looking for and then add them to array
for line in bible_lines_arr:
    count = count + 1
    if ky_search_str1 in line:
        kysat_arr = kysat_arr + [line]
        kysat_loc_arr = kysat_loc_arr + [count]
    if ky_search_str2 in line:
        kysat_arr = kysat_arr + [line]
        kysat_loc_arr = kysat_loc_arr + [count]
    if sat_search_str1 in line:
        sat_arr = sat_arr + [line]
        sat_loc_arr = sat_loc_arr + [count]
    if sat_search_str2 in line:
        sat_arr = sat_arr + [line]
        sat_loc_arr = sat_loc_arr + [count]

print("length of sat_arr is", len(sat_arr))
print("length of kysat_arr is", len(kysat_arr))

# This should contain location of index where value was found
print("sat_loc_arr value", str(sat_loc_arr))
print("kysat_loc_arr value", str(kysat_loc_arr))

# print lines where CAT and KYCAT were found
for line in sat_arr:
    print (line)
for line in kysat_arr:
    print (line)

# Take a slice of a timestamp for filename
slice_time = str(time.time())[:10]

# Create filename that will be used for exporting data
output_filename = output_filename + slice_time + ".txt"

# I haven't done this yet
with io.open(output_filename,'w',encoding='utf8') as f:
    f.write(sep_text)
