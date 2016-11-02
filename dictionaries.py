vocabulary_words = {"tuple":"immutable", "dictionary":"unordered", "key": "value", "list":"brackets"}



def count_letter():
    character_dict={}
    name="charmaine"

    for character in name:
        if character in character_dict.keys():
            character_dict[character] +=1
         
        else: 
            character_dict[character] =1
    return character_dict        





print count_letter()