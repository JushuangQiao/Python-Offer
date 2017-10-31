# 4.4 分解让复杂问题简单化

## 面试题26 复杂链表的复制
> 要求：链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点
>
> 分为三步完成：
>
> 一:复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2
>
> 二:为每个新结点设置other指针
>
> 三:把复制后的结点链表拆开
>
> 题目设置了复杂链表的实现，测试代码见文件twenth_six.py
>
```python
class Solution(object):

    @staticmethod
    def clone_nodes(head):
        # 结点复制
        move = head
        while move:
            tmp = Node(move.val)
            tmp.next = move.next
            move.next = tmp
            move = tmp.next
        return head

    @staticmethod
    def set_nodes(head):
        # other指针设置
        move = head
        while move:
            m_next = move.next
            if move.other:
                m_next.other = move.other.next
            move = m_next.next
        return head

    @staticmethod
    def reconstruct_nodes(head):
        # 结点拆分
        ret = head.next if head else Node
        move = ret
        while head:
            head = move.next
            if head:
                move.next = head.next
                move = move.next
        return ret

    @staticmethod
    def clone_link(head):
        # 结果
        h = Solution.clone_nodes(head)
        h = Solution.set_nodes(h)
        ret = Solution.reconstruct_nodes(h)
        return ret
```

## 面试题27 二叉搜索树与双向链表

## 面试题28 字符串的排列
