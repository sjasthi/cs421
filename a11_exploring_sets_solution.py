#a11: Exploring Sets
# Performs a Union of Sets passed and returns the combination of sets passed
# This can be performed, either as set_1.union(set_2) or set_1 | set_2
def set_union(input_set_1,input_set_2):
    output_union_set = input_set_1.union(input_set_2)
    # output_union_set = input_set_1 | input_set_2
    return output_union_set

# Performs an Intersection of Sets passed and returns the elements common in sets passed
# This can be performed, either as set_1.intersection(set_2) or set_1 & set_2
def set_intersection(input_set_1,input_set_2):
    output_intersection_set = input_set_1.intersection(input_set_2)
    # output_intersection_set = input_set_1 & input_set_2
    return output_intersection_set

# Returns a difference between the Set of elements passed
# This can be performed, either as set_1.difference(set_2) or set_1 - set_2
def set_difference(input_set_1,input_set_2):
    output_difference_set = input_set_1.difference(input_set_2)
    # output_difference_set = input_set_1 - input_set_2
    return output_difference_set

# Returns the elements which are unique in each set passed
# This can be performed, either as set_1.symmetric_difference(set_2) or set_1 ^ set_2
def set_symmetric_difference(input_set_1,input_set_2):
    output_symmetric_difference_set = input_set_1.symmetric_difference(input_set_2)
    # output_symmetric_difference_set = input_set_1 ^ input_set_2
    return output_symmetric_difference_set

# Below are the list of liked words of myself and my son
my_words = {'chocolate', 'ice-cream', 'sports', 'movies'}
son_words = {'chocolate', 'dinosaur', 'ice-cream', 'school'}

# Find all the words me and my son like
our_union = set_union(my_words, son_words)

# Find the words me and my son like in common
our_intersection = set_intersection(my_words, son_words)

# Find the words which I like and my son doesn't
me_son_difference = set_difference(my_words, son_words)

# Find the words which my son like and I don't
son_me_difference = set_difference(son_words, my_words)

# Find the words which are not liked by each other
our_symmetric_difference = set_symmetric_difference(my_words, son_words)


print("UNION: List of words that exists in my set or my son's set")
print(*our_union)

print("INTERSECTION: List of words that exists both sets")
print(*our_intersection)

print("DIFFERENCE 1: List of words that are exclusive to me")
print(*me_son_difference)

print("DIFFERENCE 2: List of words that are exclusive to my son")
print(*son_me_difference)

print("SYMMETRIC DIFFERENCE: List of words that do not have any overlap")
print(*our_symmetric_difference)
