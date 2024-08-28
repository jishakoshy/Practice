# anagram -> len of 2 string are equal and all elements in str1 is present on str2

def anagram(str1,str2):
    for item in str1:
        if len(str1) == len(str2) and item in str1 and str2:
            
            print("it is anagram")

str1 = "justwait"
str2 = "waittsuj"