#!/bin/sh
# Use ccache by default. Users who don't want that can set the CCACHE_DISABLE
# environment variable in their personal profile.
case ":${PATH:-}:" in
    *:/usr/lib64/ccache/bin:*) ;;
    *) PATH="/usr/lib64/ccache/bin${PATH:+:$PATH}" ;;
esac
