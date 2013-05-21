from __future__ import unicode_literals

from spotify import ffi, lib


__all__ = [
    'Search',
]


class Search(object):
    """A Spotify search."""

    def __init__(self, sp_search):
        lib.sp_search_add_ref(sp_search)
        self.sp_search = ffi.gc(sp_search, lib.sp_search_release)

    def as_link(self):
        """Make a :class:`Link` to the search."""
        from spotify.link import Link
        return Link(self)

    # TODO Add sp_search_* methods
