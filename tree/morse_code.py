table = [
    ("A", ".-"),
    ("B", "-..."),
    ("C", "-.-."),
    ("D", "-.."),
    ("E", "."),
    ("F", "..-."),
    ("G", "--."),
    ("H", "...."),
    ("I", ".."),
    ("J", ".---"),
    ("K", "-.-"),
    ("L", ".-.."),
    ("M", "--"),
    ("N", "-."),
    ("O", "---"),
    ("P", ".--."),
    ("Q", "--.-"),
    ("R", ".-."),
    ("S", "..."),
    ("T", "-"),
    ("U", "..-"),
    ("V", "...-"),
    ("W", ".--"),
    ("X", "-..-"),
    ("Y", "-.--"),
    ("Z", "--.."),
]


def encode(ch):
    idx = ord(ch) - ord("A")
    return table[idx][1]


def decode_slow(code):
    for e in table:
        if code == e[1]:
            return e[0]
    return None


class TNode:
    def __init__(self, elem, left, right):
        self.data = elem
        self.left = left
        self.right = right


def make_morse_tree():
    root = TNode(None, None, None)

    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == ".":
                if node.left is None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == "-":
                if node.right is None:
                    node.right = TNode(None, None, None)
                node = node.right

        node.data = tp[0]
    return root


def decode(root, code):
    mode = root
    for c in code:
        if c == ".":
            mode = mode.left
        elif c == "-":
            mode = mode.right
    return mode.data


if __name__ == "__main__":
    morseCode = make_morse_tree()
    str = input("입력 문장 : ")
    mlist = []
    for ch in str:
        code = encode(ch)
        mlist.append(code)
    print("Morse Code: ", mlist)
    print("Decoding: ", end="")
    for code in mlist:
        ch = decode(morseCode, code)
        print(ch, end="")
    print()
