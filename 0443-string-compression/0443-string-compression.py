class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("")
        t = 0
        prev = chars[0]
        ans = ""
        
        for i in chars:
            if i == prev:
                t += 1
            elif t == 1:
                ans += prev
                t = 1
            else:
                ans += prev + str(t)
                t = 1
            
            prev = i
            
        ans = [i for i in ans]   
        chars[:] = ans
        return len(chars)
                
                
            