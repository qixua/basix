from utils.process_keymap import process_keymap
from utils.squeeze import squeeze


def encrypt(string: str, keymap_path: str) -> str:
    LENGTH = len(string)
    LENGTH_IS_EVEN = True if LENGTH % 2 == 0 else False
    KEYMAP = process_keymap(keymap_path)
    encrypted = string

    slide_amount = 0

    for i, c in enumerate(string):
        for k in KEYMAP:
            kv = k["v"]
            kc = k["c"]

            if kc == c:
                value_len = len(kv)
                slide_amount += value_len - 1 if value_len > 1 else 1

                encrypted = squeeze(
                    put=kv, into=i + slide_amount, at=encrypted)

        slide_amount += 1

    encrypted = f"{LENGTH}{encrypted}{LENGTH}{'+' if LENGTH_IS_EVEN else '-'}"

    return encrypted
