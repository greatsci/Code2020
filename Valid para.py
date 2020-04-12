# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order.


class Solution(object):
  def isValid(self, input):
    """
    input: string input
    return: boolean
    """
    # write your solution here
    # 2/26 copied but modified
    # Laioffer answer might be wrong
    s = []
    match = {'(' : ')', '[' : ']', '{' : '}'}
    for p in input:
      if p in match:
        s.append(p)
      elif s and match[s[-1]] == p:
        s.pop()
      else:
        return False
    if not s:
      return True
    else:
      return False
# T: O(n)
# S: O(n)

