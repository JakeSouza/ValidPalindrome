'''
Created on Jan 5, 2018

@author: Jake
'''
import string
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #if empty return True
        if(len(s) == 0):
            return True
        #two lists containing all valid characters
        alphabet = list(string.ascii_lowercase)
        number = ["1","2","3","4","5","6","7","8","9","0"]
        #make sure that all letters are lowercase to check properly
        temp = list(s.lower())
        
        arr = []
        #turn string into a list
        for x in temp:
            if(x in alphabet or x in number):
                arr.append(x)  
        #if new list is empty return True       
        if(len(arr) == 0):
            return True
        #if only contains two things, check to see if they're equal
        elif(len(arr) == 2):
            if(arr[0] == arr[1]):
                return True
            else:
                return False
        #more than 2 items in list
        else:
            first = 0
            last = len(arr) - 1
            #use two pointers to check from front to back 
            while(first != last and last > first):
                if(arr[first] != arr[last]):
                    return False
                else:
                    first += 1
                    last -= 1
                    
            return True