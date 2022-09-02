def process_keymap(abs_path: str) -> list[dict]:
    keymap = []

    with open(abs_path, "r") as keymap_raw:
        keymap_lines = keymap_raw.readlines()

        # to remove the \n at the end of every line
        # not len(l) - 2 as len() as 1-based
        for i, l in enumerate(keymap_lines):
            keymap_lines[i] = l[: len(l) - 1]

        for l in keymap_lines:
            keymap.append({"c": l[:1], "v": l[5:]})

    return keymap
