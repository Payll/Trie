class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True

    def search(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_word

    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True

    def display_to_md(self, filename="trie_visualization.md"):
        def dfs(node, path, parent="root"):
            if node.is_word:
                words.append(("".join(path), parent))  # record the word and its parent node
            for letter, next_node in node.children.items():
                child = "".join(path + [letter])
                dfs(next_node, path + [letter], child)
                edges.add((parent, child, letter))

        words = []  # List of words and their parent nodes
        edges = set()  # Set of edges (parent, child, letter)
        dfs(self.root, [])
        with open(filename, "w") as file:
            file.write("# Trie Visualization\n\n```mermaid\ngraph TD\n")
            for parent, child, letter in edges:
                if child.endswith("*"):  # Check if it is the end of a word
                    child = child.rstrip("*") + "(*end*)"
                file.write(f"{parent} --> |{letter}| {child}\n")
            file.write("```\n")


trie = Trie()

with open("frequence.csv") as f:
    lines= f.readlines()

    for line in lines[:10]:
        word = line.strip()
        trie.insert(word)

# Searching for a word
print(trie.search("an"))
print(trie.search("and"))

# Displaying the trie
trie.display_to_md()
