import pytest

from texture import atlas as mod

CASES = [
    ('sort_rects', [[(10, 20, 'a'), (30, 5, 'b'), (8, 20, 'c')]], [(10, 20, 'a'), (8, 20, 'c'), (30, 5, 'b')], False),
    ('pad_rect', [16, 8, 2], (20, 12), False),
    ('rotate_size', [16, 8, True], (8, 16), False),
    ('rotate_size', [16, 8, False], (16, 8), False),
    ('next_pow2', [17], 32, False),
    ('next_pow2', [16], 16, False),
    ('uv_rect', [16, 32, 8, 8, 128, 256], [0.125, 0.125, 0.0625, 0.03125], True),
    ('dedupe_key', ['grass', (32, 32)], 'grass:(32, 32)', False),
    ('lru_victim', [{'a': 3, 'b': 1, 'c': 2}], 'b', False),
    ('page_for', [9, 4], 2, False),
    ('bleed_padding', [2, 3], 8, False),
    ('commit_pages', [[True, True]], True, False),
    ('pad_rect', [1, 1, 0], (1, 1), False),
    ('next_pow2', [1], 1, False),
    ('page_for', [4, 4], 1, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_atlas_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
