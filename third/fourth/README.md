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

## 面试题18 树的子结构
