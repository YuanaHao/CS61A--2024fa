## SpecStory

## Understanding List Append Behavior in Python (2025/1/22 13:52:43)

_**User**_

>>> s = [3]
>>> a.pop()
8
>>> a
[9, 7]
>>> s.extend([4, 5])
>>> a
[9, 7]
>>> s.extend([s.append(9), s.append(10)])
>>> s
[3, 4, 5, 9, 10, None, None]为什么s结果会有两个None

---

_**Assistant**_

让我解释一下为什么`s`的结果中会有两个`None`。

这是因为`list.append()`方法的返回值是`None`。让我们一步步分析这个过程：

1. 最初 `s = [3]`
2. 执行`s.extend([4, 5])`后，`s`变成 `[3, 4, 5]`
3. 然后执行`s.extend([s.append(9), s.append(10)])`
   - 首先执行`s.append(9)`，将9添加到s中，但这个操作返回`None`
   - 然后执行`s.append(10)`，将10添加到s中，但这个操作也返回`None`
   - 所以实际上是在执行`s.extend([None, None])`

所以最终的执行顺序是：
1. `s.append(9)` -> s变成`[3, 4, 5, 9]`，返回`None`
2. `s.append(10)` -> s变成`[3, 4, 5, 9, 10]`，返回`None`
3. `s.extend([None, None])` -> 将两个`None`添加到列表末尾

这就是为什么最终结果是`[3, 4, 5, 9, 10, None, None]`。

如果你想要避免这种情况，应该分开写这些操作：
```python
s = [3]
s.extend([4, 5])
s.append(9)
s.append(10)
# 现在 s 是 [3, 4, 5, 9, 10]
```

---



---

