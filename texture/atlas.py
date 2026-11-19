"""图集打包：矩形、旋转与页溢出：待实现的核心模块。"""


def sort_rects(rects):
    """按高度降序排列矩形，保持稳定。"""
    raise NotImplementedError

def pad_rect(width, height, padding):
    """四周各留 padding。"""
    raise NotImplementedError

def rotate_size(width, height, rotated):
    """旋转 90 度后宽高交换。"""
    raise NotImplementedError

def next_pow2(value):
    """向上取 2 的幂。"""
    raise NotImplementedError

def uv_rect(x, y, width, height, page_width, page_height):
    """图块 UV 归一化到页尺寸。"""
    raise NotImplementedError

def dedupe_key(name, size):
    """相同图片按名称与尺寸去重。"""
    raise NotImplementedError

def lru_victim(entries):
    """返回最久未使用的页面/图块。"""
    raise NotImplementedError

def page_for(index, per_page):
    """单页溢出时分到下一页。"""
    raise NotImplementedError

def bleed_padding(padding, mip_count):
    """mip 级别越多，bleed 边越宽。"""
    raise NotImplementedError

def commit_pages(results):
    """批量页全部成功才提交。"""
    raise NotImplementedError
