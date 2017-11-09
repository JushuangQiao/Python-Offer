# 3.4 代码的鲁棒性

## 面试题15 链表中倒数第k个结点
> 要求：求单链表中的倒数第k个结点
>
> 思路：使用快慢指针，快的先走k-1步，需要考虑空链表以及k为0

```python
def last_kth(link, k):
    if not link or k <= 0:
        return None
    move = link
    while move and k-1 >= 0:
        move = move.next
        k -= 1
    while move:
        move = move.next
        link = link.next
    if k == 0:
        return link.val
    return None
```

## 面试题16 反转链表
> 要求：反转链表
>
> 思路：需要考虑空链表，只有一个结点的链表

```python
def reverse_link(head):
    if not head or not head.next:
        return head
    then = head.next
    head.next = None
    last = then.next
    while then:
        then.next = head
        head = then
        then = last
        if then:
            last = then.next
    return head
```

## 面试题17 合并两个排序的链表
> 要求：合并两个排序的链表
>
> 思路：使用递归

```python
def merge_link(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.val <= head2.val:
        ret = head1
        ret.next = merge_link(head1.next, head2)
    else:
        ret = head2
        ret.next = merge_link(head1, head2.next)
    return ret

```

## 面试题18 树的子结构
> 要求：判断一棵二叉树是不是另一个的子结构
>
> 思路：使用递归

```python
def sub_tree(tree1, tree2):
    if tree1 and tree2:
        if tree1.val == tree2.val:
            return sub_tree(tree1.left, tree2.left) and sub_tree(tree1.right, tree2.right)
        else:
            return sub_tree(tree1.left, tree2) or sub_tree(tree1.right, tree2)
    if not tree1 and tree2:
        return False
    return True
```
