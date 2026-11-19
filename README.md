# 图集打包：矩形、旋转与页溢出

图集边缘出现相邻图块的像素：矩形没有按高度排序，padding 只加一边，旋转后尺寸算错，页尺寸不是 2 的幂，mip 溢出没有留边，同图重复打包，淘汰没有按 LRU，单页溢出没分页，UV 没有归一化，批量页只提交一半。

## 目录结构

```
README.md
conftest.py
.gitignore
texture/__init__.py
texture/atlas.py
tests/test_atlas.py
```

## 当前状态

`texture/atlas.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_atlas.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 矩形按高度降序排列
2. 四周留 padding
3. 旋转后宽高交换
4. 页尺寸向上取 2 的幂
5. mip 级别留 bleed padding
6. 相同图片按内容去重
7. LRU 淘汰最久未用
8. 单页溢出分到下一页
9. UV 归一化到 0–1
10. 批量页统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `texture/atlas.py`
后 15 条用例应全部通过。
