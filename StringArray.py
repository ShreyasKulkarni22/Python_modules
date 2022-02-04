def frequent_char(word):
    char_dict=dict()
    for letter in word:
        if letter in char_dict:
            char_dict[letter]+=1
        else:
            char_dict[letter]=1
    
    freq_char=''
    cnt_freq_char=max(char_dict.values())
    for key in char_dict:
        if char_dict[key]==cnt_freq_char:
            freq_char=key
    return freq_char

def occurs_at(word,c):
    for i in range(len(word)):
        if word[i]==c:
            break
    if word[i]==c:
        return i
    else:
        print("No such character")

def occurs_last_at(word,c):
    for i in range(len(word)-1,-1,-1):
        if word[i]==c:
            break
    if word[i]==c:
        return i
    else:
        print("No such character")

def is_palindrome(word):
    rev=word[::-1]
    if rev==word:
        return True
    else:
        return False

def is_anagram(word1,word2):
    char_dict1=dict()
    char_dict2=dict()
    for letter in word1:
        if letter in char_dict1:
            char_dict1[letter]+=1
        else:
            char_dict1[letter]=1
    
    for letter in word2:
        if letter in char_dict2:
            char_dict2[letter]+=1
        else:
            char_dict2[letter]=1

    if char_dict1==char_dict2:
        return True
    else:
        return False