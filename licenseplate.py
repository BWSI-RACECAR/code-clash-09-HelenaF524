"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON0123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""

from pyparsing import alphanums


class Solution:
    def licensePlate(self,str):
        # type str: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        prob = 1
        alpha = 26
        num = 10
        for i in range(len(str)):
            if str[i:i+1] != ".":
                if i<3:
                    alpha -= 1
                else:
                    num-=1
        if alpha == 24: #1 missing, 2 letters used
            prob *= alpha
        elif alpha == 25:
            prob *= alpha
            prob *= alpha-1
        elif alpha == 26: #all missing, none used
            prob*=alpha
            prob*=alpha-1
            prob*=alpha-2
        if num == 10: #all 4 missing, no nums used
            prob*=num
            prob*=num-1
            prob*= num-2
            prob*=num-3
        elif num == 9:
            prob*=num
            prob*=num-1
            prob*= num-2
        elif num == 8:
            prob*=num
            prob*= num-1
        elif num == 7:
            prob*=num
        return prob



        

def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()