def readFile(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def countWords(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(reportData, totalWords):
    print("The total words in this book are: " + str(totalWords))

    for item in reportData:
        if item["char"].isalpha():        
            print("The " + item["char"] + " character was found " + str(item["num"]) + " times")

    print("--- End report ---")

def main():
    path_to_file = "./books/frankenstein.txt"
    
    print("--- Start report for " + path_to_file + " ---")
    text = readFile(path_to_file)

    wordCount = countWords(text)
    char_dict = get_chars_dict(text)
    
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)

    print_report(chars_sorted_list, wordCount)


main()