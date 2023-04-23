from cffi import FFI

CDEF = '''\
typedef double score_t;

#define MATCH_MAX_LEN 1024

int has_match(const char *needle, const char *haystack);
score_t match_positions(const char *needle, const char *haystack, size_t *positions);
score_t match(const char *needle, const char *haystack);
'''

SRC = '#include "match.h"'

ffibuilder = FFI()
ffibuilder.cdef(CDEF)
ffibuilder.set_source(
    '_fzy', SRC,
    sources=['./deps/fzy/src/match.c'],
    include_dirs=['./deps/fzy/src'],
)
