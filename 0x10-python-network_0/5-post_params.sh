#!/bin/bash
# This bash script  takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sX POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
