# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List, Optional

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer
def findDuplicate(input: List[int]) -> Optional[int]:
    """
    Traverse the input list, and check if the current number within exists in a
    newly defined set. If so, return that number. If not, add the number to 
    the set and continue to traverse the input list. If no duplicate is found,
    return None. This solution is better in terms of time complexity as it 
    only traverses the list once.
    
    Time: O(N)
    Space: O(N)
    """ 
    seen_nums = set()
    for number in input:
        if number in seen_nums:
            return number
        seen_nums.add(number)
    return None
    
def findDuplicateAlternative(input: List[int]) -> Optional[int]:
    """
    Second method would be keep two pointers, i and j. We will traverse the
    list and compare the current number to every other number in the list, 
    returning a duplicate (if found). if no duplicate is found, return None
    this solution is the worst of the two, as traversing the list on each
    inner loop means the time complexity of this solution is quadratic.
    
    Time: O(N^2)
    Space: O(1)
    """
    input_length = len(input)
    for i in range(input_length):
        for j in range(i + 1, input_length):
            if input[i] == input[j]:
                return input[i]
    return None