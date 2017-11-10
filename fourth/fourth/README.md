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
> 要求: 将二叉搜索树转化成一个排序的双向链表，只调整树中结点的指向
>
> 思路: 中序遍历，根结点的left指向左子树的最后一个(最大)值，right指向右子树的(最小)值
>
> 注意: 题目构造了一个普通二叉树用来测试，构造时按照二叉搜索树的顺序输入结点，空结点用None表示，详情见twenty_seven.py
>

```python
class Solution(object):

    @staticmethod
    def convert(tree):
        """结点转换"""
        if not tree:
            return None
        p_last = Solution.convert_nodes(tree, None)
        while p_last and p_last.left:  # 获取链表头结点
            p_last = p_last.left
        return p_last

    @staticmethod
    def convert_nodes(tree, last):
        if not tree:
            return None
        if tree.left:
            last = Solution.convert_nodes(tree.left, last)
        if last:
            last.right = tree
        tree.left = last
        last = tree
        if tree.right:
            last = Solution.convert_nodes(tree.right, last)
        return last
```

## 面试题28 字符串的排列
> 要求：求输入字符串的全排列
>
> 思路：递归完成，也可以直接使用库函数
>

```python
def my_permutation(s):
    str_set = []
    ret = []  # 最后的结果

    def permutation(string):
        for i in string:
            str_tem = string.replace(i, '')
            str_set.append(i)
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            str_set.pop()

    permutation(s)
    return ret
```