#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -s -X OPTIONS "$1" -I | grep "Allow:" | cut -d' ' -f2-
