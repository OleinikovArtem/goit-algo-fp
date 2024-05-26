# Task 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        self.head = reverse_list(self.head)

    def sort(self):
        self.head = merge_sort(self.head)


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sort(head):
    if not head or not head.next:
        return head
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list


def sorted_merge(a, b):
    result = None
    if not a:
        return b
    if not b:
        return a
    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result


def get_middle(head):
    if not head:
        return head
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


if __name__ == '__main__':
    # Створення і тестування однозв'язного списку
    ll = LinkedList()
    ll.append(4)
    ll.append(2)
    ll.append(3)
    ll.append(1)

    # Друк початкового списку
    print("Початковий список:")
    ll.print_list()

    # Реверсування списку
    ll.reverse()
    print("Реверсований список:")
    ll.print_list()

    # Сортування списку
    ll.sort()
    print("Відсортований список:")
    ll.print_list()

    # Створення двох відсортованих списків для об'єднання
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)

    # Друк початкових списків
    print("Список 1:")
    ll1.print_list()

    print("Список 2:")
    ll2.print_list()

    # Об'єднання списків
    merged_head = merge_sorted_lists(ll1.head, ll2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    # Друк об'єднаного списку
    print("Об'єднаний відсортований список:")
    merged_list.print_list()
