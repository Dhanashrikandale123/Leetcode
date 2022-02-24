'''3. Longest Substring Without Repeating Characters
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''

def lengthOfLongestSubstring(s):
   charset=set()
   left=0
   result=0
   for right in range(len(s)):
       while s[right]in charset:
           charset.remove(s[left])
           left+=1
       charset.add(s[right])
       result=max(result,right-left+1)
   print(result)
           
s="bbbbb"
lengthOfLongestSubstring(s)
