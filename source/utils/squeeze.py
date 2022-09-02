def squeeze(*, put: str, into: int, at: str) -> str:
    return at[:into] + put + at[into:]
