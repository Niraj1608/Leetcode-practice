class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
       
        word1=s1.split()
        word2=s2.split()
        words=word1+word2
        word_cnt=Counter(words)
        ans=[word for word in word_cnt if word_cnt[word]==1]

                            

        return ans
