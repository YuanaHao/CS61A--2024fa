## SpecStory

## Fixing Item Assignment Error in Code (2025/1/22 13:52:43)

_**User**_

For the code present, we get this error:
```
'cnt' does not support item assignment
```
How can I resolve this? If you propose a fix, please make it concise.

---

_**Assistant**_

我注意到问题出在 `repeated` 函数中。错误的原因是 `cnt = list` 这一行有问题 - 这里应该创建一个字典来记录数字出现的次数，而不是使用 list 类型。

让我们修复这个问题：

```python:lab05.py
// ... existing code ...
def repeated(t, k):
    assert k > 1
    cnt = {}  # 改为使用字典而不是 list
    num = 0
    while True:
        num = next(t)
        if num not in cnt:  # 如果数字第一次出现
            cnt[num] = 1
        else:
            cnt[num] += 1
        if cnt[num] == k:
            return num
// ... existing code ...
```

主要修改：
1. 将 `cnt = list` 改为 `cnt = {}`
2. 添加了对新数字的处理逻辑
3. 调整了判断逻辑的顺序

这样就可以正确地统计连续出现的数字了。

---



---

