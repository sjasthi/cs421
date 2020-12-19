#Assignment 8: Implement isPalindrome and isAnagram methods
#Assignment 8: Test for both positive and negative cases


# Panlindrome:  See  https://en.wikipedia.org/wiki/Palindrome#Characters,_words,_or_lines 
# This function returns "TRUE" if the given word is a palindrome
#           else it returns "FALSE"
def  isPalindrome(word):
    # reverse the input word using the slicing
    reversed_word = word[::-1]
    
    #comapre the two. Result will be True or False
    result = (word == reversed_word)
   
    #return the result   
    return result
   

# NOTE: This cryptic one line implementation is equivalent to the above method   
# def isPalindrom(word):
#       return (word == word[::-1])


# Anagram:  See  https://en.wikipedia.org/wiki/Anagram 
# This function returns "TRUE" if the two words are Anagrams
#           else it returns "FALSE"
def  areAnagrams(word_1, word_2):
   # convert the inputs to lists
   word_1_list = list(word_1)
   word_2_list = list(word_2)
   
   # sort those lists
   word_1_list.sort()
   word_2_list.sort()
   
   #compared the two lists. Result will be True or False
   result = (word_1_list == word_2_list)
   
   #return the result
   return result

# NOTE: This cryptic one line implementation is equivalent to the above method   
# def  areAnagrams(word_1, word_2):
#       return (list(word_1).sort() == list(word_2).sort())


#  Test cases for the two functions

# Palindrome positive test cases (should return TRUE)
# radar, level, rotor, kayak, racecar, madam
x = isPalindrome("radar")
print("is radar palindrome? = ",  x)

# Palindrome positive test cases (should return FALSE)
# python, java, silc
x = isPalindrome("python")
print("is python palindrome? = ",  x)



# Anagram positive test cases (should return TRUE)
# evil=vile,  silent=listen,  eleven plus two=twelve plus one
word_x = "silent"
word_y = "listen"
result = areAnagrams(word_x, word_y)
print("Are ", word_x, " and ", word_y," anagrams? = ", result)


# Anagram positive test cases (should return FALSE)
# python = pxthon, java = lava, a = abcdefghijklmnopqrstuvwxyz
word_x = "python"
word_y = "pxthon"
result = areAnagrams(word_x, word_y)
print("Are ", word_x, " and ", word_y," anagrams? = ", result)
