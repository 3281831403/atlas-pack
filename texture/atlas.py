"""图集打包：矩形、旋转与页溢出."""


def sort_rects(rects):
    """按高度降序排列矩形，保持稳定。"""
    # reverse=True 仍保持相等元素的原始相对顺序。
    return sorted(rects, key=lambda rect: rect[1], reverse=True)

def pad_rect(width, height, padding):
    """四周各留 padding。"""
    return (width + 2 * padding, height + 2 * padding)

def rotate_size(width, height, rotated):
    """旋转 90 度后宽高交换。"""
    if rotated:
        return (height, width)
    return (width, height)

def next_pow2(value):
    """向上取 2 的幂。"""
    if value <= 1:
        return 1
    result = 1
    while result < value:
        result <<= 1
    return result

def uv_rect(x, y, width, height, page_width, page_height):
    """图块 UV 归一化到页尺寸。"""
    if page_width <= 0 or page_height <= 0:
        raise ValueError("page dimensions must be positive")
    return [x / page_width, y / page_height,
            width / page_width, height / page_height]

def dedupe_key(name, size):
    """相同图片按名称与尺寸去重。"""
    if isinstance(size, list):
        size = tuple(size)
    return f"{name}:{size}"

def lru_victim(entries):
    """返回最久未使用的页面/图块。"""
    if not entries:
        raise ValueError("entries must not be empty")
    return min(entries, key=entries.get)

def page_for(index, per_page):
    """单页溢出时分到下一页。"""
    if per_page <= 0:
        raise ValueError("per_page must be positive")
    if index < 0:
        raise ValueError("index must be non-negative")
    return index // per_page

def bleed_padding(padding, mip_count):
    """mip 级别越多，bleed 边越宽。"""
    if mip_count <= 1:
        return padding
    return padding * (1 << (mip_count - 1))

def commit_pages(results):
    """批量页全部成功才提交。"""
    for page in results:
        if isinstance(page, (list, tuple)):
            if not all(bool(item) for item in page):
                return False
        elif not page:
            return False
    return True
