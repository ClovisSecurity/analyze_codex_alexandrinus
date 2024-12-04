import io 

with io.open('greek-letters-raw.txt','r',encoding='utf8') as f:
    text = f.read()
# process Unicode text
#with io.open(filename,'w',encoding='utf8') as f:
#    f.write(text)
    
count = 0
output=[]
for character in text:
    if character not in output:
        output.append(character)
        count = count + 1
print("The output is:",output)
print(count)
