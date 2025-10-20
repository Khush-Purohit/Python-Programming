text = input("Enter text: ")
original_length = len(text)



def clean_review(text):
    text = text.lower()
    # print(text)
    modified_Text = ""
    word_count = 0
    for i in text:
        # if(i.isalpha()):
        #     # word_count+=1
        #     modified_Text+=i
        # if(i == ' '):
        #     modified_Text+=i

        if(i.isalpha() or i == ' '):
            # word_count+=1
            modified_Text+=i
        # if(i == ' '):
        #     modified_Text+=i

    # print(f'modified_Text: {modified_Text}')
    return modified_Text

modified_Text = clean_review(text)

word_count = len(modified_Text.split())

unique_words = set(modified_Text.split())
unique_words = len(unique_words)

print("Analysis: ")
print(f"Original Text: {text}")
print(f"Cleaned Text: {modified_Text}")
print(f"Original Length: {original_length}")
print(f"Word Count: {word_count}")
print(f"Unique words: {unique_words}")
    
