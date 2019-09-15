def same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    frequency_counter1 = dict()
    frequency_counter2 = dict()
    for value in arr1:
        if value in frequency_counter1:
            frequency_counter1[value] += 1
        else: frequency_counter1[value] = 1
    for value in arr2:
        if value in frequency_counter2:
            frequency_counter2[value] += 1
        else: frequency_counter2[value] = 1
    print(frequency_counter1)
    print(frequency_counter2)
    for k in frequency_counter1.keys():
        if k**2 not in frequency_counter2:
            return False
        if frequency_counter1[k] != frequency_counter2[k ** 2]:
            return False
    return True
    
    
print(same([1, 2, 3], [1, 4, 9]))
print(same([1, 2, 3, 2, 5], [9, 1, 4, 4, 11]))

def valid_anagram(first, second):
    if len(first) != len(second):
        return False
    letters = {}
    for value in first:
        if value in  letters:
             letters[value] += 1
        else: letters[value] = 1
    for val in second:
        if not letters[val]:
            return False
        else:
            letters[val] -=1;
    return True

print('anagrams')
print(valid_anagram('anagrams', 'nagarams'))
print(valid_anagram('anagrams', 'nagaramm'))