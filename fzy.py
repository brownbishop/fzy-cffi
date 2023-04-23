from _fzy import ffi
from _fzy import lib

def has_match(needle: str, haystack: str) -> bool:
    needle = ffi.new("char[]", needle.encode())
    haystack = ffi.new("char[]", haystack.encode())
    return bool(lib.has_match(needle, haystack))

def match_score(needle: str, haystack: str) -> float:
    needle = ffi.new("char[]", needle.encode())
    haystack = ffi.new("char[]", haystack.encode())
    return lib.match(needle, haystack)

def match_positions(needle: str, haystack: str) -> list[int]:
    n = len(needle)
    positions = ffi.new("size_t[" + n.__str__() + "]")
    needle = ffi.new("char[]", needle.encode())
    haystack = ffi.new("char[]", haystack.encode())
    lib.match_positions(needle, haystack, positions)
    return list(positions)
