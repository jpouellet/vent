#!/bin/sh

cd "$(dirname "$0")"

/usr/local/sbin/thttpd -p 80 -d www -l - -u ubuntu -c '**.cgi' -D
