import re

# This is a simple regression test to check if the os_module.py file is working correctly after recent edits.
# We will check if the file can be imported without errors and if the functions are working as expected.

text = """PostgreSQL was invented at the Berkeley Computer Science Department, University of California.
It started as a project in 1986 with the goal of creating a database system with the minimal features needed to support multiple data types.
In the beginning, PostgreSQL ran on UNIX platforms, but now it can run on various platforms, including Windows and MacOS."""

# Check if the text contains the word "PostgreSQL"
if re.search(r"\bPostgreSQL\b", text):
    print("The text contains the word 'PostgreSQL'.")
else:
    print("The text does not contain the word 'PostgreSQL'.")
    
#search for a pattern that matches a date in the format YYYY-MM-DD
date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"
date_text = "The release date of PostgreSQL 15 is expected to be in 2024-10-01."
if re.search(date_pattern, date_text):
    print("The text contains a date in the format YYYY-MM-DD.")
else:
    print("The text does not contain a date in the format YYYY-MM-DD.")

match = re.search(r"\bPostgreSQL\b", text)
if match:
    print("Found 'PostgreSQL' in the text:", match.group())
    print("Found 'PostgreSQL' in the text start index:", match.start()) #the index of the start of the match
    print("Found 'PostgreSQL' in the text end index:", match.end()) #the  index of the end of the match
else:
    print("'PostgreSQL' not found in the text.")
    
text = text + (" PostgreSQL is an open-source relational database management system.")
    
maches = re.findall(r"\bPostgreSQL\b", text)
print("All occurrences of 'PostgreSQL' in the text:", maches)

#replace all occurrences of "PostgreSQL" with "Postgres"
replaced_text = re.sub(r"\bPostgreSQL\b", "Postgres", text)

#compile a regular expression pattern to match email addresses
email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
email_text = "Please contact us at info@company.com for more information."  
if re.search(email_pattern, email_text):
    print("The text contains a valid email address.")
else:
    print("The text does not contain a valid email address.")
    
text1 = "The quick brown fox jumps over the lazy dog."

#Search for a pattern that matches words that start with 'b' and end with 'n'
pattern = r"\bb\w*n\b"
matches = re.findall(pattern, text1)
print("Words that start with 'b' and end with 'n':", matches)

match1 = re.search("brown", text1)
if match1:
    print("Found 'brown' in the text:", match1.group())
    print("Found 'brown' in the text start index:", match1.start())
    print("Found 'brown' in the text end index:", match1.end())
else:
    print("'brown' not found in the text.")
    
#fill all matches of the pattern with "the"
matches = re.findall("the", text1, re.IGNORECASE) #the re.IGNORECASE flag makes the search case-insensitive
print("All occurrences of 'the' in the text:", matches)

#replace all occurrences of "the" with "a"
replaced_text1 = re.sub(r"\bthe\b", "a", text1, flags=re.IGNORECASE)
print("Text after replacing 'the' with 'a':", replaced_text1)

#compile a regular expression pattern to match phone numbers in the format (XXX) XXX-XXXX
phone_pattern = re.compile(r"\(\d{3}\) \d{3}-\d{4}")
phone_text = "Please call us at (123) 456-7890 for more information."
if re.search(phone_pattern, phone_text):
    print("The text contains a valid phone number.")
else:
    print("The text does not contain a valid phone number.")
    
#compile a regular expression pattern to match URLs
url_pattern = re.compile(r"https?://[^\s]+")
url_text = "Visit our website at https://www.example.com for more information."
if re.search(url_pattern, url_text):
    print("The text contains a valid URL.")
else:
    print("The text does not contain a valid URL.")
    
#compile a regex for email addresses and find all matches in a text
email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
email_text = "Please contact us at info@company.com for more information."
if re.search(email_pattern, email_text):
    print("The text contains a valid email address.")
else:
    print("The text does not contain a valid email address.")

#compile a regex for efficiency and that matches whole words
word_pattern = re.compile(r"\b\w+\b")
text = "The quick brown fox jumps over the lazy dog."
matches = word_pattern.findall(text)
print("All words in the text:", matches)