class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(root, index):
            for i in range(index, len(word)):
                w = word[i]
                if w == '.':
                    for node in root.children.values():
                        if dfs(node, i + 1):
                            return True
                    return False
                else:
                    if w not in root.children:
                        return False
                    root = root.children[w]
            return root.word

        return dfs(self.root, 0)
                    