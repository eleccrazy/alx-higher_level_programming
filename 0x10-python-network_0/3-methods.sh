#!/bin/bash
# This bash script takes in a URL and displays all HTTP methods the server will accept.
curl -siLX OPTIONS "$1" | grep Allow | cut -d " " -f 2-
