def most_common_word(filename: str):

    with open(filename) as file:
        content = file.read()
        content = content.strip()
        content = content.rstrip(".")
        content = content.replace("\n", " ")
        content = content.replace(".", " ")
        words = content.split(" ")
        for word in words:
            lower_limit = 0
            count = words.count(word)
            if count > lower_limit:
                lower_limit = count
                most_common = word

        return most_common
        #return {word: words.count(word) for word in words if words.count(word) >= lower_limit}    


print(most_common_word("programming.txt"))