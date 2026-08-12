class Solution:

    def encode(self, strs: List[str]) -> str:
        combine = ''
        for x in strs:
            combine += x + ':;'
        combine += str(len(strs))
        print(combine)
        return combine

    def decode(self, s: str) -> List[str]:
        words = s.split(':;')
        return words[:int(words[-1])]
