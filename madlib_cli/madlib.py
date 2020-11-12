
row = ' MadLibs Are Fun! '.center(40, '*')


def read_template(path):
    with open(path) as file:
        contents = file.read()
        stripped_contents = contents.strip()
        # print(stripped_contents)
    return stripped_contents


def parsed_madlib(contents):
    capturing = False
    string = contents
    parsed_string = ""
    speech_words = []
    current_speech_word = ""

    for char in string: 
        if not capturing:
            parsed_string += char
            if char == "{":
                capturing = True
        else:
            if char == "}":
                capturing = False
                speech_words.append(current_speech_word)
                parsed_string += char
                current_speech_word = ""
            else:
                current_speech_word += char
    # print(parsed_string, speech_words)        
    return (parsed_string, speech_words)


def user_input(parsed_string, speech_words):
    response_list = []
    
    for words in speech_words:
        response = input(f"{row}\nType the following type of word ({words})>:" )
        response_list.append(response)
    # print(response_list)
    return response_list


def merged_template(parsed_string, response_list):
    # print(stripped_template.format(*response_list)
    merged_madlib = parsed_string.format(*response_list)
    print(row)
    print(merged_madlib)
    print(row)
    return merged_madlib

def make_a_copy():
    data_for_copy = open("copy_madlib.txt", "x")
    data_for_copy.write(merged_madlib)


if __name__ == "__main__":
    file_path = "./madlib_cli/assets/template_madlib.txt"
    stripped_contents = read_template(file_path)
    parsed_string, speech_words = parsed_madlib(stripped_contents)
    response_list = user_input(parsed_string, speech_words)
    merged_madlib = merged_template(parsed_string, response_list)
    make_a_copy()