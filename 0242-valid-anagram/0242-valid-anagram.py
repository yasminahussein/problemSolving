class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = []
        if(len(s)!= len(t)):
            return False
        else:
            for i in s:
                counter = 0
                for j in t:
                    counter +=1
                    if (i ==j):
                       s= s.replace(i , '',1)
                       t=t.replace(j , '',1)
                       break
                    elif (counter == len(t)):
                        s_letters.append(i)
                    else:
                        continue 

            if (len(s_letters)!= 0 ) :
                return False
            else :
                return True