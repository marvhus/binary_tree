class Node:
    def __init__(self, val, childs=[]):
        self.val = val
        self.childs = []
        for child in childs:
            self.childs.append(child)

def traverse(node, spacing=""):
    print(f"{spacing}{node.val}")
    for child in node.childs:
        traverse(child, spacing + "\t")

stuff = Node(0, 
    childs = [
        Node(1,
            childs = [
                Node(2,
                    childs = [
                        Node(3),
                        Node(3)
                    ]
                ),
                Node(2,
                    childs = [
                        Node(3),
                        Node(3)
                    ]
                )
            ]
        ),
        Node(1,
            childs = [
                Node(2,
                    childs = [
                        Node(3),
                        Node(3)
                    ]
                ),
                Node(2,
                    childs = [
                        Node(3),
                        Node(3)
                    ]
                )
            ]
        )
    ]
)

traverse(stuff)
