class Node(object):
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    @classmethod
    def sorted_array_to_bst(cls, nums):
        if not nums:
            return None

        mid_num = len(nums) // 2
        root = cls(nums[mid_num])
        root.left = cls.sorted_array_to_bst(nums[:mid_num])
        root.right = cls.sorted_array_to_bst(nums[(mid_num + 1):])
        return root

    def traverse(self, spacing=""):
        if self.val is None:
            return

        print(f"{spacing}{self.val}")

        if self.left:
            self.left.traverse(spacing + "\t")
        if self.right:
            self.right.traverse(spacing + "\t")
    
    def quick_find(self, val, loc=[]):
        # If found nothing
        if self.val != val and not self.left and not self.right:
            return

        if self.right and self.right.val and val >= self.right.val:
            loc.append(1)
            return self.right.quick_find(val, loc)
        
        # Val is on left side
        if self.left and self.left.val:
            loc.append(0)
            return self.left.quick_find(val, loc)

        loc.append(0)
        return loc

    def get_val(self, loc):
        if not loc:
            if self.val is None:
                return "no val"
            return self.val
        if loc[0] == 0:
            if self.left is None:
                return "no left"
            loc.pop(0)
            return self.left.get_val(loc)
        if loc[0] == 1:
            if self.right is None:
                return "no right"
            loc.pop(0)
            return self.right.get_val(loc)

def main():
    arr = [i for i in range(20)]
    node = Node.sorted_array_to_bst(arr)
    if node:
        node.traverse()
        find_val = int(input("Please enter a val to find:\n> "))
        loc = node.quick_find(find_val)
        if loc is None:
            print("Not found")
            return
        print("Location:", loc)
        print("Val:", node.get_val(loc))

if __name__ == '__main__':
    main()
