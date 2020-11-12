
def read_template():
    with open('./madlib_cli/assets/template_madlib.txt', 'r') as file:
        contents = file.read()
        print(contents)
        print('File is closed.', file.closed)
    return contents

originalContent = read_template()

def parsed_madlib(contents):
    string = "a {adjective} and not and {noun}, so yeah..."
    found = ""
    foundWords = []
    for char in string(0, len(string)): 
        if char == "{":
            found = str(found[i])
            found = string1.replace(i, '')
        print(foundWords)

# substring = parsed_madlib(originalContent)


# text = 'I want to find a string between two substrings' left = 'find a ' right = 'between two' # Output: 'string' print text[text.index(left)+len(left):text.index(right)]

# How to get the substring between two markers in Python, Use indexing to get substring between two markers​​ To get where the substring starts, add len (start_marker) to string. find (start_marker) to get the index at which start marker ends. The substring ends at the start of the end marker.

# Regular expressions are the most flexible option. How to get string between two delimiters python. 0. Extract Parts of String from in Between Two Characters-1.

# with open('assets/template_madlib.copy', 'w') as f2:
#     f2.write(trimmed)
