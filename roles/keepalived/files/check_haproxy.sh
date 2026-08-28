#!/bin/sh
echo "show info" | socat -T2 stdio /run/haproxy/admin.sock > /dev/null 2>&1