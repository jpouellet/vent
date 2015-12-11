#!/bin/sh

sudo thttpd -p 80 -d /home/pi/vent/temp-www -c 'api/**' -l - -u pi -D
