import re
string = 'Zero:0 one:1 Two:2 Three:3 Four:4 Five:5 Six:6 Seven:7 eight:8 Nine:9 Ten:10 Twenty:20 Thirty:30 Forty:40 Fifty:50 Sixty:60 Seventy:70 Eighty:80 Ninety:90 Hundred:100'  
regex = '\d+' 
# This statement splits the string on the basis of matching values between pattern and string.      
splitval = re.split(regex, string)
print(splitval)

string = 'a1 \nb2 \nc4'  
pattern = '\d' # This statement defines the regular expression for matching with the string.  
 
# empty string  
replace = 's'  
# This statement replaces those matched characters with a string stored in a replace variable.
new_string = re.sub(pattern, replace, string)   

# This statement displays the new string after the replacement of characters.      
print(new_string)      



text = "Regular Expression is also referred as Regex. "  
regex= "\d"  
res = re.search(regex, text)   # This statement searches the regular expression in a string.   
if res:  
  print("Regular expression found inside the string")  
else:  
  print("Regular expression not found inside the String")  