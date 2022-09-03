from utils.process_keymap import process_keymap
from utils.squeeze import squeeze


def encrypt(string: str, keymap_path: str) -> str:
    LENGTH = len(string)
    LENGTH_IS_EVEN = True if LENGTH % 2 == 0 else False
    KEYMAP = process_keymap(keymap_path)
    encrypted = string

    i = 0
    char_i = 0
    stop = False

    while not stop:
        if i == len(string) - 1:
            for k in KEYMAP:
                kv = k["v"]
                kc = k["c"]

                if kc == string[-1]:
                    encrypted += kv
                    stop = True
        elif i < len(string) - 1:
            for k in KEYMAP:
                kv = k["v"]
                kc = k["c"]

                if char_i < len(encrypted) - 1 and kc == encrypted[char_i]:
                    encrypted = squeeze(
                        put=kv, into=char_i + 1, at=encrypted)
                    char_i += len(kv) + len(kc)

                    i += 1

    encrypted = f"{LENGTH}{encrypted}{LENGTH}{'+' if LENGTH_IS_EVEN else '-'}"

    return encrypted
