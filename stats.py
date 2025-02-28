def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def get_character_count(file_contents):
    characters_dict = {}
    for characters in file_contents:
        characters = characters.lower()
        if characters in characters_dict:
            characters_dict[characters] += 1
        else: characters_dict[characters] = 1
    return characters_dict

def sort_character(characters_dict):
    characters_list = []
    for char, count in characters_dict.items():
        char_dict = {char: count}
        characters_list.append(char_dict)
    def sort_on(dict_item):
        char = list(dict_item.keys())[0]
        return dict_item[char]
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list



    

