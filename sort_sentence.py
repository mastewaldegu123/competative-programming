class Solution:
    def sortSentence(self, s: str) -> str:
         array=s.split()
         final=[0]*len(array)
         for i in array:
             final[int(i[-1]) -1]=i[:-1]
    
         return ' '.join(final)

    
